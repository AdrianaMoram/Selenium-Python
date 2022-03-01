# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""Se importan categorias"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
from bs4 import BeautifulSoup
import os
from datetime import datetime
from selenium.webdriver import ActionChains
import time
#from selenium.webdriver.support.ui import Select



#Se importan los datos de excel
#B1=pd.ExcelFile('./Basededatos.xlsx')    
#df=B1.parse('Hoja1')
#row=df.shape[0]

#print(row)



def primerChrome(link='https://www.bbvaassetmanagement.com/am/am/co/ce/inversionista-particular/fondos-inversion/ficha/PAIS/BBVA%20PAIS%20CLASE%20A?origen=netl'):
    
    link='https://www.bbvaassetmanagement.com/am/am/co/ce/inversionista-particular/fondos-inversion/ficha/PAIS/BBVA%20PAIS%20CLASE%20A?origen=net'
    driver=webdriver.Chrome() #driver.get(link)
    #driveropt= Options()
    #driveropt.add_argument("--incognito")
    driver.get(link)

#f=driver.current_url
#print(f)
    time.sleep(15)
    #link2='javascript:void(document.oncontextmenu=null);'
    #driver.get(link2)
    action=ActionChains(driver)
 
    numero=driver.find_elements
   #print(numero)
    time.sleep(15)
 #https://bbva-cells-files.s3.amazonaws.com/cells/apps/bbva_es_ficha_global_am_cells/bbva_ficha_global_am_cells_co/master/cellsapp/prod/vulcanize/index.html#!/fichaco/CCAPAISCB
        
primerChrome()



