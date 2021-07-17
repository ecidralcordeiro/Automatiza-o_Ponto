#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import schedule
import pyautogui
import pyperclip
import time
import timer


pyautogui.PAUSE = 1

def beatTime():
    pyautogui.PAUSE = 1

    #Press win
    pyautogui.press('win')

    #write Chome
    chrome = 'Google Chrome'
    pyperclip.copy(chrome)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')

    #Click work
    timer.PAUSE = 4
    #pyautogui.click(x=958, y=569)

    #press ctrl t
    pyautogui.hotkey('ctrl', 't')
    #digitar link
    ponto = 'https://app.pontomaisweb.com.br/#/meu_ponto/registro_de_ponto'
    pyperclip.copy(ponto)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.PAUSE = 10
    pyautogui.press('enter')

    #Clicar no Ponto
    pyautogui.click(x=-1042, y=397)

#Horas e dias que quero
schedule.every().monday.at("09:40").do(beatTime)
schedule.every().monday.at("11:50").do(beatTime)
schedule.every().monday.at("13:10").do(beatTime)
schedule.every().monday.at("17:00").do(beatTime)

schedule.every().tuesday.at("09:30").do(beatTime)
schedule.every().tuesday.at("11:30").do(beatTime)
schedule.every().tuesday.at("13:00").do(beatTime)
schedule.every().tuesday.at("17:00").do(beatTime)

schedule.every().wednesday.at("09:30").do(beatTime)
schedule.every().wednesday.at("11:30").do(beatTime)
schedule.every().wednesday.at("13:00").do(beatTime)
schedule.every().wednesday.at("17:00").do(beatTime)

schedule.every().thursday.at("09:30").do(beatTime)
schedule.every().thursday.at("11:30").do(beatTime)
schedule.every().thursday.at("13:00").do(beatTime)
schedule.every().thursday.at("17:00").do(beatTime)

schedule.every().friday.at("09:30").do(beatTime)
schedule.every().friday.at("11:30").do(beatTime)
schedule.every().friday.at("13:00").do(beatTime)
schedule.every().friday.at("17:00").do(beatTime)


while 1:
    schedule.run_pending()
    time.sleep(1)
# In[ ]:


#Timer de bater ponto:

