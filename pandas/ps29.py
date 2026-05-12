importrequests

frombs4importBeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/static/computer/laptops"

response=requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")

products=soup.find_all("div",class_="thumbnail")

forproductinproducts:

    name_tag=product.find("a",class_="title")

name=name_tag.text.strip()ifname_tagelse"No Name"

price_tag=product.find("h4",class_="price")

price=price_tag.text.strip()ifprice_tagelse"No Price"

review_tag=product.find("p",class_="review-count")

reviews=review_tag.text.strip()ifreview_tagelse"No Reviews"

rating=len(product.find_all("span",class_="glyphicon-star"))

print("Product Name:",name)

print("Price:",price)

print("Reviews:",reviews)

print("Rating:",rating,"Stars")

print("-"*50)