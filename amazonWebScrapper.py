import requests
import smtplib
from bs4 import BeautifulSoup

URL = "https://www.amazon.com.tr/SanDisk-Cruzer-Glide-Flash-128GB/dp/B017RD11JQ/ref=sr_1_1?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2WW9CCP4OWQ2V&dchild=1&keywords=usb+bellek&qid=1596221423&sprefix=usb+%2Caps%2C245&sr=8-1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    productTitle = soup.find(id="productTitle").get_text()
    productPrice = soup.find(id="priceblock_ourprice").get_text()
    converted_productPrice = float(productPrice[1:3])


    print(productTitle.strip())
    print(converted_productPrice)

    if(converted_productPrice < 100):
        send_email()



def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('yazilimcifaik@gmail.com', 'bxeiwsuutdvpagmh')

    subject = 'New price brooooo!!'
    body    = 'Check this link out:\nhttps://www.amazon.com.tr/SanDisk-Cruzer-Glide-Flash-128GB/dp/B017RD11JQ/ref=sr_1_1?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2WW9CCP4OWQ2V&dchild=1&keywords=usb+bellek&qid=1596221423&sprefix=usb+%2Caps%2C245&sr=8-1'
    msg     = f"Subject: {subject}\n\n{body}"

    server.sendmail('yazilimcifaik@gmail.com',
                    'faikyesilyaprak@outlook.com',
                    msg)
    
    print("HEY EMAIL HAS BEEN SENT!!")

    server.quit()

check_price()