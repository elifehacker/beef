from bs4 import BeautifulSoup
from product import Product
#https://www.woolworths.com.au/shop/browse/meat-seafood-deli/meat/beef-veal
#https://www.woolworths.com.au/shop/browse/meat-seafood-deli/meat/beef-veal?pageNumber=2
def processWow(file):
    wow = list()
    with open(file, 'r',  encoding='utf-8') as f:

        contents = f.read()
        soup = BeautifulSoup(contents, "html.parser")

        divs = soup.find_all("div", {"class": "shelfProductTile-content"})
        for div in divs:
            #print(div)
            name = div.find("a", {"class": "shelfProductTile-descriptionLink"}).get_text()
            url = div.find("a", {"class": "shelfProductTile-descriptionLink"}).get('href')
            print(name)
            print(url)
            try:
                dollar = div.find("span", {"class": "price-dollars"}).get_text()
                cent = div.find("span", {"class": "price-cents"}).get_text()
                print(dollar+'.'+cent)
                per1kg = div.find("div", {"class": "shelfProductTile-cupPrice"}).get_text()
                per1kg = per1kg.split(' ')[1][1:]
                print(per1kg)
                wow.append(Product(name, dollar+'.'+cent, per1kg, url, "WOW"))
            except:
                pass
    return wow
if __name__ == "__main__":
    processWow('Fresh Beef & Veal Woolworths.htm')