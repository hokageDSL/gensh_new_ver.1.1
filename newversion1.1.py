import random
import sqlite3
from sqlite3 import Error

import winsound


def sql_connection():
    try:
        con = sqlite3.connect('base_charapters.db')
        return con
    except Error:
        print(Error)


con = sql_connection()

ganyu = [
    "Секретарь, который ответственен за каждое постановление и решение Цисин в Ли Юэ.",
    "Трудолюбивая и ответственная девушка, которая славится своим трудолюбием и усердием, \nа также предпочитает плотно поесть.",
    "Главный секретарь павильона Лунного моря.",
    "В ее жилах течет кровь мифического зверя цилиня.",
]

hutao = [
    "Хозяйка ритуального бюро «Ваншэн» в семьдесят седьмом поколении.",
    "Небольшая девушка с бледной кожей и длинными каштановыми волосами, \nплавно переходящими в алый цвет и собранными в два низких хвоста.",
]

ayaka = [
    "Дочь клана Камисато комиссии Ясиро.",
    "Благородна, изящна, мудра и сильна. Всегда честна и учтива. \nОбожаемая народом Инадзумы, она заслужила прозвище «Сирасаги Химэгими».",
]

lst_character_description_all = [ganyu, hutao, ayaka]
lst_character_name_all = ["Гань Юй", "Ху Тао", "Аяка"]
lst_character_audio_all = ["audio\\ganyu.wav", "audio\\hutao.wav", "audio\\ayaka.wav"]


def game():
    print("Привет, я игра 'Угадай персонажа'.")
    def user_name_check():
        while True:
            symbols = (' ! " # $ % & ’ ( ) * + , - . / : ; < = > ? @ [  ] ^ _ ` { | } ~. ')
            user_name_f = input("Введите имя игрока: ").capitalize()
            result = -1
            for i in user_name_f:
                result += symbols.find(i)
            if result > -1:
                print(
                    "В имени найдены запрещенные символы.\nИмя должно содержать только буквы английского/русского алфавитов и цифры, введите имя еще раз.")
                continue
            break
        return user_name_f

    user_name = user_name_check()

    print(f"{user_name}, чтобы начать игру, напиши - что-нибудь, чтобы завершить игру напиши - 'Стоп'.")

    game_status = input().capitalize()

    unused_character_name = []
    unused_character_name.extend(lst_character_name_all)
    unused_character_description = []
    unused_character_description.extend(lst_character_description_all)
    unused_character_audio = []
    unused_character_audio.extend(lst_character_audio_all)

    while game_status != "Стоп":
        if len(unused_character_name) == 0:
            if input('Персонажи закончились, если хотите попробовать снова, ответьте: "Да" ').capitalize() == 'Да':
                game()
            break

        random_character = random.choice(
            range(0, len(unused_character_name)))  # случайный индекс неиспользованного персонажа.

        charact_description = unused_character_description[
            random_character]  # список описаний персонажа, индекс которого выбран строчкой выше.

        character_description = charact_description[random.choice(range(0, len(charact_description)))]

        print(character_description)
        winsound.PlaySound(unused_character_audio[random_character], winsound.SND_FILENAME | winsound.SND_ASYNC)

        player_option = (input("Ответ: ")).title()
        if player_option == unused_character_name[random_character]:
            winsound.PlaySound(None, winsound.SND_PURGE)
            print(f"{user_name}, поздравляю вы угадали персонажа!\nСтоп - завершить игру.")
            game_status = input("Идем дальше? ").capitalize()

        else:
            print("К сожалению вы не угадали, Стоп - завершить игру.")
            winsound.PlaySound(None, winsound.SND_PURGE)
            game_status = input("Идем дальше? ").capitalize()

        unused_character_name.pop(random_character)
        unused_character_description.pop(random_character)
        unused_character_audio.pop(random_character)


game()

print("Вы вышли из игры.")
