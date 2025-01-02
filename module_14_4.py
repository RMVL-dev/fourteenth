from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import API
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions

vitamins = crud_functions.get_all_products()
api = API.apiKey
bot = Bot(token=api)
crud_functions.initiate_db()

dispatcher = Dispatcher(bot=bot, storage=MemoryStorage())

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
main_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

inline_keyboard = InlineKeyboardMarkup()
buying_keyboard = InlineKeyboardMarkup()

inline_keyboard.row(InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="Calories"),
                    InlineKeyboardButton(text="Формулы расчета", callback_data="formulas"))

buying_keyboard.row(InlineKeyboardButton(text=vitamins[0].name, callback_data="product_buying"),
                    InlineKeyboardButton(text=vitamins[1].name, callback_data="product_buying"),
                    InlineKeyboardButton(text=vitamins[2].name, callback_data="product_buying"),
                    InlineKeyboardButton(text=vitamins[3].name, callback_data="product_buying"),
                    )

calories_button = KeyboardButton(text="Рассчитать")
start_button = KeyboardButton(text="/start")
info_button = KeyboardButton(text="Информация")
buy_button = KeyboardButton(text="Купить")

start_keyboard.add(start_button)
main_keyboard.row(calories_button, info_button)
main_keyboard.add(buy_button)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dispatcher.message_handler(text="Купить")
async def get_buying_list(message):
    for vitamin in vitamins:
        with open(vitamin.resource_url, "rb") as img:
            await message.answer_photo(img,
                                       f"Название: {vitamin.name} | Описание: описание №{vitamin.description} | Цена: {vitamin.price}")
    await message.answer("Выберите продукт для покупки:", reply_markup=buying_keyboard)


@dispatcher.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()


@dispatcher.message_handler(text="Рассчитать")
async def main_menu(ms):
    await ms.answer("Выберите опцию:", reply_markup=inline_keyboard)


@dispatcher.callback_query_handler(text="Calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст")
    await UserState.age.set()
    await call.answer()


@dispatcher.callback_query_handler(text="formulas")
async def get_formulas(call):
    await call.message.answer("10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5")
    await call.answer()


@dispatcher.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост")
    await UserState.growth.set()


@dispatcher.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес")
    await UserState.weight.set()


@dispatcher.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    try:
        await message.answer(
            f"Ваша норма калирий {float(data['weight']) * 10 + float(data['growth']) * 6.25 - float(data['age']) * 5 + 5}")
    except ValueError:
        await message.answer("Вы ввели не верные данные")
    finally:
        await state.finish()


@dispatcher.message_handler(commands="start")
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=main_keyboard)


@dispatcher.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.", reply_markup=start_keyboard)


if __name__ == "__main__":
    executor.start_polling(dispatcher, skip_updates=True)
