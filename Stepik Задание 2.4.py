from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math


try:
   
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = WebDriverWait(browser, 14).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    browser.find_element_by_id('book').click()


    x=int(browser.find_element_by_id('input_value').text)
    calc=str(math.log(abs(12*math.sin(x))))
    browser.find_element_by_id('answer').send_keys(calc)
    browser.find_element_by_id('solve').click()
    time.sleep(6)
    browser.quit()

except Exception as e:
    print(e)
