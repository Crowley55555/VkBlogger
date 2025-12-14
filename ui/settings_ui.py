import pygame
from ui.widget import Button, TextInput
import json

class SettingsUI:
    def __init__(self, screen: pygame.Surface, config_manager):
        self.screen = screen
        self.config_manager = config_manager
        self.inputs = []
        self.buttons = []
        self.dropdowns = {}
        self.checkboxes = {}
        self._create_ui()

    def _create_ui(self):
        center_x = self.screen.get_width() // 2
        input_width, input_height = 400, 50
        margin = 20
        y_pos = 80

        # Blog Topic
        self.inputs.append(
            TextInput(center_x - input_width // 2, y_pos, input_width, input_height, "Тема блога")
        )
        self.inputs[-1].text = self.config_manager.config.get("blog_topic", "")
        y_pos += input_height + margin

        # Group ID
        self.inputs.append(
            TextInput(center_x - input_width // 2, y_pos, input_width, input_height, "ID группы ВК")
        )
        self.inputs[-1].text = str(self.config_manager.config.get("group_id", ""))
        y_pos += input_height + margin

        # Access Token
        self.inputs.append(
            TextInput(center_x - input_width // 2, y_pos, input_width, input_height, "Access Token", password=True)
        )
        self.inputs[-1].text = self.config_manager.config.get("access_token", "")
        y_pos += input_height + margin

        # AI Model Dropdown
        models = ["gigachat", "yandexgpt", "openrouter", "gpt4o", "gpt5"]
        self.dropdowns["ai_model"] = {
            "options": models,
            "selected": self.config_manager.config.get("ai_model", models[0]),
            "rect": pygame.Rect(center_x - input_width // 2, y_pos, input_width, input_height),
            "open": False
        }
        y_pos += input_height + margin

        # Post Style Dropdown
        styles = ["аналитический", "официальный", "мемный", "юмористический"]
        self.dropdowns["post_style"] = {
            "options": styles,
            "selected": self.config_manager.config.get("post_style", styles[0]),
            "rect": pygame.Rect(center_x - input_width // 2, y_pos, input_width, input_height),
            "open": False
        }
        y_pos += input_height + margin

        # Generate Images Checkbox
        self.checkboxes["generate_images"] = {
            "rect": pygame.Rect(center_x - input_width // 2, y_pos + 10, 20, 20),
            "label_rect": pygame.Rect(center_x - input_width // 2 + 30, y_pos, 300, 30),
            "label": "Генерировать изображения",
            "checked": self.config_manager.config.get("generate_images", False)
        }
        y_pos += 50 + margin

        # Posting Frequency
        self.inputs.append(
            TextInput(center_x - input_width // 2, y_pos, input_width, input_height, "Частота публикаций (часы)")
        )
        self.inputs[-1].text = str(self.config_manager.config.get("posting_frequency", 24))
        y_pos += input_height + margin

        # Save Button
        self.buttons.append(
            Button(
                center_x - 100,
                y_pos,
                200,
                60,
                "Сохранить",
                on_click=self.save_settings
            )
        )
        y_pos += 70

        # Back Button
        self.buttons.append(
            Button(
                center_x - 100,
                y_pos,
                200,
                60,
                "Назад",
                on_click=lambda: self.handle_event({"type": "action", "action": "back"})
            )
        )

    def save_settings(self):
        self.config_manager.update_config("blog_topic", self.inputs[0].text)
        self.config_manager.update_config("group_id", self.inputs[1].text)
        self.config_manager.update_config("access_token", self.inputs[2].text)
        self.config_manager.update_config("ai_model", self.dropdowns["ai_model"]["selected"])
        self.config_manager.update_config("post_style", self.dropdowns["post_style"]["selected"])
        self.config_manager.update_config("generate_images", self.checkboxes["generate_images"]["checked"])
        try:
            freq = int(self.inputs[3].text)
            self.config_manager.update_config("posting_frequency", max(1, freq))
        except ValueError:
            pass

    def render(self):
        title_font = pygame.font.Font(None, 48)
        title_surf = title_font.render("Настройки", True, (100, 200, 255))
        title_rect = title_surf.get_rect(center=(self.screen.get_width() // 2, 40))
        self.screen.blit(title_surf, title_rect)

        font = pygame.font.Font(None, 32)
        dropdown_font = pygame.font.Font(None, 28)

        for inp in self.inputs:
            inp.render(self.screen)

        for name, dropdown in self.dropdowns.items():
            pygame.draw.rect(self.screen, (50, 50, 100), dropdown["rect"], border_radius=8)
            pygame.draw.rect(self.screen, (200, 200, 200), dropdown["rect"], 2, border_radius=8)
            text = dropdown_font.render(dropdown["selected"], True, (255, 255, 255))
            text_rect = text.get_rect(center=dropdown["rect"].center)
            self.screen.blit(text, text_rect)

        for name, cb in self.checkboxes.items():
            color = (100, 100, 150) if cb["checked"] else (50, 50, 100)
            pygame.draw.rect(self.screen, color, cb["rect"])
            pygame.draw.rect(self.screen, (200, 200, 200), cb["rect"], 1)
            label_surf = font.render(cb["label"], True, (200, 200, 200))
            self.screen.blit(label_surf, cb["label_rect"])

        for button in self.buttons:
            button.render(self.screen)

    def handle_event(self, event) -> str:
        # Проверяем, является ли event словарем (а не pygame.Event)
        if isinstance(event, dict) and "action" in event:
            return event["action"]

        for inp in self.inputs:
            inp.handle_event(event)

        for name, cb in self.checkboxes.items():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if cb["rect"].collidepoint(event.pos):
                    cb["checked"] = not cb["checked"]
                    return ""

        for name, dropdown in self.dropdowns.items():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if dropdown["rect"].collidepoint(event.pos):
                    dropdown["open"] = not dropdown["open"]
                elif dropdown["open"]:
                    # Click outside - close
                    dropdown["open"] = False
                    # Check if click was on an option
                    for i, option in enumerate(dropdown["options"]):
                        option_rect = pygame.Rect(dropdown["rect"].x, dropdown["rect"].y + (i + 1) * 30, dropdown["rect"].width, 30)
                        if option_rect.collidepoint(event.pos):
                            dropdown["selected"] = option
                            break

        for button in self.buttons:
            if button.handle_event(event):
                if button.text == "Назад":
                    return "back"
                elif button.text == "Сохранить":
                    self.save_settings()
        return ""