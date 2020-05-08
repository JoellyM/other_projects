import requests
import smtplib
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/Mechanical-Keyboard-Keyboards-Detachable-Programmable/dp/B07QS6MG8B/ref=sr_1_6?crid=3DH39B1SPWKRB&keywords=mechanical+keyboard&qid=1572483324&sprefix=mechanical+k%2Caps%2C194&sr=8-6'

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content,  'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])

    if(converted_price > 35.99):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo

    print('working on it')

    server.login('j.ekomalet@gmail.com', 'bbrffkgilngnqbuy')

    subject = 'Price for Amazon item fell down!!'
    body = 'https://www.amazon.com/Mechanical-Keyboard-Keyboards-Detachable-Programmable/dp/B07QS6MG8B/ref=sr_1_6?crid=3DH39B1SPWKRB&keywords=mechanical+keyboard&qid=1572483324&sprefix=mechanical+k%2Caps%2C194&sr=8-6'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'j.ekomalet@gmail.com',
        'liljearsy@gmail.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

check_price()