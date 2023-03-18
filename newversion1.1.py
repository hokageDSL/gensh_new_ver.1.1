import random

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


def game(lst_character_name, lst_character_description_all):
    user_name = input("Привет, я игра 'Угадай персонажа', введите имя игрока: ")

    print(f"{user_name}, чтобы начать игру, напиши - что-нибудь, чтобы завершить игру напиши - 'Стоп'.")

    game_status = input().capitalize()

    unused_character_name = lst_character_name  # не использованные персонажи.

    unused_character_description = lst_character_description_all

    while game_status != "Стоп":

        random_character = random.choice(
            range(0, len(unused_character_name)))  # случайный индекс не использованного персонажа.

        charact_description = unused_character_description[
            random_character]  # список описаний персонажа, индекс которого выбран строчкой выше.

        character_description = charact_description[random.choice(range(0, len(charact_description)))]

        print(character_description)

        player_option = (input("Ответ: "))
        if player_option == unused_character_name[random_character]:
            print(f"{user_name}, поздравляю вы угадали персонажа!\nСтоп - завершить игру.")
            game_status = input("Идем дальше? ").capitalize()

        else:
            print("К сожалению вы не угадали, Стоп - завершить игру.")
            game_status = input("Идем дальше? ").capitalize()

        unused_character_name.pop(random_character)
        unused_character_description.pop(random_character)


game(lst_character_name_all, lst_character_description_all)

print("Вы вышли из игры.")