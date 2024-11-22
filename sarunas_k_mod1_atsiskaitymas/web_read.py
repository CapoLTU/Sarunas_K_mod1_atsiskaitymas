from requests import get
from lxml.etree import HTML
from datetime import datetime, timedelta
laikas_end: datetime = datetime.now() + timedelta(seconds=6)
listas1 =[]

def check_time(a):
    return  datetime.now() < laikas_end

def duino (laikas : int = 2):
    laikas_end: datetime = datetime.now() + timedelta(seconds=laikas)
    listas = []
    response = get("https://www.duino.lt/64-valdikliai")
    text = response.text
    tree = HTML(text)

    products = tree.xpath("//div[contains(@class, 'right-block')]")
    for product in products :
        if check_time(laikas_end) == True :
            prod = product.xpath(".//a[contains(@class, 'product-name')]/text()")
            listas.append(prod)
        else:
            print("END TIME")
            break
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





