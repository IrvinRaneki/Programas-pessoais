#!/bin/python
import time
from datetime import datetime
now = datetime.now()

import datetime

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


data_save = datetime.datetime.now()

def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 5)
    return driver


def lookup(driver, data):
    global data_save
    login="i081641"
    senha="irg094001"
    ra="081641"
    nome="Irvin Gomes"
    email="irvin.alemao@gmail.com"
    motivo="es"

    http="http://sistemas.ft.unicamp.br/onibus/"
    driver.get(http)

    try:
        box1 = driver.wait.until(EC.presence_of_element_located((By.NAME, "user")))
        box1.send_keys(login)
        box2 = driver.wait.until(EC.presence_of_element_located((By.NAME, "password")))
        box2.send_keys(senha)
        box2.send_keys(Keys.RETURN)

        ##entrou na pagina
        box3 = driver.wait.until(EC.presence_of_element_located((By.NAME, "motivo")))
        box3.send_keys(motivo)
        box3.send_keys(Keys.TAB)
        box4 = driver.wait.until(EC.presence_of_element_located((By.NAME, "data_uso")))
        box4.send_keys(data)
        box4.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)

    except TimeoutException:
        arquivo = open('/home/estagiario/Documents/git_gsf/trunk/testes/teste.txt','w')
        arquivo.write(str(data_save))
        arquivo.close()
        print("Nao foi")


def main():
    global data_save

    Diasemana = ('segunda feira','terceira feira','quarta feira', 'quinta feira','sexta feira','sabado','domingo')
    data = datetime.datetime.now()
    dia = datetime.date.weekday(data)

    arquivo = open('/home/estagiario/Documents/git_gsf/trunk/testes/teste.txt','r')
    data = arquivo.read()
    data_save = data
    arquivo.close()

    data = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S.%f")+ datetime.timedelta(days=1)
    dia = datetime.date.weekday(data)


    if dia < 5:
        print(data.strftime('%d/%m/%Y'))
        print(Diasemana[dia])
        print()

        result = data.strftime('%d/%m/%Y')


        arquivo = open('/home/estagiario/Documents/git_gsf/trunk/testes/teste.txt','w')
        arquivo.write(str(data))
        arquivo.close()

    if dia is 5:
        print(data.strftime('%d/%m/%Y'))
        print(Diasemana[dia])
        print()

        dia = datetime.date.weekday(data + datetime.timedelta(days = 2))
        data = data + datetime.timedelta(days=2)

        print(data.strftime('%d/%m/%Y'))
        print(Diasemana[dia])
        result = data.strftime('%d/%m/%Y')
        print()

        arquivo = open('/home/estagiario/Documents/git_gsf/trunk/testes/teste.txt','w')
        arquivo.write(str(data))
        arquivo.close()

    if dia is 6:
        print(data.strftime('%d/%m/%Y'))
        print(Diasemana[dia])
        print()

        dia = datetime.date.weekday(data + datetime.timedelta(days = 1))
        data = data + datetime.timedelta(days=1)

        print(data.strftime('%d/%m/%Y'))
        print(Diasemana[dia])
        result = data.strftime('%d/%m/%Y')
        print()

        arquivo = open('/home/estagiario/Documents/git_gsf/trunk/testes/teste.txt','w')
        arquivo.write(str(data))
        arquivo.close()

    print('vai mandar', result)
    print()
    driver = init_driver()
    lookup(driver, result)
    time.sleep(0.5)
    driver.quit()


if __name__ == "__main__":
    main()
