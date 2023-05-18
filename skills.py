import os
import webbrowser
import sys
import subprocess

import voice

try:
    import requests
except:
    pass


def browser():
    '''Открывает браузер '''

    webbrowser.open('https://www.youtube.com', new=2)


def game():
    '''Нужно разместить путь к exe файлу любого приложения'''
    try:
        subprocess.Popen('...')
    except:
        voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
    # os.system('shutdown \s')
    print('пк выключен')


def weather():
    try:
        params = {'q': 'London', 'units': 'metric', 'lang': 'ru', 'appid': 'ключ к API'}
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")

    except:
        voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    '''Отключние бота'''
    sys.exit()


def passive():
    '''Функция заглушка при простом диалоге с ботом'''
    pass
