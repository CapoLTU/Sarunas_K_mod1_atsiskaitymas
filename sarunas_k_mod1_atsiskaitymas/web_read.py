from requests import get
from lxml.etree import HTML
from datetime import datetime, timedelta
laikas_end: datetime = datetime.now() + timedelta(seconds=6)
listas1 =[]

def check_time(a):
    return  datetime.now() < laikas_end

def duino (laikas : int = 1):
    laikas_end: datetime = datetime.now() + timedelta(seconds=laikas)
    listas = []
    response = get("https://www.duino.lt/64-valdikliai")
    text = response.text
    tree = HTML(text)

    products = tree.xpath("//div[contains(@class, 'right-block')]")
    listas = [
        {'Produktas : ': product.xpath(".//a[contains(@class, 'product-name')]/text()")[0],
         'Kaina : ': product.xpath(".//span[contains(@class, 'price product-price')]/text()")[0].strip().replace("€",
                                                                                                                 "")
         }
        for product in products
    ]
    for i in listas:
        if check_time(laikas_end) == True :
            open("Duino.txt", "a").write(str(i) + "\n")
            open("Duino.txt", "a").close()
        else :
            print("END TIME")
            break
    return listas
listas1 = duino()
print(listas1)

def skonis():
    listas = []
    response = get("https://www.skonis-kvapas.lt/kava")
    text = response.text
    tree = HTML(text)

    products = tree.xpath("//div[contains(@class, 'products__item  ')]")
    listas = [
        {'Produktas : ': product.xpath(".//h2[contains(@class, 'products__item-title')]/text()")[0].strip().replace("\n", ""),
         'Kaina : ': product.xpath(".//div[contains(@class, 'products__item-price')]/ins/text()")[0].strip().replace("\xa0", "").replace("€","")
         }
        for product in products
    ]
    for i in listas:
            open("Skonis_ir_Kvapas.txt", "a").write(str(i) + "\n")
            open("Skonis_ir_Kvapas.txt", "a").close()

    return listas

