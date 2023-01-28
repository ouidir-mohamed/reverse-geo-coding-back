import uuid
from selenium import webdriver
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')



def takeScreenShot(polyline:str):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('http://localhost/preview_route?poly='+polyline)
    sleep(3)
    randomName =  'static/'+str(uuid.uuid4())+".png"
    driver.get_screenshot_as_file(randomName)
    driver.quit()
    print("end...")
    return randomName