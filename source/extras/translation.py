"""
File with gettext alias
"""
from pathlib import Path

from aiogram.contrib.middlewares.i18n import I18nMiddleware

_ = i18n = I18nMiddleware("Bot", Path(__file__).parents[2] / "locales").gettext