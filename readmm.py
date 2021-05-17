from bs4 import BeautifulSoup
from product import Product
#https://pendlehillmeatmarket.com.au/product-category/fresh-meat/beef/?count=36&paged=
def processMM(file):
    wow = list()
    with open(file, 'r', encoding='utf8') as f:

        contents = f.read()
        soup = BeautifulSoup(contents, "html.parser")

        divs = soup.find_all("div", {"class": "product-desc"})
        for div in divs:
            #print(div)
            name = div.find("a", {"class": "product-name"}).get_text()
            url = div.find("a", {"class": "product-name"}).get('href')
            print(name)
            print(url)
            try:
                price = div.find("span", {"class": "woocommerce-Price-amount amount"}).get_text()
                price=price.replace('$','')
                print(price)
                if "1kg" in name:
                    per1kg = price
                else:
                    per1kg=""
                per1kg=per1kg.replace('$','')
                print(per1kg)
                wow.append(Product(name, price, per1kg, url, "MeatMarket"))
            except:
                pass
    return wow
if __name__ == "__main__":
    processMM('Beef Archives - Pendle Hill Meat Market.htm')