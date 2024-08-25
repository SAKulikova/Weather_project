import requests
from bs4 import BeautifulSoup
import re
url = f'https://www.meteoservice.ru/weather/week/kaliningrad#24052024'

def parsing_weather_week():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    days_on_week = [tag.get_text(strip=True) for tag in soup.find_all('span', class_='show-for-medium')]
    return days_on_week
def parsing_weather_days():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    #Описание погоды ✓✓
    status_on_day = [tag.get_text(strip=True) for tag in soup.find_all('div', class_="value show-for-medium show-for-advanced-only")]
    status_on_day = [status.split(',')[0] for status in status_on_day]
    status_on_day_new = [status_on_day[i:i + 8] for i in range(0, len(status_on_day), 8)]

    #Температура ✓✓
    temperature_on_day = [tag.get_text(strip=True) for tag in soup.find_all('tr', class_='temperature')]
    temperature_on_day_1 = [[0],[0],[0],[0],[0],[0],[0]]
    for i in range(7):
        temperature_on_day_1[i] = temperature_on_day[i].split()[1][7:-1].split('°')

    #Время ✓✓
    time_on_day = ["00:00", "03:00", "06:00", "09:00", "12:00", "15:00", "18:00", "21:00"]

    #осадки ✓✓
    precipitation_on_day = [tag.get_text(strip=True) for tag in soup.find_all('tr', class_='precipitation')]
    precipitation_on_day_cleaned = []
    for entry in precipitation_on_day:
        # Удаляем все вхождения вида "opacityX,X мм" или "opacityX мм"
        cleaned_entry = re.sub(r'\d+,\d+ мм|\d+ мм', '', entry)
        # Оставляем только проценты вероятности осадков
        percentages = re.findall(r'\d+%', cleaned_entry)
        precipitation_on_day_cleaned.append(percentages)

    #давление ✓✓
    pressure_on_day = [tag.get_text(strip=True) for tag in soup.find_all('tr', class_='pressure advanced')]
    pressure_on_day_1=[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    for i in range(0,13, 2):
        pressure_on_day_1[i] = pressure_on_day[i][8:].split('рт.ст.')[:-1]
    pressure_on_day_2 = pressure_on_day_1[::2]

    # влажность воздуха в течение дня ✓✓
    humidity_on_day = [tag.get_text(strip=True) for tag in soup.find_all('tr', class_='humidity advanced')]
    humidity_on_day_cleaned = []
    for entry in humidity_on_day:
        # Извлекаем проценты влажности
        percentages = re.findall(r'\d+%', entry)
        humidity_on_day_cleaned.append(percentages)

    #ветер ✓✓
    wind_on_day = [tag.get_text(strip=True) for tag in soup.find_all('tr', class_='wind')]
    wind_on_day_1 = [[0], [0], [0], [0], [0], [0], [0]]
    for i in range(7):
        wind_on_day_1[i] = wind_on_day[i][5:].split('м/с')[:-1]
        # Преобразование строк с ветром, добавляя пробелы между буквами и цифрами
    wind_with_spaces = []
    for day in wind_on_day_1:
        wind_day_with_spaces = [re.sub(r'([А-Яа-я])([0-9])', r'\1 \2', wind.strip()) for wind in day]
        wind_with_spaces.append(wind_day_with_spaces)

    return time_on_day, temperature_on_day_1, precipitation_on_day_cleaned, pressure_on_day_2, humidity_on_day_cleaned, wind_with_spaces, status_on_day_new
parsing_weather_days()