importrequests

url="https://store.steampowered.com/appreviews/730?json=1"

response=requests.get(url)

data=response.json()

print(data)

reviews=data['reviews']

print(reviews)

forreviewinreviews:

    customer_name=review['author']['personaname']

comment=review['review']

rating=review['voted_up']

ifrating:

        rating_text="Positive"

else:

        rating_text="Negative"

print("Customer Name: ",customer_name)

print("Comment: ",comment)

print("Rating: ",rating_text)

print("-"*60)