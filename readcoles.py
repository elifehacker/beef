from bs4 import BeautifulSoup
from product import Product
import decimal
#https://shop.coles.com.au/a/national/everything/browse/meat-seafood-deli/bef-veal?pageNumber=1
def processColes(file):
    wow = list()
    with open(file, 'r', encoding='utf8') as f:

        contents = f.read()
        soup = BeautifulSoup(contents, "html.parser")

        divs = soup.find_all("div", {"class": "product"})
        for div in divs:
            try:
                name = div.find("span", {"class": "product-name"}).get_text()
                url = div.find("a").get('href')
                if "https" not in url:
                    url="https://shop.coles.com.au"+url
                print(name)
                print(url)
                dollar = div.find("span", {"class": "dollar-value"}).get_text()
                cent = div.find("span", {"class": "cent-value"}).get_text()
                print(dollar+cent)
                per1kg = div.find("span", {"class": "package-price"}).get_text()
                unit = per1kg.split(' ')[-1]
                per1kg = per1kg.split(' ')[0][1:]
                if unit =='100G':
                    per1kg = str(decimal.Decimal(per1kg)*10)
                print(per1kg)
                wow.append(Product(name, dollar+cent, per1kg, url, "COLES"))
            except:
                pass
    return wow
if __name__ == "__main__":
    processColes('Beef & Veal Meat & Seafood Everything Coles Online.htm')