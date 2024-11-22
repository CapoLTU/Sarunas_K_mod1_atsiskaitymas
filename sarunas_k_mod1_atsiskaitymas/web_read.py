from requests import get
from lxml.etree import HTML

listas1 =[]
def duino ():
    listas = []
    response = get("https://www.duino.lt/64-valdikliai")
    text = response.text
    tree = HTML(text)

    products = tree.xpath("//div[contains(@class, 'right-block')]")
    for product in products :
        prod = product.xpath(".//a[contains(@class, 'product-name')]/text()")
        listas.append(prod)
    return listas
listas1 = duino()
print(listas1)
