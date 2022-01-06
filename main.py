import pandas as pd
from bs4 import BeautifulSoup
import requests

product_name=input()
product_name=product_name.replace(" ","%20")
x=requests.get("https://www.flipkart.com/search?q="+product_name+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soap = BeautifulSoup(x.content,'html.parser')

k=[]

for x in soap.find_all(class_='_13oc-S'):

    html=x.children
    for y in x.children:
         for t in y.find_all('a'):
             if t.get('title')!=None:
                a=t.get('title')

         for t in y.find_all(class_='_25b18c'):
             h=list(t.children)[0]
             if h.get_text()!=None:
                b=h.get_text()
         k.append([a,b])

print(pd.DataFrame(k))


