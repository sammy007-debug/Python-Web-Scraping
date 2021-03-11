import requests

from bs4 import BeautifulSoup

import smtplib

URL = 'https://www.amazon.es/Razer-Modelos-avanzados-CH5-T-4K-OLED/dp/B087VHQN9X/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Razer+Blade+15&qid=1615464502&sr=8-1'


headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

def checkPrice():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    ##print(soup.prettify())
    price = soup.find(id="priceblock_ourprice").get_text()
    converter = price[0:5]
    converter= float(converter)
    
    if (converter < 3.000):
        send_mail()

    print(converter)

  

   

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('wecodingalong@gmail.com', 'btadqpybwqjsexgn')

    subject = 'Yo the price is down!'
    body = 'Checkout the amazon link it time to spend that money!! https://www.amazon.es/Razer-Modelos-avanzados-CH5-T-4K-OLED/dp/B087VHQN9X/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Razer+Blade+15&qid=1615464502&sr=8-1 '
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'wecodingalong@gmail.com',
        'samuelolayemi221@yahoo.com',
        msg
    )

    print('Yo Email has been sent!')

    server.quit()

checkPrice()