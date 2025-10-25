from aiogram.filters.state import State,StatesGroup
class ReklamaState(StatesGroup):
    add = State()
    check = State()
class TextState(StatesGroup):
    text = State()
    url = State()
    check = State()
class ImageState(StatesGroup):
    image = State()
    url = State()
    check = State()
class VideoState(StatesGroup):
    video = State()
    url = State()
    check = State()
class AddChannelState(StatesGroup):
    id = State()
    check = State()
class LanguageState(StatesGroup):
    language_get = State()