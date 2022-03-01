# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 22:43:18 2021

@author: morit
"""
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class ExplicitWaitTest(unittest.TestCase):
    
    def setUp(self):

       self.driver=webdriver.Chrome(executable_path = 'chromedriver.exe')
       driver=self.driver
       driver.implicitly_wait(10)
       driver.maximize_window()
       driver.get('https://www.bbva.com.co/personas/productos/inversion/fondos/pais.html')
   

    def test_value(self):
        
        iframe=self.driver.find_element_by_id('content-iframe_copy')
        self.driver.execute_script("arguments[0].scrollIntoView();", iframe)
        self.driver.switch_to.frame(iframe)
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, 'cells-template-fichaco')))
        #time.sleep(15)
        #cosa= driver.find_element_by_id('cells-template-fichaco')
        texto=self.driver.execute_script("return document.querySelector('fichaco-page').shadowRoot.querySelector('cells-template-paper-drawer-panel div.container div.entrada div.primer-contenido div.caja-liquidativo-rentabilidad p.liquidativo-rentabilidad')")
        print( texto.text)
        
        
        
    def tearDown(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.close()

    
if __name__ == "__main__":
    unittest.main(verbosity= 2)        