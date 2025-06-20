from conf import global_config


def global_context(request):
    return {
        "support_email": "support@example.com",
        "project_name": global_config.project_name,
        # Можешь добавить сюда меню, данные из settings, и т.д.
        "main_menu": [
            {"title": "Главная", "url": "/", "icon": "bi-house"},
            {"title": "Категории", "url": "/categories", "icon": "bi-grid"},
            {"title": "О проекте", "url": "/about", "icon": "bi-info-circle"},
        ],
        "dropdown_menu": [
            {"title": "👤 Моя страница", "url": "/", "icon": "bi-house"},
            {"title": "➕ Добавить игру", "url": "/add_game", "icon": "bi-house"},
            {"title": "dropdown-divider"},
            {"title": "🚪 Выход", "url": "/", "icon": "bi-house"},
        ],
    }
