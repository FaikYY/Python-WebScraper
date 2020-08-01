# encoding:utf-8

import requests
import smtplib
import time
from email.mime.text import MIMEText
from bs4 import BeautifulSoup

## Taranacak URL 
URL = "https://www.hepsiburada.com/apple-macbook-air-icin-45w-magsafe-2-guc-adaptoru-tr-uyumulu-md592ch-a-p-HBV00000F014K"

## Tarayıcı bilgileri
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}



    ################# FONKSİYONLAR ################# 

## Fiyat kontrol fonksiyonu ##
def check_price():
    ## Belirtilen urlye şu browser ile istekte bulun
    page = requests.get(URL, headers=headers)

    ## HTML kodlarını çek
    soup = BeautifulSoup(page.content, 'html.parser')

    ## Ürün başlığını al (String olarak)
    productTitle = soup.find(id="product-name").get_text()

    ## Ürün fiyatını al (String olarak)
    productPrice = soup.find("div", {"class": "extra-discount-price"}).get_text()
    
    ## Konsola ürün başlığını ve fiyatını yazdır
    print(productTitle.strip())
    print(productPrice)

    ## Email yollama fonksiyonunu çalıştır
    send_email(productTitle.strip(), productPrice)
##############################
    



## Email yollama fonksiyonu (Türkçe yazılarda saçmalıyor. UTF8 desteği yok bu fonksiyonda. İngilizce için ideal) ##
def send_email_old(title, price):
    ## Belirtilen gmail serverına bağlan
    server = smtplib.SMTP('smtp.gmail.com', 587)

    ## Bağlantıyı başlat
    server.ehlo()

    ## Bağlantıyı şifrele
    server.starttls()

    ## Bağlantıyı tekrar başlat
    server.ehlo()

    ## Belirtilen hesap bilgilerini kullan (mail, şifre (google uygulama özel şifresi))
    server.login('yazilimcifaik@gmail.com', 'bxeiwsuutdvpagmh')

    ## Mail içinde olacak konu başlık ve içerik bölümü
    subject = 'The USB price fell down!!'
    body    = 'Title: ' + title + '\nPrice: ' + price
    msg     = f"Subject: {subject}\n\n{body}"

    ## Email yolla (gönderen, alıcı, mesaj)
    server.sendmail('yazilimcifaik@gmail.com',
                    'faikyesilyaprak@outlook.com',
                    msg.encode('UTF-8'))
    
    ## Konsola mail yollandı yaz
    print("HEY EMAIL HAS BEEN SENT SUCCESSFULLY!!")

    ## Mail serverından çıkış yap
    server.quit()
#################################



## Email yollama fonksiyonu (UTF8 destekli. Türkçe gayet güzel çalışıyor)
def send_email(title, price):

    ## Text türü
    text_type = 'plain' # or 'html'

    ## Mailin body kısmı içerik yani
    text = 'Başlık: ' + title + '\nFiyat: ' + price

    ## Mesajı tanımla (mesaj, mesaj tipi, encode türü)
    msg = MIMEText(text, text_type, 'utf-8')

    ## Mail konu kısmı
    msg['Subject'] = 'Yeni bir üründe indirim var!!'

    ## Mail gönderen
    msg['From'] = 'yazilimcifaik@gmail.com'

    ## Mail alıcı
    msg['To'] = 'faikyesilyaprak@outlook.com'

    ## Mail server ayarı
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    ## Mail server için gönderici bilgileri (mail, şifre (google 2 yönlü uygulama şifresi))
    server.login('yazilimcifaik@gmail.com', 'bxeiwsuutdvpagmh')

    ## Mesajı yolla
    server.send_message(msg)

    ## Yedek kod
    # or server.sendmail(msg['From'], msg['To'], msg.as_string())


    ## Konsola mail yollandı yaz
    print("HEY EMAIL HAS BEEN SENT SUCCESSFULLY!!")

    ## Mail serverından çıkış yap
    server.quit()
##############################



############### FONKSİYON ÇALIŞTIRMA BÖLÜMÜ ###############
while(true):    
    check_price()
    time.sleep(60 * 60)