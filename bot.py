# imports
from aiogram import Bot, executor, types, Dispatcher
from config import TOKEN, open_weather_token
import logging
from aiogram.types import ReplyKeyboardMarkup
import requests
import datetime

# logging
logging.basicConfig(level=logging.INFO)

# keyboard cities
button3 = 'Зеленоград'
button4 = 'Московский'
button5 = 'Троицк'
button6 = 'Щербинка'
button7 = 'Апрелевка'
button8 = 'Балашиха'
button9 = 'Белоозёрский'
button10 = 'Бронницы'
button11 = 'Верея'
button12 = 'Видное'
button13 = 'Волоколамск'
button14 = 'Воскресенск'
button15 = 'Высоковск'
button16 = 'Голицыно'
button17 = 'Дедовск'
button18 = 'Дзержинский'
button19 = 'Дмитров'
button20 = 'Долгопрудный'
button21 = 'Домодедово'
button22 = 'Дрезна'
button23 = 'Дубна'
button24 = 'Егорьевск'
button25 = 'Жуковский'
button26 = 'Зарайск'
button27 = 'Звенигород'
button28 = 'Ивантеевка'
button29 = 'Istra'
button30 = 'Кашира'
button31 = 'Клин'
button32 = 'Коломна'
button33 = 'Королёв'
button34 = 'Котельники'
button35 = 'Красноармейск'
button36 = 'Красногорск'
button37 = 'Краснозаводск'
button38 = 'Краснознаменск'
button39 = 'Кубинка'
button40 = 'Куровское'
button41 = 'Ликино-Дулёво'
button42 = 'Лобня'
button43 = 'Лосино-Петровский'
button44 = 'Луховицы'
button45 = 'Лыткарино'
button46 = 'Люберцы'
button47 = 'Можайск'
button48 = 'Мытищи'
button49 = 'Наро-Фоминск'
button50 = 'Ногинск'
button51 = 'Одинцово'
button52 = 'Озёры'
button53 = 'Орехово-Зуево'
button54 = 'Павловский Посад'
button55 = 'Пересвет'
button56 = 'Подольск'
button57 = 'Протвино'
button58 = 'Пушкино'
button59 = 'Пущино'
button60 = 'Раменское'
button61 = 'Реутов'
button62 = 'Рошаль'
button63 = 'Руза'
button64 = 'Сергиев Посад'
button65 = 'Серпухов'
button66 = 'Солнечногорск'
button67 = 'Старая Купавна'
button68 = 'Ступино'
button69 = 'Талдом'
button70 = 'Фрязино'
button71 = 'Химки'
button72 = 'Хотьково'
button73 = 'Черноголовка'
button74 = 'Чехов'
button75 = 'Шатура'
button76 = 'Щёлково'
button77 = 'Электрогорск'
button78 = 'Электросталь'
button79 = 'Электроугли'
button80 = 'Яхрома'


cities = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button3).add(button4).add(
    button5).add(button6).add(button7).add(
    button8).add(button9).add(button10).add(button11).add(button12).add(button13).add(button14).add(button15).add(
    button16).add(button17).add(
    button18).add(button19).add(button20).add(button21).add(button22).add(button23).add(button24).add(button25).add(
    button26).add(button27).add(button28).add(button29).add(button30).add(button31).add(button32).add(button33).add(
    button34).add(button35).add(button36).add(button37).add(button38).add(button39).add(button40).add(button41).add(
    button42).add(button43).add(button44).add(button45).add(button46).add(button47).add(button48).add(button49).add(
    button50).add(button52).add(button53).add(button54).add(button55).add(button56).add(button57).add(button58).add(
    button59).add(button60).add(button61).add(button62).add(button63).add(button64).add(button65).add(button66).add(
    button67).add(button68).add(button69).add(button70).add(button71).add(button72).add(button73).add(button74).add(
    button75).add(button76).add(button77).add(button78).add(button79).add(button80)

# keyboard 4
button81 = 'Назад'
keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button81)

# init
bot = Bot(TOKEN)
dp = Dispatcher(bot)


# handlers

# start-handler
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Привет, я - бот для сообщения погоды, выбери свой город.\nЕсли его тут нет, то просто напиши! '
                         '\nЯ не могу говорить погоду в: деревнях, сёлах и тп...',
                         reply_markup=cities)


# check-weather handler
@dp.message_handler()
async def get_weather(meessage: types.Message):
    code_to_smile = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={meessage.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data['name']
        cur_weather = data['main']['temp']

        weater_discription = data['weather'][0]["main"]
        if weater_discription in code_to_smile:
            wd = code_to_smile[weater_discription]
        else:
            wd = 'Посмотри в окно, не пойму, что там за погода'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - datetime.datetime.fromtimestamp(
            data['sys']['sunrise'])

        await meessage.answer(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H-%M')}***\n"
                              f'Погода в городе {city}\nТемпература: {int(cur_weather)}C° {wd}\n'
                              f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с  \n"
                              f"Восход солнца {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {length_of_the_day}\n"
                              f"Хорошего дня!"
                              )

    except:
        await meessage.answer('Проверте название города: ')


# start-polling
executor.start_polling(dp)
