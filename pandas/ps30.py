importrequests

frombs4importBeautifulSoup

url="https://books.toscrape.com/"

response=requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")

books=soup.find_all("article",class_="product_pod")

forbookinbooks:

    title=book.h3.a["title"]

price=book.find("p",class_="price_color").text

availability=book.find("p",class_="instock availability").text.strip()

rating_class=book.find("p")["class"][1]

print("Book Name:",title)

print("Price:",price)

print("Availability:",availability)

print("Rating:",rating_class)

print("-"*50)