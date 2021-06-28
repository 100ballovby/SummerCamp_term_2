import pandas as pd


def parse_dominos(card):
    res = pd.DataFrame()  # таблица для результатов
    url = 'https://dominos.by/pizza/'
    pizza_link = url + card.get('data-code').lower()  # ссылка на пиццу
    pizza_name = card.find('div', {'class': 'product-card__title'}).text
    pizza_ingr = card.find('div', {'class': 'product-card__description'}).text
    pizza_img = card.find('img', {'class': 'product-card-media__element'}).get('src')
    pizza_price = card.find('p', {'class': 'product-card__modification-info-price'}).text
    print(pizza_link, pizza_name, pizza_ingr, pizza_img, pizza_price)

    res = res.append(
        pd.DataFrame(  # создаю таблицу на основе полученных данных
            [[pizza_link, pizza_name, pizza_ingr, pizza_price, pizza_img]],
            columns=['Ссылка', 'Название', 'Ингредиенты', 'Цена', 'картинка']),
        ignore_index=True
    )
    return res
