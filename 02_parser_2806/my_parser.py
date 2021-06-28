import pandas as pd


def parse_dominos(card):
    res = pd.DataFrame()  # таблица для результатов
    url = 'https://dominos.by/pizza/'
    pizza_link = url + card.get('data-code')  # ссылка на пиццу
    print(pizza_link,)
    '''
    res = res.append(
        pd.DataFrame(  # создаю таблицу на основе полученных данных
            [[]],
            columns=['Ссылка', 'Название', 'Ингридиенты', 'Цена', 'Масса', 'картинка']),
        ignore_index=True
    )'''
    return res
