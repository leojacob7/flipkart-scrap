import requests
import os
from bs4 import BeautifulSoup
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.ehlo()
server.login("webscrapeleo@gmail.com", "qweqwepoipoi")
#os.environ["HTTPS_PROXY"] = "http://username:pass@192.168.1.107:3128"
url= "https://www.flipkart.com/search?q=mac%20air&otracker=start&as-show=on&as=off" 
source_code = requests.get(url)
plain_text = source_code.content
soup = BeautifulSoup(plain_text,"html.parser")

box  = soup.find_all("div",{"class":"_6BWGkk"})
heading=soup.find_all("div",{"class":"_3wU53n"})
#print(box)
min=50000
for i in range(len(box)):
	price=box[i].find("div",{"class":"_1vC4OE _2rQ-NK"})		
	if (min) > int(price.text[1:].replace(",","")):
	   min=int(price.text[1:].replace(",",""))
	   k=i
	
msg="Best price for " + (heading[k].text[:18]) + " costs : " + str(min)
server.sendmail("webscrapeleo@gmail.com", "leobjacob@gmail.com", msg)
print "########"
