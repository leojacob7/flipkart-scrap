
import requests
import os
from bs4 import BeautifulSoup
url= "https://www.flipkart.com/search?q=mac%20air&otracker=start&as-show=on&as=off" 
source_code = requests.get(url)
plain_text = source_code.content
soup = BeautifulSoup(plain_text,"html.parser")
#here the elements for mac book are in a list format
box  = soup.find_all("div",{"class":"_6BWGkk"})
heading=soup.find_all("div",{"class":"_3wU53n"})
for i in range(len(box)):
	price=box[i].find("div",{"class":"_1vC4OE _2rQ-NK"})
	print(price.text[1:].replace(",","")),
	print(heading[0].text)
