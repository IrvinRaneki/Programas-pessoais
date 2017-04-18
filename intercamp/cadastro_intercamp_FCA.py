#!/bin/python
#coding: utf-8

import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys


def init_driver():
    driver = webdriver.Firefox()
    driver.wait = WebDriverWait(driver, 0)
    return driver


def lookup(driver, data):
    nome=sys.argv[1]+" "+sys.argv[2]
    ra = sys.argv[3]
    email=sys.argv[4]
    motivo=sys.argv[5]

    a=int(sys.argv[6])
    b=int(sys.argv[7])
    c=int(sys.argv[8])
    d=int(sys.argv[9])
    e=int(sys.argv[10])
    f=int(sys.argv[11])
    g=int(sys.argv[12])
    h=int(sys.argv[13])

    #print nome
    #print ra
    #print email
    #print motivo

    #print "a", a
    #print "b", b
    #print "c", c
    #print "d", d
    #print "e", e
    #print "f", f
    #print "g", g
    #print "h", h

    http="https://docs.google.com/forms/d/1N3RHDZDFuXoSHU5TWuAfYYSGeUCqEPeAJZYJ3FLU69g/viewform?formkey=dEQwUWtDNm81Z0hnQnpfay1NUGhZUlE6MQ&fromEmail=true"
    #webbrowser.open_new(http) #isso abre o navegador padrao
    driver.get(http)

    try:
        #box1 = driver.wait.until(EC.presence_of_element_located((By.NAME, "entry.1000000")))
        #box1.send_keys(ra)

        box1 = driver.find_element_by_name("entry.1000000")
        box1.send_keys(ra)
        box2 = driver.find_element_by_name("entry.1000001")
        box2.send_keys(nome)
        box3 = driver.find_element_by_name("entry.1000003")
        box3.send_keys(email)
        box4 = driver.find_element_by_name("entry.1000005")
        box4.send_keys(motivo[0])
        box5 = driver.find_element_by_name("entry.1000008")
        box5.send_keys(data)

        ##checkbox
        ## 06:00 go to campinas
        box6 = driver.find_elements_by_name("entry.1000006")[1-a]
        box6.click()

        box7 = driver.find_elements_by_name("entry.1000007")[1-b] # 2 itens na lista do radio btn (escolha 1)
        box7.click()
        box8 = driver.find_elements_by_name("entry.1729785991")[1-c]
        box8.click()
        box9 = driver.find_elements_by_name("entry.968610607")[1-d]
        box9.click()
        box10 = driver.find_elements_by_name("entry.576367717")[1-e]
        box10.click()

        ##18:00 back to limeira
        box11 = driver.find_elements_by_name("entry.221136388")[1-f]
        box11.click()

        box12 = driver.find_elements_by_name("entry.449771019")[1-g]
        box12.click()
        box13 = driver.find_elements_by_name("entry.881017458")[1-h]
        box13.click()

        ##submi btn
        #time.sleep(15)
        #box8 = driver.find_element_by_name("submit")
        #box8.click()

    except TimeoutException:
        print("Nao foi")


if __name__ == "__main__":

    for ano in range(2017,2018):
        for mes in range(4,5):
            for dia in range(1,31):
                data=str(dia)+"/"+str(mes)+"/"+str(ano)
                print(data)
                driver = init_driver()
                lookup(driver, data)
                time.sleep(0.5)
                driver.quit()
