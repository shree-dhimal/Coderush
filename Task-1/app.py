from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import time
import smtplib


app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=["POST"])
def submit():
    text1 = request.form.get['Symbol']
    text2 = request.form.get['Price']
    text3 = request.form.get['smsText']
    text4 = request.form.get['emailText']
    dropdown1 = request.form.get['dropdown1']
    dropdown2 = request.form.get['dropdown2']


    if dropdown1 == '_15':
        f_time = 15
    elif dropdown1=='_20':
        f_time = 20
    elif dropdown1== '_1':
        f_time = 60
    

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)

        

    Stock_Name = text1
    Stock_url = "https://finance.yahoo.com/quote/"+Stock_Name+"?p="+Stock_Name+"&.tsrc=fin-srch"
    #Stock_url = "https:/finance.yahoo.com/quote/"+Stock_Name+"/history?p="+ Stock_Name

    #print(Stock_url)

    response = requests.get(Stock_url)

    #print(response)

    soup = BeautifulSoup(response.text, 'html.parser')

    #data = soup.find(id="")
    #print(data)

    data = soup.find(id="quote-header-info")
    final_price = data.find("fin-streamer",class_="Fw(b) Fz(36px) Mb(-4px) D(ib)").getText()

    print(final_price)
    content = "Your price threshold reached, i.e:"+ final_price
    if text2 == final_price:
        if dropdown2 == "email":
            sender = 'noreplynofacemaskalert@gmail.com'
            sender_pass = 'kzgocnslulvajdxb'
            
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender,sender_pass)
            server.sendmail(sender,text4,content)
        elif dropdown2 == "sms":
            pass
   
    return render_template('submit.html')

if __name__ == "__main__":
    app.run(debug=True)