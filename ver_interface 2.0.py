import random
import sqlite3
import time
from sqlite3 import Error
from tkinter import *

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


def user_name_check(user_name):
    if user_name == "":
        return 2

    symbols = '! " # $ % & ’ ( ) * + , - . / : ; < = > ? @ [ ] ^ _ ` { | } ~ .'
    for s in user_name:
        if s in symbols:
            return 1
    else:
        return 0


def game():
    window = Tk()
    window.title("Привет, я игра 'Угадай персонажа'.")
    # window.state('zoomed')
    # window.attributes("-fullscreen", True)

    f1 = Frame(window)
    f2 = Frame(window)
    f3 = Frame(window)
    f4 = Frame(window)

    for frame in (f1, f2, f3, f4):
        frame.grid(row=0, column=0, sticky="news")

    uncorrect = Label(f1)
    uncorrect.pack(side='bottom')

    exit_button = Button(
        f2,
        text="Выйти из игры",
        command=window.destroy
    )
    exit_button.pack(side="top")

    exit_button_2 = Button(
        f3,
        text="Выйти из игры",
        command=window.destroy
    )
    exit_button_2.pack(side="bottom")

    user_entry = Entry(f2)
    user_entry.pack(side="bottom")

    def raise_frame(frame):
        frame.tkraise()

    def user_inpt(event):
        nonlocal user_name
        user_name = name_input.get()
        result = user_name_check(user_name)
        if result == 2:
            uncorrect.config(text="Вы не ввели имя.")

        if result == 1:
            uncorrect.config(
                text="В имени найдены запрещенные символы или пробел.\nИмя должно содержать только буквы английского,"
                     "\nрусского алфавитов и цифры, введите имя еще раз.")

        if result == 0:
            uncorrect.config(text="")

            welcome_txt = Label(
                f2,
                text=f"{user_name}, игра стартовала!."
            )
            welcome_txt.pack()

            raise_frame(f2)

            playing()

            # welcome_txt.destroy()

    name = Label(f1, text="Введите имя:  ")
    name.pack(side=TOP)

    user_name = None

    name_input = Entry(f1)
    name_input.pack(side=TOP)

    unused_character_name = []
    unused_character_name.extend(lst_character_name_all)
    unused_character_description = []
    unused_character_description.extend(lst_character_description_all)
    unused_character_audio = []
    unused_character_audio.extend(lst_character_audio_all)

    def check_lst():
        if len(unused_character_name) == 0:
            cancel_txt = Label(
                f3,
                text='Персонажи закончились, хотите попробовать снова?'
            )
            cancel_txt.pack()

            def again():
                window.destroy()
                game()

            quit_or_again = Button(
                f3,
                text="Попробовать снова",
                command=again
            )
            quit_or_again.pack()

            window.update()

            return 1
        return 0

    def playing():
        window.update()

        check = check_lst()
        if check == 1:
            raise_frame(f3)

        random_character = random.choice(
            range(0, len(unused_character_name)))  # случайный индекс неиспользованного персонажа.

        charact_description = unused_character_description[
            random_character]  # список описаний персонажа, индекс которого выбран строчкой выше.

        character_description = charact_description[random.choice(range(0, len(charact_description)))]

        character_description_label = Label(
            f2,
            text=(character_description)
        )
        character_description_label.pack()

        winsound.PlaySound(unused_character_audio[random_character], winsound.SND_FILENAME | winsound.SND_ASYNC)

        win = Label(
            f2,
            text=""
        )
        win.pack(side="bottom")

        def check():
            winsound.PlaySound(None, winsound.SND_PURGE)

            x = user_entry.get()
            if x == unused_character_name[random_character]:
                win.config(text="")
                win.config(text=f"{user_name}, поздравляю вы угадали персонажа!")
                window.update()

                time.sleep(1)

                unused_character_name.pop(random_character)
                unused_character_description.pop(random_character)
                unused_character_audio.pop(random_character)

                win.destroy()
                player_option_but.destroy()
                character_description_label.config(text="")

                playing()

            else:
                win.config(text="")
                win.config(text="К сожалению вы не угадали.")

                window.update()

                time.sleep(2)

                win.config(text="")
                window.update()

        player_option_but = Button(
            f2,
            text="Ответить",
            command=check
        )
        player_option_but.pack(side='bottom')

        window.update()

    but = Button(f1, text="Играть")
    but.bind('<Button-1>', user_inpt)
    but.pack(expand=True, ipadx=10, ipady=1)

    raise_frame(f1)

    window.mainloop()


game()
