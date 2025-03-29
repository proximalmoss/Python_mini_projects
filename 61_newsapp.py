import requests
import json
interest=input("what type of news are you interested in?")
url=f"https://newsapi.org/v2/everything?q={interest}&from=2025-02-20&sortBy=publishedAt&apiKey=b452b934308946d3950203adac594c26"
r=requests.get(url)
news=json.loads(r.text)
#print(news,type(news))
for article in news["articles"]: #in browser this name is given for that dictionary
    print(article["title"]) #in browser this name is given for that key
    print(article["description"]) #in browser this name is given for that value
    print("____________________")