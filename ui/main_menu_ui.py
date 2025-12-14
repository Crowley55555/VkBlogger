import pygame
from ui.widget import Button

class MainMenuUI:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.buttons = []
        self._create_ui()

    def _create_ui(self):
        center_x = self.screen.get_width() // 2
        button_width, button_height = 300, 60
        spacing = 20

        self.buttons.append(
            Button(
                center_x - button_width // 2,
                200,
                button_width,
                button_height,
                "Настройки",
                on_click=lambda: self.handle_event({"type": "action", "action": "settings"})
            )
        )
        self.buttons.append(
            Button(
                center_x - button_width // 2,
                300,
                button_width,
                button_height,
                "Запустить автопостинг",
                on_click=lambda: self.handle_event({"type": "action", "action": "start"})
            )
        )

    def render(self):
        title_font = pygame.font.Font(None, 64)
        title_surf = title_font.render("AutoBlog VK", True, (100, 200, 255))
        title_rect = title_surf.get_rect(center=(self.screen.get_width() // 2, 100))
        self.screen.blit(title_surf, title_rect)

        for button in self.buttons:
            button.render(self.screen)

    def handle_event(self, event) -> str:
        # Проверяем, является ли event словарем (а не pygame.Event)
        if isinstance(event, dict) and "action" in event:
            return event["action"]

        for button in self.buttons:
            if button.handle_event(event):
                if button.text == "Настройки":
                    return "settings"
                elif button.text == "Запустить автопостинг":
                    return "start"
        return ""