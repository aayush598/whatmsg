#whatsapp message

import pywhatkit
import pyautogui as pg
def whatsapp_msg():
    text=input('Enter the text you want to send: ')
    number=input('Enter the phone number you want to send message: ')
    repeat=input('How many times you want to send: ')
    hr=input('Hour: ')
    min=input('Minute: ')
    hr=int(hr)
    min=int(min)
    i=0
    while (i<repeat):
		pywhatkit.sendwhatmsg(number,text,hr,min)
		pg.press('Enter')
		i=i+1
whatsapp_msg()
