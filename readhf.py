from bs4 import BeautifulSoup
from product import Product
#https://www.harrisfarm.com.au/collections/beef
def processHF(file):
    wow = list()
    with open(file, 'r', encoding='utf8') as f:

        contents = f.read()
        contents = contents.replace("compare_at_price unit_price","xxxx")
        soup = BeautifulSoup(contents, "html.parser")

        divs = soup.find_all("div", {"class": "caption"})
        for div in divs:
            
            try:
                name = div.find("a").get_text()
                name = name.strip()
                print(name)
                url = "https://www.harrisfarm.com.au/collections/beef"+div.find("a").get('href')
                print(url)
                price = div.find("span", {"class": "from_price"}).get_text()
                price = price[1:]
                print(price)
                sale = div.find("span", {"class": "sale"})
                #print(sale)
                per1kg = sale.find("span",{"class": "xxxx"}).get_text()
                per1kg = per1kg.split(' ')[0][1:]
                print(per1kg)
                wow.append(Product(name, price, per1kg, url, "HarrisFarm"))
            except:
                pass
    return wow
if __name__ == "__main__":
    print("HF")
    processHF('webs/hf1.htm')