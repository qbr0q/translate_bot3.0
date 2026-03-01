from app.database.models import RussianWord, ItalianWord


MODEL_TO_COMMAND_MAP = {
    "/add_ru": RussianWord,
    "/add_it": ItalianWord
}
