#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui
import pyperclip
import timer


pyautogui.PAUSE = 0.3

#apertar win
pyautogui.press('win')

#escrever chrome
chrome = 'Google Chrome'
pyperclip.copy(chrome)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#clicar no perfil trabalho
timer.PAUSE = 5
pyautogui.click(x=958, y=569)


#apertar ctrl t
pyautogui.hotkey('ctrl', 't')
#digitar link
ponto = 'https://app.pontomaisweb.com.br/#/meu_ponto/registro_de_ponto'
pyperclip.copy(ponto)
pyautogui.hotkey('ctrl', 'v')
pyautogui.PAUSE = 10
pyautogui.press('enter')

#Clicar no Ponto
pyautogui.click(x=-1042, y=397)


# ## Setar Timer

# In[ ]:


#Timer de bater ponto:

