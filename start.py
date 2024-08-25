import fnmatch
import pygame
from pygame import *
import sys
import parsing
import random
import time
import os
#функция баннера
def show_banner(screen, status):
    banner_font = pygame.font.SysFont('Verdana', 24)
    if status == "Небольшой дождь":
        phrases = ["Облачно, возможны осадки в виде фрика...","Не забудь свой зонтик!", "Дождик небольшой, а может и большой","Не промочи ноги бро","Возьми с собой зонтик!"]
        banner_text = banner_font.render(random.choice(phrases), True, (255, 255, 255))
    elif status == "Ясно":
        phrases = ["Не забудь нанести spf","Какое прекрасное солнышко!","Отличная погода для прогулки!","Самое время для маленького путешествия","Защищайся от солнца сегодня, оно очень яркое!", "Какое прекрасное солнышко!", "Нанеси СПФ,а то в старости будешь как изюм"]
        banner_text = banner_font.render(random.choice(phrases), True, (255, 255, 255))
    elif status == "Пасмурно":
        phrases = ["Послушай музыку в наушниках","Самостоятельно сделай день ярче!","Одевайся теплее сегодня","Проведите время в уюте дома"]
        banner_text = banner_font.render(random.choice(phrases), True, (255, 255, 255))
    elif status == "Облачно":
        phrases = [ "Сегодня облачно, отличный день для прогулки", "Сегодня обещают прекрасную погоду","Отличная погода для пробежки!", "Облачная погода идеальна для садоводства"]
        banner_text = banner_font.render(random.choice(phrases), True, (255, 255, 255))
    elif status == "Малооблачно" or status == "Переменная облачность":
        phrases = ["Иногда стоит насладиться маленькими облаками", "Отличная погода для занятия спортом на улице!", "Сегодня не так много облаков - нанеси свой spf","Отличная погода для пробежки!"]
        banner_text = banner_font.render(random.choice(phrases), True, (255, 255, 255))
    elif status == "Дымка":
        phrases = ["Туманно однако, но это ненадолго!","Примерно такая погода в фильме 'Сумерки'","Сегодня лучше остаться дома!"]
        banner_text = banner_font.render(random.choice(phrases), True, (255, 255, 255))
    elif status == "Снег":
        phrases = ["Зимняя сказка!", "Отличная погода, чтобы остаться дома", "Отличная погода, чтобы поиграть в снежки","Сегодня можно ловить снежинки языком!","Холодная зима, не так ли?"]
        banner_text = banner_font.render(random.choice(phrases), True, (255, 255, 255))
    else:
        banner_text = banner_font.render("Пары? Нет, не слышали...", True, (255, 255, 255))
    banner_rect = banner_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    pygame.draw.rect(screen, (color_4), (120, 195, 640, 110), 0, 25)
    pygame.draw.rect(screen, (color_6), (130, 205, 620, 90), 0, 15)
    screen.blit(banner_text, banner_rect.topleft)

    close_button_font = pygame.font.SysFont('Arial', 20, bold=True)
    close_button_text = close_button_font.render('X', True, (255,0,0))
    close_button_rect = pygame.Rect(729, 210, 20, 20)  # Сделаем close_button_rect объектом Rect
    pygame.draw.rect(screen, (color_6), close_button_rect, 0, 10)
    screen.blit(close_button_text, close_button_rect)

    return close_button_rect

clock = pygame.time.Clock()
pygame.init()
size = [880, 500]
change_rect = 1
change_rect_sec  = 0
color_1 = [163,190,255]#фон
color_2 = [21,52,102] #большие квадраты
color_3 = [98,10,255] #дни и время
color_4 = [52, 21, 102] #большой центральный 52, 21, 102
color_5 = [122,51,255] #цвет выбранной кнопки
color_6 = [120, 47, 194] #квадраты параметров 120, 47, 194
alpha_value = 0

"""музыка"""
pygame.mixer.music.load("music/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
ef_1 = pygame.mixer.Sound('music/push.mp3')
sound = True
label_emoji = pygame.font.Font('font/seguiemj.ttf', 20)
menu_set_music_on_label = label_emoji.render("🔊", False, "White", color_3)
menu_set_music_off_label = label_emoji.render("🔈  ", False, "White", color_3)


"""мемы"""
#количество папок
def direct(path):
    entries = os.listdir(path)
    directories = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
    return directories

#количество пнг файлов
def direct_2(path):
    entries = os.listdir(path)
    png_files = [entry for entry in entries if fnmatch.fnmatch(entry, '*.png') and os.path.isfile(os.path.join(path, entry))]
    return png_files

mems = {}
path = direct("images")
for i in range(len(path)): #рэнж равен количеству папок с мемами
    mems[path[i]] = []
    for j in range(len(direct_2(f"images/{path[i]}"))): #рэнж равен количеству мемов в папке
        mems[path[i]].append(pygame.image.load(f"images/{path[i]}/{direct_2(f'images/{path[i]}')[j]}"))
print(mems)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Погода")
screen.fill(color_1)


font_1 = pygame.font.SysFont('Verdana', 18, bold=True)
temp_font = pygame.font.SysFont('Impact', 90)
prec_font = pygame.font.SysFont('Impact', 28)
phrase_font = pygame.font.SysFont('font/Comic Sans MS.ttf', 30)

change_day = True
change_time = True
change_for_mem = True

parsind_data = parsing.parsing_weather_days()
weather_week = parsing.parsing_weather_week()
time_on_day = parsind_data[0]
temperature_on_day = parsind_data[1]
precipitation_on_day = parsind_data[2]
pressure_on_day = parsind_data[3]
humidity_on_day = parsind_data[4]
wind_with_spaces = parsind_data[5]
status_on_day = parsind_data[6]

change_rect_sec = int(((min([0, 3, 6, 9, 12, 15, 18, 21], key=lambda x: abs(x - int(time.strftime("%H", time.localtime())))))/3)+1) #определяем текущее время и ближайшее время в погоде

# показываем баннер
close_button_rect = show_banner(screen, status_on_day[0][change_rect_sec])
pygame.display.update()

banner_shown = True
while banner_shown:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if close_button_rect.collidepoint(event.pos):
                banner_shown = False


while True:
    screen.fill(color_1)
    # це дизайн. биг рект
    pygame.draw.rect(screen, color_2, (20, 20, 220, 460), 0,24)
    pygame.draw.rect(screen, color_2, (260, 20, 600, 65),0,16)
    pygame.draw.rect(screen, color_4, (260, 105, 350, 375),0,16)

    # це дизайн. дэйс он вик
    y_rect = 30
    for i in range(7):
        if change_rect == i+1:
            pygame.draw.rect(screen, color_5, (30, y_rect, 200, 54), 0, 14)
        else:
            pygame.draw.rect(screen, color_3, (30, y_rect, 200, 54), 0, 14)
        text1 = font_1.render(weather_week[i].split()[0], True, (238, 238, 238))
        text2 = font_1.render(weather_week[i].split()[1]+' '+ weather_week[i].split()[2], True, (238, 238, 238))
        screen.blit(text1, (42, y_rect + 3))
        screen.blit(text2, (42, y_rect+26))
        y_rect = y_rect + 64

    x_rect = 270
    for i in range(8):
        if change_rect_sec == i + 1:
            pygame.draw.rect(screen, color_5, (x_rect - 2, 28, 66, 48), 0, 6)
        else:
            pygame.draw.rect(screen, color_3, (x_rect - 2, 28, 66, 48), 0, 6)
        text3 = pygame.font.SysFont('Verdana', 17, bold=True).render(time_on_day[i], True, (238, 238, 238))
        screen.blit(text3, (x_rect+2, 40))
        x_rect = x_rect + 74

    #(x,y, ширина, высота)
    pygame.draw.rect(screen, color_6, (270, 115, 150, 150), 0, 6) #температура
    pygame.draw.rect(screen, color_6, (270, 275, 150, 95), 0, 6)  # ветер
    pygame.draw.rect(screen, color_6, (430, 115, 170, 95), 0, 6)  # статус
    pygame.draw.rect(screen, color_6, (430, 220, 170, 130), 0, 6)  # осадки
    pygame.draw.rect(screen, color_6, (270, 380, 150, 90), 0, 6)  # влажность
    pygame.draw.rect(screen, color_6, (430, 360, 170, 110), 0, 6)  # давление

    try:
        if change_for_mem == True and (status_words[0] == 'Пасмурно' or status_words[1]=='облачность'):
            change_for_mem = False
            index_mem = random.randint(0, len(mems["Pasmurno"])-1)
            # print(index_mem)
        if status_words[0] == "Пасмурно" or status_words[1]=="облачность":
            screen.blit(mems["Pasmurno"][index_mem], (620, 110))
    except:
        pass

    try:
        if change_for_mem == True and (status_words[0] == 'Дождь' or status_words[1]=='дождь'):
            change_for_mem = False
            index_mem = random.randint(0, len(mems["Rain"])-1)
            # print(index_mem)
        if (status_words[0] == "Дождь" or status_words[1]=="дождь"):
            screen.blit(mems["Rain"][index_mem], (620, 110))
    except:
        pass

    try:
        if change_for_mem == True and status_words[0] == 'Ясно':
            change_for_mem = False
            index_mem = random.randint(0, len(mems["Yasno"])-1)
        if status_words[0] == "Ясно":
            screen.blit(mems["Yasno"][index_mem], (620, 110))
    except:
        pass

    try:
        if change_for_mem == True and status_words[0] == 'Дымка':
            change_for_mem = False
            index_mem = random.randint(0, len(mems["Fog"])-1)
            # print(index_mem)
        if status_words[0] == "Дымка":
            screen.blit(mems["Fog"][index_mem], (620, 110))
    except:
        pass

    try:
        if change_for_mem == True and status_words[0] == 'Снег':
            change_for_mem = False
            index_mem = random.randint(0, len(mems["Snow"])-1)
            # print(index_mem)
        if status_words[0] == "Снег":
            screen.blit(mems["Snow"][index_mem], (620, 110))
    except:
        pass

    try:
        if change_for_mem == True and (status_words[0] == 'Облачно'or status_words[0]=='Малооблачно'):
            change_for_mem = False
            index_mem = random.randint(0, len(mems["Oblachno"])-1)
            # print(index_mem)
        if (status_words[0] == "Облачно" or status_words[0]=="Малооблачно"):
            screen.blit(mems["Oblachno"][index_mem], (620, 110))
    except:
        pass

    if change_day == True and change_time == True:
        index_day = change_rect
        index_time = change_rect_sec

        #отрисовка статуса
        status_words = status_on_day[index_day - 1][index_time - 1].replace('Ясная погода', 'Ясно').split()
        x, y = 440, 120
        for word in status_words:
            text_word = pygame.font.SysFont('Impact', 26).render(word, True, (238, 238, 238))
            screen.blit(text_word, (x, y))
            y += text_word.get_height() + 5
        current_status = status_words[0]

        #отрисовка температуры
        phrase_temperature = phrase_font.render('Температура:', True, (238, 238, 238))
        screen.blit(phrase_temperature, (280, 125))
        text_temperature = temp_font.render(temperature_on_day[index_day-1][index_time-1], True, (238, 238, 238))
        screen.blit(text_temperature, (273, 150))

        #отрисовка осадков
        phrase_precipitation = 'Вероятность выпадения осадков:'
        num = str(precipitation_on_day[index_day - 1][index_time - 1])
        # Начальные координаты для вывода слов
        x, y = 440, 230
        words = phrase_precipitation.split()
        # Вывод каждого слова по отдельности
        for word in words:
            text_word = phrase_font.render(word, True, (238, 238, 238))
            screen.blit(text_word, (x, y))
            y += text_word.get_height() + 5 # Добавляем небольшой отступ между словами
        text_num = prec_font.render(num, True, (238, 238, 238))
        screen.blit(text_num, (x, 305))

        #отрисовка давления
        phrase_pressure = phrase_font.render('Давление:', True, (238, 238, 238))
        screen.blit(phrase_pressure, (440, 370))
        words = f'{pressure_on_day[index_day-1][index_time-1]} рт.ст.'.split()
        x, y = 440, 395
        # Вывод каждого слова по отдельности
        for word in words:
            text_word = prec_font.render(word, True, (238, 238, 238))
            screen.blit(text_word, (x, y))
            y += text_word.get_height() - 5 # Добавляем небольшой отступ между словами

        #отрисовка влажности воздуха
        phrase_humidity = 'Влажность воздуха:'
        num = str(humidity_on_day[index_day - 1][index_time - 1])
        x, y = 280, 390
        words = phrase_humidity.split()
        # Вывод каждого слова по отдельности
        for word in words:
            text_word = phrase_font.render(word, True, (238, 238, 238))
            screen.blit(text_word, (x, y))
            y += text_word.get_height() + 2  # Добавляем небольшой отступ между словами
        text_num = prec_font.render(num, True, (238, 238, 238))
        screen.blit(text_num, (280, y))

        #отрисовка ветра
        phrase_wind = phrase_font.render('Ветер:', True, (238, 238, 238))
        screen.blit(phrase_wind, (280, 285))
        parts = f'{wind_with_spaces[index_day - 1][index_time - 1]}  м/c'.split()
        x, y = 280, 310
        # Вывод каждой части по отдельности
        for part in parts:
            if part == 'Ветер:':
                text_part = prec_font.render(part, True, (238, 238, 238))
                screen.blit(text_part, (x, y))
                y += text_part.get_width() + 1  # Увеличение координаты y для следующей части
            else:
                text_part = prec_font.render(part, True, (238, 238, 238))
                screen.blit(text_part, (x, y))
                x += text_part.get_width() + 3  # Добавляем небольшой отступ между словами

    if sound == True:
        menu_set_music_on_label_rect = menu_set_music_on_label.get_rect()
        menu_set_music_on_label_rect.center = (860, 480)
        screen.blit(menu_set_music_on_label, menu_set_music_on_label_rect)
    if sound == False:
        menu_set_music_off_label_rect = menu_set_music_off_label.get_rect()
        menu_set_music_off_label_rect.center = (860, 480)
        screen.blit(menu_set_music_off_label, menu_set_music_off_label_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(7):
                if 30 < event.pos[0] < 230 and 30 + 64*i < event.pos[1] < 84 + 64*i:
                    change_rect = i+1
                    ef_1.play()
                    change_day = True

        if event.type == pygame.MOUSEBUTTONDOWN and change_day == True:
            for i in range(8):
                if 270 + 74*i < event.pos[0] < 334+74*i and 28 < event.pos[1] < 76:
                    change_rect_sec = i+1
                    ef_1.play()
                    change_for_mem = True
                    change_time = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 845 < event.pos[0] < 875 and 465 < event.pos[1] < 495:
                if sound == True:
                    pygame.mixer.music.pause()
                    sound = False
                elif sound == False:
                    pygame.mixer.music.unpause()
                    sound = True
        if event.type == pygame.MOUSEMOTION:
            coor = event.pos

    pygame.display.update()
    clock.tick(60)