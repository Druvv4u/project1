

import smtplib
import time

def mail (encrypted):
    #smtp port and server address
    server= smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("narutobaka987@gmail.com","password@13")

    #(your mail, recipient's mail, message )
    server.sendmail("narutobaka987@gmail.com","ey825190@gmail.com", encrypted)
    server.quit()

def dec(encrypted , series):
    value =int(input("enter the key :"))
    decrypted=""
    for letter in encrypted:
        position2=series.find(letter)
        newp2= (position2-value)%53
        if letter==" ":
            decrypted+=" "
        else:
            decrypted+=series[newp2]
    print(decrypted)            


def enc():
    
    message =" hey there its me"
    value=5
    encrypted=""
    series="abcdefghijklmnopqrstuvwxyz"
    series+=series.upper()
    series+=" "

    for letter in message:
        position=series.find(letter)
        newp= (position+value)%53
        if letter==" ":
            encrypted+=" "
        else:
            encrypted+=series[newp]  
    print(encrypted)
    mail(encrypted)
    time.sleep(2)
    dec(encrypted,series)  
enc()