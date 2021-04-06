import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.in/ZR-Aluminum-Strung-Badminton-Racquet/dp/B07QWSNTVY/ref=sr_1_2?dchild=1&keywords=badminton&qid=1591530583&sr=8-2"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}


def check_price():

    print("sending request")
    page = requests.get(URL, headers=headers)
    print("request recieved")
    soup = BeautifulSoup(page.content,'html.parser')
    print("parsing successful")
    
    print("searching for data")
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    print("data found")

    converted_price = float(price[2:5])

    print(title.strip())
    print(converted_price)


    if(converted_price <= 500):
        send_mail()

def send_mail():
    print("connecting to email server")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    print("server connected")

    server.login('nihalpuramgiis@gmail.com','REDACTED')
    print("login successful")
    subject = "price fell down buy now \n"
    body = " open the link \n https://www.amazon.in/ZR-Aluminum-Strung-Badminton-Racquet/dp/B07QWSNTVY/ref=sr_1_2?dchild=1&keywords=badminton&qid=1591530583&sr=8-2"

    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail("nihalpuramgiis@gmail.com","puramnihal@gmail.com",msg)
    print("hey message has been sent!")
    server.quit()
    exit()

while(True):
    check_price()
    time.sleep(60*60*6)
