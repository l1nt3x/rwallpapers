# Импорт необходимых библиотек
import requests
from copy import deepcopy
from random import choice


# Получить ссылку на обои
def get_wallpaper_path(apikey, categories=111, purity=100, atleast='1920x1080', ratios='16x9', sorting='date_added',
                       order='desc'):
    # Проверка на ключ api
    if not apikey:
        return 'No APIkey'
    # Первоначальный запрос
    req = f'https://wallhaven.cc/api/v1/search?apikey={apikey}&categories={categories}&purity={purity}&atleast={atleast}&ratios={ratios}&sorting={sorting}&order={order}'
    # Ответ
    resp = requests.get(req)
    # Ответ в json
    jresp = resp.json()
    # Вытаскиваем информацию об обоях из ответа
    wallpapers_jsons = deepcopy(jresp['data'])  # len(wallpapers_jsons) == 24 ## True
    # Выбираем рандомные обои из 24 возможных
    random_wallpaper_json = choice(wallpapers_jsons)
    # Получаем прямую ссылку на выбранные обои
    random_wallpaper_path = random_wallpaper_json['path']

    # Возвращаем полученную ссылку
    return random_wallpaper_path


# Получить навзание обоев
def get_wallpaper_alt(apikey, wallpaper_path):
    # Проверка на ключ api
    if not apikey:
        return 'No APIkey'
    # Получаем id из прямой ссылки
    wallpaper_id = wallpaper_path[wallpaper_path.rfind('wallhaven-') + 10:-4]
    # Первоначальный запрос
    req = f'https://wallhaven.cc/api/v1/w/{wallpaper_id}?apikey={apikey}'
    # Ответ
    resp = requests.get(req)
    # Ответ в json
    jresp = resp.json()
    # Получаем название обоев из категории, разрешения и названий тэгов
    wallpaper_alt = jresp['data']['category'] + '-' + jresp['data']['resolution']
    for i in range(len(jresp['data']['tags'])):
        wallpaper_alt += '-' + jresp['data']['tags'][i]['name']
    # Делаем первую букву заглавной
    wallpaper_alt = wallpaper_alt.capitalize()
    # Замена пробелов на дефисы
    wallpaper_alt = wallpaper_alt.replace(' ', '-')

    # Возвращаем название обоев
    return wallpaper_alt
