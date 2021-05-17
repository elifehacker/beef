from bs4 import BeautifulSoup
from product import Product
# https://www.meat4u.com.au/collections/premium-beef?page=1
def processM4U(file):
    wow = list()
    with open(file, 'r', encoding='utf8') as f:

        contents = f.read()
        soup = BeautifulSoup(contents, "html.parser")

        divs = soup.find_all("div", {"class": "item relative product-id item-row table-center clearfix"})
        for div in divs:
            #print(div)
            title = div.find("div",{"class": "item-title"})
            name = title.find("a").get_text().encode("ascii", errors="ignore").decode()
            url = title.find("a").get('href')
            print(name)
            print(url)
            try:
                price = div.find("span", {"class": "price-preview price price-field"}).get_text()
                print(price)
                price=price.replace('$','')
                if "1kg" in name or "/kg" in name:
                    per1kg = price
                else:
                    per1kg=""
                print(per1kg)
                per1kg=per1kg.replace('$','')
                wow.append(Product(name, price, per1kg, url, "Meat4u"))
            except:
                pass
    return wow
if __name__ == "__main__":
    processM4U('Premium Beef Meat 4 You.htm')