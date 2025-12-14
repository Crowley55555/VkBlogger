import pygame
from typing import Tuple, Optional

class Button:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        text: str,
        on_click=None,
        color: Tuple[int, int, int] = (70, 130, 180),
        hover_color: Tuple[int, int, int] = (100, 149, 237)
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.on_click = on_click
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.Font(None, 32)

    def render(self, screen: pygame.Surface):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        pygame.draw.rect(screen, (200, 200, 200), self.rect, 2, border_radius=8)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.on_click:
                    self.on_click()
                return True
        return False


class TextInput:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        label: str = "",
        password: bool = False
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.label = label
        self.text = ""
        self.active = False
        self.password = password
        self.font = pygame.font.Font(None, 32)
        self.label_font = pygame.font.Font(None, 24)

    def render(self, screen: pygame.Surface):
        # Render label
        if self.label:
            label_surf = self.label_font.render(self.label, True, (200, 200, 200))
            screen.blit(label_surf, (self.rect.x, self.rect.y - 25))

        # Render input box
        color = (100, 100, 150) if self.active else (50, 50, 100)
        pygame.draw.rect(screen, color, self.rect, border_radius=8)
        pygame.draw.rect(screen, (200, 200, 200), self.rect, 2, border_radius=8)

        # Render text
        display_text = self.text if not self.password else "*" * len(self.text)
        text_surf = self.font.render(display_text, True, (255, 255, 255))
        screen.blit(text_surf, (self.rect.x + 10, self.rect.y + 10))

    def handle_event(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            return True

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                return True
            else:
                self.text += event.unicode
        return False