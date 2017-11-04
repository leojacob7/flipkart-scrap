# # import smtplib
# # server=smtplib.SMTP('smtp.gmail.com',587)
# # server.starttls()
# # server.login("heleny1819@gmail.com","qweqwe123")
# # message="message is sent"
# # server.sendmail("heleny1819@gmail.com","r1120924@mvrht.net",message)
# # server.quit()
# import smtplib
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# #Next, log in to the server
# # I have used xxxxxxx to denote password
# server.login("heleny1819@gmail.com", "qweqwe123")

# #Send the mail
# msg = "qwqwqw"
# server.sendmail("heleny1819@gmail.com", "", msg)
# server.quit()
import requests
import os
from bs4 import BeautifulSoup
#os.environ["HTTPS_PROXY"] = "http://username:pass@192.168.1.107:3128"
url= "https://www.flipkart.com/search?q=mac%20air&otracker=start&as-show=on&as=off" 
source_code = requests.get(url)
plain_text = source_code.content
soup = BeautifulSoup(plain_text,"html.parser")

box  = soup.find_all("div",{"class":"_6BWGkk"})
heading=soup.find_all("div",{"class":"_3wU53n"})
#print(box)
for i in range(len(box)):
	price=box[i].find("div",{"class":"_1vC4OE _2rQ-NK"})
#print(len(box))
	print(price.text[1:].replace(",","")),
	print(heading[0].text)
# content = box.contents

# box_len = len(box)
# print(box_len)

# for i in range(box_len):
#     links = content[i].find('div').find('div').findAll('a')
#     print(links[1]['title'])
    