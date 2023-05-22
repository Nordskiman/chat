import aiogram
import config
import logging
import openai

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = aiogram.Bot(token=config.TOKEN)
dp = aiogram.Dispatcher(bot)
openai.api_key = config.API_OPENAI_KEY
model_engine = "text-davinci-003"


@dp.message_handler(commands="start")
async def start(message: aiogram.types.Message):
    user = message.from_user
    text_msg = f"Добро пожаловать, {user.first_name}!!!"
    text_msg += f"\n\nЗадай мне вопрос"
    await message.answer(text_msg)


@dp.message_handler()
async def chatiko(message: aiogram.types.Message):
    prompt = message.text

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    await message.answer(completion.choices[0].text)


if __name__ == "__main__":
    aiogram.executor.start_polling(dp, skip_updates=True)
