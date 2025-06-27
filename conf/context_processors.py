from conf import global_config


def global_context(request):
    return {
        "support_email": "support@example.com",
        "project_name": global_config.project_name,
        # Можешь добавить сюда меню, данные из settings, и т.д.
        "main_menu": [
            {"title": "Главная 🏠", "url": "/"},
            {"title": "Категории 📂", "url": "/categories"},
            {"title": "Случайная игра 🎲", "url": "/random"},
            {"title": "О проекте ℹ️", "url": "/about"},
        ],
        "dropdown_menu": [
            {"title": "👤 Моя страница", "url": "/"},
            {"title": "➕ Добавить игру", "url": "/add_game"},
            {"title": "dropdown-divider"},
            {"title": "🚪 Выход", "url": "/"},
        ],
    }
