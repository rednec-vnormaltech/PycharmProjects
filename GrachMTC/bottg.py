import telebot
from bs4 import BeautifulSoup
import requests
import datetime

# Токен вашего Telegram бота
bot = telebot.TeleBot('5749610539:AAHeIhyijfUuF1l2QO0FQRGBiLCMPDCmpd0')


#Блок получения  погоды с сайта www.openweathermap.org
# Замените 'YOUR_API_KEY' на ваш реальный API-ключ OpenWeatherMap
api_key = '3d2f6d71c83830e0f7a52359215f1940'

# Задайте город, для которого вы хотите получить информацию о погоде
city = 'Moscow'

# Формируйте URL для запроса к API
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Отправьте GET-запрос к API и получите ответ
response = requests.get(url)

# Проверьте, что запрос выполнен успешно
if response.status_code == 200:
    data = response.json()

    # Извлеките информацию о погоде, например, температуру
    temperature_kelvin = data['main']['temp']
    temperature_celsius = temperature_kelvin - 273.15

    # Дополнительно извлеките информацию о ветре, давлении, влажности и точке росы
    wind_speed = data['wind']['speed']
    wind_direction = data['wind']['deg']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    dew_point = data['main'].get('dew_point', 'N/A')  # Устанавливаем значение по умолчанию 'N/A', если ключ отсутствует

    # Выведите информацию о погоде
    print(f"Погода в {city}: {temperature_celsius:.2f}°C")
    print(f"Скорость ветра: {wind_speed} m/s, Направление ветра: {wind_direction}°")
    print(f"Давление: {pressure}hPa")
    print(f"Влажность: {humidity}%")
else:
    print("Не удалось получить информацию о погоде.")

table1 = f"Погода в {city}: {temperature_celsius:.2f}°C\n"\
    f"Скорость ветра: {wind_speed} m/s, Направление ветра: {wind_direction}°\n"\
    f"Давление: {pressure}hPa\n"\
    f"Влажность: {humidity}%\n"


#Курс йены
url2 = 'https://www.banki.ru/products/currency/cny/'  # сохраним наш URL в переменную
source2 = requests.get(url2)  # отправим GET()-запрос на сайт и сохраним полученное в переменную source
soup2 = BeautifulSoup(source2.text, "html.parser")
table2 = soup2.find('div', {'class': 'Text__sc-j452t5-0 bCCQWi'})

if table2 is not None:
    print("Курс йены:", table2.text)
else:
    print("Информация о Курсе йены не найдена.")


#Курс доллара
url3 = 'https://www.banki.ru/products/currency/usd/'  # сохраним наш URL в переменную
source3 = requests.get(url3)  # отправим GET()-запрос на сайт и сохраним полученное в переменную source
soup3 = BeautifulSoup(source3.text, "html.parser")
table3 = soup3.find('div', {'class': 'Text__sc-j452t5-0 bCCQWi'})

if table3 is not None:
    print("Курс USD:", table3.text)
else:
    print("Информация о Курсе USD не найдена.")



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "<b>Список команд:</b>""\n"
                                      "<b>/time: Показывает текущую дату и время </b>""\n"
                                      "<b>/pogoda: Показывает текущую погоду </b>""\n"
                                      "<b>/USD: Показывает курс ЦБ РФ Доллара </b>""\n"
                                      "<b>/CNY: Показывает курс ЦБ РФ Юаня </b>"
                     , parse_mode='html')


@bot.message_handler(commands=['time'])
def time(message):
    if datetime.datetime.now() is not None:
        bot.send_message(message.chat.id, "Текущее Дата и Время:", parse_mode='html')
        bot.send_message(message.chat.id, datetime.datetime.now() , parse_mode='html')
    else:
        print("Информация о текущей дате и времени не найдена.")

@bot.message_handler(commands=['pogoda'])
def pogoda(message):
    bot.send_message(message.chat.id, table1, parse_mode='html')

@bot.message_handler(commands=['CNY'])
def cny(message):
    bot.send_message(message.chat.id, table2.text, parse_mode='html')

@bot.message_handler(commands=['USD'])
def cny(message):
    bot.send_message(message.chat.id, table3.text, parse_mode='html')


bot.polling(none_stop=True)