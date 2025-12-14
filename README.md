# VkBlogger

Приложение-ассистент для автоматического ведения блога во ВКонтакте.

## Описание

VkBlogger — это десктопное приложение на Python с использованием Pygame, которое автоматически публикует посты во ВКонтакте на заданную пользователем тему. Приложение использует ИИ для генерации текста и изображений, а также может получать свежие новости из RSS-лент.

## Особенности

- Автоматическая генерация постов с помощью ИИ (GigaChat, YandexGPT, GPT-4o и др.)
- Поддержка различных стилей постов: аналитический, официальный, мемный, юмористический
- Генерация изображений к постам
- Настраиваемая частота публикаций
- Простой и интуитивный интерфейс на Pygame
- Сохранение настроек между сессиями

## Требования

- Python 3.8+
- Pygame
- Pillow
- requests
- feedparser
- openai (опционально)
- python-dotenv (опционально)

## Установка

```bash
pip install pygame pillow requests feedparser
```

Для использования OpenAI моделей:
```bash
pip install openai
```

## Запуск

```bash
cd VkBlogger/autoblog_vk
python main.py
```

## Конфигурация

Настройки хранятся в файле `config.json`. При первом запуске будет создан с значениями по умолчанию.

## Архитектура

Проект следует принципам SOLID и DRY, использует чистую ООП-архитектуру и легко расширяется.

```
autoblog_vk/
├── core/
│   ├── app.py
│   └── config_manager.py
├── ui/
│   ├── settings_ui.py
│   ├── main_menu_ui.py
│   └── widget.py
├── news/
│   ├── news_fetcher.py
│   ├── rss_fetcher.py
│   └── news_parser.py
├── ai/
│   ├── base_model.py
│   ├── gigachat_model.py
│   ├── yandexgpt_model.py
│   ├── openrouter_model.py
│   ├── gpt4o_model.py
│   ├── gpt5_model.py
│   └── image_generator.py
├── post/
│   ├── post_generator.py
│   ├── style_presets.py
│   └── post.py
├── vk/
│   ├── vk_publisher.py
│   └── vk_auth.py
├── utils/
│   ├── logger.py
│   └── file_manager.py
└── main.py
```

## Лицензия

MIT
