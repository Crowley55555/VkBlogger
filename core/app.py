import pygame
from ui.main_menu_ui import MainMenuUI
from ui.settings_ui import SettingsUI
from core.config_manager import ConfigManager

class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("AutoBlog VK")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = "main_menu"  # 'main_menu', 'settings', 'running'

        self.config_manager = ConfigManager("config.json")
        self.main_menu_ui = MainMenuUI(self.screen)
        self.settings_ui = SettingsUI(self.screen, self.config_manager)

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state == "main_menu":
                action = self.main_menu_ui.handle_event(event)
                if action == "settings":
                    self.state = "settings"
                elif action == "start":
                    self.state = "running"
                    self.start_autoposting()

            elif self.state == "settings":
                action = self.settings_ui.handle_event(event)
                if action == "back":
                    self.state = "main_menu"

    def render(self):
        self.screen.fill((25, 25, 35))
        if self.state == "main_menu":
            self.main_menu_ui.render()
        elif self.state == "settings":
            self.settings_ui.render()
        pygame.display.flip()

    def start_autoposting(self):
        # Placeholder for autoposting logic
        print("Autoposting started with config:", self.config_manager.config)
        self.running = False  # For demo
