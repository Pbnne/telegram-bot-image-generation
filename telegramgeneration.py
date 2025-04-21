import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from g4f.client import Client
# Токен вашего Telegram-бота
TELEGRAM_TOKEN = 'Твой токен'
# Инициализация бота
bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
# Создаём экземпляр клиента для генерации изображений
client = Client()
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Напиши мне описание, и я сгенерирую изображение.")
@dp.message_handler()
async def generate_image(message: types.Message):
    # Сохраняем сообщение пользователя в переменную sms
    sms = message.text
    
    # Отправляем запрос на генерацию изображения по заданному промпту
    response = await client.images.async_generate(
        model="flux",
        prompt=sms,
        response_format="url"
    )
    
    # Получаем URL сгенерированного изображения
    image_url = response.data[0].url
    print(f"URL сгенерированного изображения: {image_url}")
    
    # Отправляем ссылку на сгенерированное изображение пользователю в Telegram
    await message.reply(f"Вот ваша сгенерированная картинка: {image_url}")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
