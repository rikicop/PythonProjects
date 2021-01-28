from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re
import time

start_time = time.time()

#HIDE CHROME
opt = webdriver.ChromeOptions()
opt.add_argument('headless')
opt.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver',options=opt)
time.sleep(2)
driver.get('https://twitter.com/dolartoday')
time.sleep(2)
pageSource = driver.execute_script("return document.documentElement.outerHTML;")
#Cierra Chrome para np perder memoria
driver.close()

#REGEX
re_find  =  re.findall('cotiza a Bs.(.+?),',  pageSource)
joined = ''.join(str(e) for e in re_find)
re_rm_dupl = re.sub(r'\b(\w+)( \1\b)+', r'\1', joined)
re_wwspace = re_rm_dupl.lstrip()

#CONVERTIR A NUMERO FLOTANTE
x=float(re_wwspace)
print("Tipo de dato:\n")
print(type(x))
ecu = x + 1000000
print("Resultado de sumar un millón: " , ecu )


#FORMATO DECIMAL
xf = '{:,.2f}'.format(x)
print("Número en formato decimal: ", xf)

print ("My program took", time.time() - start_time, "to run")
