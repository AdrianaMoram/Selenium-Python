# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 17:40:33 2021

@author: morit
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
#from bs4 import BeautifulSoup
import os
#from datetime import datetime
from selenium.webdriver import ActionChains
import time

#from selenium.webdriver.support.ui import Select
B2=pd.ExcelFile('./Basededatos1.xlsx')    
df2=B2.parse('Hoja1')
row2=df2.shape[0]
print(row2)
cont2=0
def SegundoChrome(link='https://forms.gle/NoV5nu2UDDeXBa6JA'):
   
    link='https://forms.gle/NoV5nu2UDDeXBa6JA'
    driver2=webdriver.Chrome() #driver.get(link)
    driver2.get(link)
#f=driver.current_url
#print(f)
    time.sleep(2)
    action=ActionChains(driver2)
    for i in range (0,row2):
        
        Nombre=df2.iloc[i,0]
#CC="Cedula Ciudadania"
#df.iloc [0, 0]
        
        Apellido=df2.iloc[i,1]
        idf=driver2.find_elements_by_class_name('quantumWizTextinputPaperinputInput.exportInput')
#nombre
        idf[0].send_keys(Nombre)
#Apellido
        time.sleep(1)
        idf[1].send_keys(Apellido)
        time.sleep(1)
        CC=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div:nth-child(1) > label > div > div.docssharedWizToggleLabeledContent > div > span')
        TI=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div:nth-child(2) > label > div > div.docssharedWizToggleLabeledContent > div > span')
        PE=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(3) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div:nth-child(3) > label > div > div.docssharedWizToggleLabeledContent > div > span')
        if str(df2.iloc[i,2])=="Cedula Ciudadania":
            CC.click()
        elif str(df2.iloc[i,2])=="Tarjeta de Identificación":
                     TI.click()
        else:
                PE.click()
        time.sleep(1)
        NumeroId=str(df2.iloc[i,3])
        idf[2].send_keys(NumeroId)
        time.sleep(1)
        Opcion1=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(5) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div > label > div > div.docssharedWizToggleLabeledContent > div > span')
        Opcion1.click()
        Bogt=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(6) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div:nth-child(1) > label > div > div.docssharedWizToggleLabeledContent > div > span')
        Villa=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(6) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div:nth-child(2) > label > div > div.docssharedWizToggleLabeledContent > div > span')
        Arme=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(6) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div:nth-child(3) > label > div > div.docssharedWizToggleLabeledContent > div > span')
        time.sleep(1)
        if str(df2.iloc[i,5])=="Bogotá":
                Bogt.click()
            
        elif str(df2.iloc[i,5])=="Villavicencio":
                     Villa.click()
        else:
                Arme.click()
                print(df2.iloc[i,5])
        time.sleep(1)
        Casa=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(7) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div:nth-child(1) > label > div > div.docssharedWizToggleLabeledContent > div > span')
        Apt=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(7) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div:nth-child(2) > label > div > div.docssharedWizToggleLabeledContent > div > span')
        habsola=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(7) > div > div > div.freebirdFormviewerComponentsQuestionRadioRoot > div:nth-child(2) > div > span > div > div:nth-child(3) > label > div > div.docssharedWizToggleLabeledContent > div > span')
       
        if str(df2.iloc[i,6])=="Casa":
                Casa.click()
            
        elif str(df2.iloc[i,6])=="Apartamento":
                     Apt.click()
        else:
                habsola.click()
                print(df2.iloc[i,6])
        time.sleep(1)        
        ABC=driver2.find_elements_by_class_name('quantumWizTogglePapercheckboxInnerBox')
        
        
        if df2.iloc[i,7]==1:
           
          ABC[0].click()
        else:
            ABC[1].click()
        time.sleep(2)  
        if df2.iloc[i,8]==1:
           
          ABC[2].click()
        else:
            ABC[3].click()
        time.sleep(2)
        if df2.iloc[i,9]==1:
           
          ABC[4].click()
       
        else:
           ABC[5].click()             
        time.sleep(1)
        Aa=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(9) > div > div > div.freebirdFormviewerComponentsQuestionGridRoot > div > div.freebirdFormviewerComponentsQuestionGridScrollContainer > div > div:nth-child(2) > span > div:nth-child(2) > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
        Ba=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(9) > div > div > div.freebirdFormviewerComponentsQuestionGridRoot > div > div.freebirdFormviewerComponentsQuestionGridScrollContainer > div > div:nth-child(4) > span > div:nth-child(2) > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
        Ca=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(9) > div > div > div.freebirdFormviewerComponentsQuestionGridRoot > div > div.freebirdFormviewerComponentsQuestionGridScrollContainer > div > div:nth-child(6) > span > div:nth-child(2) > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
        Da=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(9) > div > div > div.freebirdFormviewerComponentsQuestionGridRoot > div > div.freebirdFormviewerComponentsQuestionGridScrollContainer > div > div:nth-child(6) > span > div:nth-child(2) > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
       
        if df2.iloc[i,10]==1:
            Aa.click()
            time.sleep(2)     
        if df2.iloc[i,11]==1: 
            Ba.click()
            time.sleep(2)
        if df2.iloc[i,12]==1:
            Ca.click()
            time.sleep(2)   
         
        uno=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(10) > div > div > div.freebirdFormviewerComponentsQuestionScaleRoot > div.appsMaterialWizToggleRadiogroupGroupContainer.exportGroupContainer.freebirdFormviewerComponentsQuestionScaleScaleRadioGroup > span > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
        dos=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(10) > div > div > div.freebirdFormviewerComponentsQuestionScaleRoot > div.appsMaterialWizToggleRadiogroupGroupContainer.exportGroupContainer.freebirdFormviewerComponentsQuestionScaleScaleRadioGroup > span > div > label:nth-child(2) > div.freebirdMaterialScalecontentInput > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
        tres=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(10) > div > div > div.freebirdFormviewerComponentsQuestionScaleRoot > div.appsMaterialWizToggleRadiogroupGroupContainer.exportGroupContainer.freebirdFormviewerComponentsQuestionScaleScaleRadioGroup > span > div > label:nth-child(4) > div.freebirdMaterialScalecontentInput > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
        cuatro=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(10) > div > div > div.freebirdFormviewerComponentsQuestionScaleRoot > div.appsMaterialWizToggleRadiogroupGroupContainer.exportGroupContainer.freebirdFormviewerComponentsQuestionScaleScaleRadioGroup > span > div > label:nth-child(5) > div.freebirdMaterialScalecontentInput > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div') 
        cinco=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(10) > div > div > div.freebirdFormviewerComponentsQuestionScaleRoot > div.appsMaterialWizToggleRadiogroupGroupContainer.exportGroupContainer.freebirdFormviewerComponentsQuestionScaleScaleRadioGroup > span > div > label:nth-child(6) > div.freebirdMaterialScalecontentInput > div > div > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div')
       
        if df2.iloc[i,14]==1:
                
             uno.click()
            
        elif df2.iloc[i,14]==2:
            dos.click()
        elif df2.iloc[i,14]==3:
            tres.click()
        elif df2.iloc[i,14]==4:
            cuatro.click()
       
        else:
                cinco.click()
                print(df2.iloc[i,14])    
        time.sleep(2)    
        Botonenviar=driver2.find_element_by_css_selector('#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div > span > span')
        Botonenviar.click()
        time.sleep(1)
        driver2.get(link)
        time.sleep(1)


SegundoChrome()

