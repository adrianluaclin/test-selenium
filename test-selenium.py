
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
  
    driver = webdriver.Chrome()  

    
    driver.get('file:///C:/Users/ADRIAN%20LUACES/Desktop/TEST/test.html')

   
    tabla = driver.find_element(By.ID,'tableId')

   
    filas = tabla.find_elements(By.TAG_NAME,'tr')

    celdas = filas[0].find_elements(By.TAG_NAME,'th')
      
    print([ celda.text for celda in celdas])
   
    for fila in filas[1:]:
     
        celdas = fila.find_elements(By.TAG_NAME,'td')
      
        print([ celda.text for celda in celdas])
        
    driver.quit()
except Exception as e:
    print(e)