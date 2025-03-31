import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from book import relationship_thinks, amicability_thinks, anarchy_thinks, joy_and_beautiful_thinks,\
    sensitivity_thinks, matimatic_thinks, fantasy_thinks, nature_thinks, resoluteness_thinks, \
    clarity_thinks, open_system_thinks, art_thinks, independence_thinks
from links import thoughts_about_links, mood_links, feelings_links, peace_links, talk_links, \
    artistic_links
from aiogram.enums import ParseMode
import random

bot = Bot('7562834452:AAEIIJgkLUXW1cVshDRtbQINhB_V5Au056g')

dp = Dispatcher()

@dp.message(Command('menu', 'start'))
async def start(message: types.Message):
    await message.answer(
        """Привет, друг! Что ты хочешь получить?
- <a href="/thinks">/thinks</a> - мысли
- <a href="/тексты">/texts</a> - тексты""",
        parse_mode=ParseMode.HTML
    )

@dp.message(Command('thinks'))
async def send_random_value(message: types.CallbackQuery):
    await message.answer(
        """О чем?
- <a href="/relationship">/relationship</a> - отношения
- <a href="/amicability">/amicability</a> - дружелюбие
- <a href="/anarchy">/anarchy</a> - безвластие и анархия
- <a href="/joy">/joy</a> - радость и красота
- <a href="/art">/art</a> - художественная свобода
- <a href="/sensitivity">/sensitivity</a> - чуткость
- <a href="/math">/math</a> - математиkа
- <a href="/fantasy">/fantasy</a> - фантазия
- <a href="/nature">/nature</a> - природа
- <a href="/resoluteness">/resoluteness</a> - решительность
- <a href="/clarity">/clarity</a> - открытость и прозрачность
- <a href="/open_system">/open_system</a> - открытая система
- <a href="/independence">/independence</a> - самостоятельность
- <a href="/start">/start</a> - в начало""",
        parse_mode=ParseMode.HTML)

@dp.message(Command('relationship'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(relationship_thinks) - 1)
    text = relationship_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('amicability'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(amicability_thinks) - 1)
    text = amicability_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('anarchy'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(anarchy_thinks) - 1)
    text = anarchy_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('joy'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(joy_and_beautiful_thinks) - 1)
    text = joy_and_beautiful_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('sensitivity'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(sensitivity_thinks) - 1)
    text = sensitivity_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('math'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(matimatic_thinks) - 1)
    text = matimatic_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('fantasy'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(fantasy_thinks) - 1)
    text = fantasy_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('sensitivity'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(sensitivity_thinks) - 1)
    text = sensitivity_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('nature'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(nature_thinks) - 1)
    text = nature_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('resoluteness'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(resoluteness_thinks) - 1)
    text = resoluteness_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('clarity'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(clarity_thinks) - 1)
    text = clarity_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('open_system'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(open_system_thinks) - 1)
    text = open_system_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('art'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(art_thinks) - 1)
    text = art_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('independence'))
async def send_random_value(message: types.CallbackQuery):
    random_index = random.randint(0, len(independence_thinks) - 1)
    text = independence_thinks[random_index] + """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('texts'))
async def send_random_value(message: types.CallbackQuery):
    await message.answer(
        """О чем?
- <a href="/thoughts_about">/thoughts_about</a> - мысли о ком-то
- <a href="/mood">/mood</a> - создать настроение
- <a href="/peace">/peace</a> - преодоление насилия
- <a href="/feelings">/feelings</a> - о людях и чувствах
- <a href="/talk">/talk</a> - идеи для разговора
- <a href="/artistic">/artistic</a> - художественное мышление
- <a href="/start">/start</a> - в начало""",
        parse_mode=ParseMode.HTML)

@dp.message(Command('thoughts_about'))
async def send_random_value(message: types.CallbackQuery):
    text = ""
    for theme in thoughts_about_links:
        text += f"""
<a href="{theme['link']}">{theme['title']}</a>"""

    text += """
    
<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)


@dp.message(Command('mood'))
async def send_random_value(message: types.CallbackQuery):
    text = ""
    for theme in mood_links:
        text += f"""
<a href="{theme['link']}">{theme['title']}</a>"""

    text += """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('feelings'))
async def send_random_value(message: types.CallbackQuery):
    text = ""
    for theme in feelings_links:
        text += f"""
<a href="{theme['link']}">{theme['title']}</a>"""

    text += """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('peace'))
async def send_random_value(message: types.CallbackQuery):
    text = ""
    for theme in peace_links:
        text += f"""
<a href="{theme['link']}">{theme['title']}</a>"""

    text += """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('talk'))
async def send_random_value(message: types.CallbackQuery):
    text = ""
    for theme in talk_links:
        text += f"""
<a href="{theme['link']}">{theme['title']}</a>"""

    text += """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

@dp.message(Command('artistic'))
async def send_random_value(message: types.CallbackQuery):
    text = ""
    for theme in artistic_links:
        text += f"""
<a href="{theme['link']}">{theme['title']}</a>"""

    text += """

<a href='/start'>/start</a> - в начало"""
    await message.answer(text, parse_mode=ParseMode.HTML)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())