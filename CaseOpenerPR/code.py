import random

CASES = {
    "wildfire" : {
        "Синий" : ['Tec-9 | Джамбия', 'USP-S | Проводник', 'SSG 08 | Некромант', 'Dual Berettas | Картель', 'MAC-10 | Лазурный хищник', 'PP-Bizon | Океанская глубина'],
        "Фиолетовый" : ['MAG-7 | Преторианец', 'FAMAS | Валентность', 'Five-SeveN | Триумвират', 'Glock-18 | Королевский легион'],
        "Розовый" : ['Desert Eagle | Дракон-предводитель', 'Nova | Скоростной зверь', 'AWP | Элитное снаряжение'],
        "Красный" : ['AK-47 | Топливный инжектор', 'M4A4 | Звёздный крейсер'],
        },
    "Chroma 2" : {
        'Синий' : ['AK-47 | Элитное снаряжение', 'MP7 | Броня', 'Desert Eagle | Бронзовая декорация', 'P250 | Валентность', 'Sawed-Off | Оригами'],
        'Фиолетовый' : ['AWP | Бог червей', 'MAG-7 | Жар', 'CZ75-Auto | Поул-позиция', 'UMP-45 | Гран-При'],
        'Розовый' : ['Five-SeveN | Обезьяне дело', 'Galil AR | Эко', 'FAMAS | Джинн'],
        'Красный' : ['M4A1-S | Скоростной зверь', 'MAC-10 | Неоновый гонщик'],
    },
}
KNIVES = ['Керамбит', 'Складной нож', 'М9 Штык-нож', 'Штык-нож', 'Фальшион', 'Тычковые ножи', 'Нож Боуи']

WEAR = ['Закаленное в боях', 'Поношенное', 'После полевых испытаний', 'Немного поношенное', 'Прямо с завода']

BONUS_KEYS = dict(purple=1, pink=3, red=7)


def open_case(case):
    chance = random.randint(1, 100)
    for (rarity, skins), y in zip(list(case.items()), [25, 10, 5, 2]):
        if chance < y:
            continue
        track_chance = random.randint(1, 100)
        skin = random.choice(skins)
        wear = random.choice(WEAR)
        item = f"{skin} ({wear}) ({rarity} скин){' ' if track_chance <= 35 else ''}"
        return item, chance, BONUS_KEYS.get(rarity, 0)
    return random.choice(KNIVES), chance, 15


def case_run(keys):
    while keys:
        cs = input("Какой кейс откроем? ")
        try:
            case = CASES[cs.lower()]
        except KeyError:
            print ("Посмотри в список кейсов!")
            continue
        else:
            item, chance, bonus_keys = open_case(case)
            print(f"Ты выиграл {item}")
            print(f"С шансом {chance}")
            if bonus_keys:
                print(f"Супер! Нв {bonus_keys} ключей больше!")
            keys += bonus_keys - 1
            print(f"Ключей осталось: {keys}")
    else:
        print ("Ключи закончились")

def main():
    keys = 5
    while True:
        case_run(keys)

        cs = input("Сыграем еще? ")
        if cs.lower() in ('Да', 'да'):
            keys = int(input("На сколько ключей? "))
        else:
            break


if __name__ == '__main__':
    print ("Добро пожаловать в Case Opener v1.0!")
    print ()
    print ("Справка об игре: ")
    print ("Доступные кейсы: Wildfire и Chroma 2")
    print ("В начале игры у тебя есть 1 ключ")
    print ('Выбиваешь синий скин - не получаешь ключей в подарок!')
    print ("Выбиваешь фиолетовый скин - получаешь 1 ключ в подарок!")
    print ("Выбиваешь розовый скин - получаешь 3 ключа в подарок!")
    print ("Выбиваешь красный скин - получаешь 7 ключей в подарок!")
    print ("Выбиваешь нож - получаешь 15 ключей в подарок!")
    print ("Качество скина ни за что не отвечает")
    print ("Чтобы открыть кейс, напиши его название")
    print()


    main()