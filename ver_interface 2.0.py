import sqlite3
from sqlite3 import Error

from tkinter import *


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
    symbols = '! " # $ % & ’ ( ) * + , - . / : ; < = > ? @ [ ] ^ _ ` { | } ~ .'
    for s in user_name:
        if s in symbols:
            return 1
    else:
        return 0


def game():
    def raise_frame(frame):
        frame.tkraise()

    def user_inpt(event):
        user_name = name_input.get()
        if user_name_check(user_name) == 1:
            Label(f1,
                  text="В имени найдены запрещенные символы.\nИмя должно содержать только буквы английского/русского "
                       "алфавитов и цифры, введите имя еще раз.").pack()
            game()

    window = Tk()
    window.title("Привет, я игра 'Угадай персонажа'.")
    # window.geometry('1280x720')

    f1 = Frame(window)
    f2 = Frame(window)
    f3 = Frame(window)
    f4 = Frame(window)

    for frame in (f1, f2, f3, f4):
        frame.grid(row=0, column=0, sticky='news')

    name = Label(
        f1,
        text="Введите имя:  "
    )
    name.pack()
    user_name = None
    name_input = Entry(f1)
    name_input.pack()

    but = Button(f1, text="Играть")
    but.bind('<Button-1>', user_inpt)
    but.pack()

    welcome_txt = Label(
        f2,
        text=f"{user_name}, чтобы начать игру, напиши - что-нибудь, чтобы завершить игру напиши - 'Стоп'."
    )
    welcome_txt.pack()

    raise_frame(f1)

    window.mainloop()


game()

print("Вы вышли из игры.")
