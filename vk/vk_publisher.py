import requests
from post.post import Post
from typing import Dict, Any

class VKPublisher:
    def __init__(self, access_token: str, group_id: str):
        self.access_token = access_token
        self.group_id = group_id
        self.api_url = "https://api.vk.com/method"
        self.version = "5.131"

    def _call_api(self, method: str, **params) -> Dict[Any, Any]:
        params.update({
            "access_token": self.access_token,
            "v": self.version
        })
        response = requests.get(f"{self.api_url}/{method}", params=params)
        return response.json()

    def upload_photo_to_server(self, photo_path: str) -> Dict[str, str]:
        # Get server for photo upload
        upload_server_response = self._call_api(
            "photos.getWallUploadServer",
            group_id=self.group_id
        )
        if "response" not in upload_server_response:
            raise Exception(f"Failed to get upload server: {upload_server_response}")

        upload_url = upload_server_response["response"]["upload_url"]

        # Upload photo to server
        with open(photo_path, 'rb') as f:
            files = {'photo': f}
            response = requests.post(upload_url, files=files)

        result = response.json()
        if "photo" not in result:
            raise Exception(f"Failed to upload photo: {result}")
        
        return result

    def save_wall_photo(self, upload_response: Dict[str, str]) -> Dict[str, Any]:
        # Save photo to wall
        response = self._call_api(
            "photos.saveWallPhoto",
            group_id=self.group_id,
            photo=upload_response["photo"],
            server=upload_response["server"],
            hash=upload_response["hash"]
        )
        if "response" not in response:
            raise Exception(f"Failed to save photo: {response}")
        return response["response"][0]  # Return photo info

    def publish_post(self, post: Post) -> bool:
        try:
            attachments = []
            message = post.to_dict()["text"]

            if post.image_path:
                # Upload and attach image
                upload_response = self.upload_photo_to_server(post.image_path)
                saved_photo = self.save_wall_photo(upload_response)
                media_id = saved_photo["id"]
                owner_id = saved_photo["owner_id"]
                attachments.append(f"photo{owner_id}_{media_id}")

            # Publish on wall
            response = self._call_api(
                "wall.post",
                owner_id=-int(self.group_id),
                from_group=1,
                message=message,
                attachments=",".join(attachments) if attachments else None
            )

            if "response" in response:
                print(f"Post published successfully: https://vk.com/wall-{self.group_id}_{response['response']['post_id']}")
                return True
            else:
                print(f"Failed to publish post: {response}")
                return False

        except Exception as e:
            print(f"Error publishing post: {e}")
            return False