from requests import get
from lxml.etree import HTML
from datetime import datetime, timedelta
import json
laikas_end: datetime = datetime.now() + timedelta(seconds=6)
listas1 =[]

def check_time(a):
    return  datetime.now() < laikas_end

def duino ( f1 : str):

    listas = []
    response = get("https://www.duino.lt/64-valdikliai")
    text = response.text
    tree = HTML(text)

    products = tree.xpath("//div[contains(@class, 'right-block')]")
    listas = [
        {'Produktas : ': product.xpath(".//a[contains(@class, 'product-name')]/text()")[0],
         'Kaina : ': product.xpath(".//span[contains(@class, 'price product-price')]/text()")[0].strip().replace("€",                                                                                                            "")
         }
        for product in products
            ]

    if f1 == ".txt":
        for i in listas:
            open("Duino.txt", "a").write(str(i) + "\n")
            open("Duino.txt", "a").close()
    elif f1 == ".json":
        for i in listas:
            print("json")
            json_object = json.dumps(i, indent=2)
            with open("Duino.json", "a") as irasymas_f:
                irasymas_f.write(json_object)
                irasymas_f.close()
    else :
        print("Neteisingai pasirinktas formatas")
        print("Galimi formatai: .json arba .txt")


def skonis(f : str):
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

    if f == ".txt":
        for i in listas:
            open(f"Skonis_ir_Kvapas.txt", "a").write(str(i) + "\n")
            open(f"Skonis_ir_Kvapas.txt", "a").close()
    elif f == ".json":
        for i in listas:
            print("json")
            json_object = json.dumps(i, indent=2)
            with open("Skonis_ir_Kvapas.json", "a") as irasymas_f:
                irasymas_f.write(json_object)
                irasymas_f.close()
    else:
        print("Neteisingai pasirinktas formatas")
        print("Galimi formatai: .json arba .txt")

def crowl(puslapis : int, formatas : str):
    match puslapis:
        case 1:
            print(" 1 pasirinkta")
            duino(formatas)
        case 2:
            print("2 pasirinkta")
            skonis(formatas)
        case _:
            print("Galimas pasirinkimas int 1 arba 2")
            print(" 1 - Duino.lt ")
            print(" 2 - Skonis ir Kvapas.lt ")
