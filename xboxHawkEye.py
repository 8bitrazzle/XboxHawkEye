import pyautogui as pag
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import winsound

driver = webdriver.Chrome();
driver.maximize_window();

driver.get('https://www.walmart.com/ip/Xbox-Series-X/443574645');
driver.execute_script("window.open ('https://www.amazon.com/dp/B08H75RTZ8?tag=nismain-20&linkCode=ogi&th=1', 'tab2')");
driver.execute_script("window.open ('https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6;28324', 'tab3')");
driver.execute_script("window.open ('https://www.target.com/p/xbox-series-x-console/-/A-80790841#lnk=sametab', 'tab4')");

def locateStockWalmart():
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    time.sleep(4)
    cords = pag.locateOnScreen('walmartcart.PNG')
    pag.click(cords)
    if cords is None:
      return True
    else:
      return False
    
def locateStockTarget():
    driver.switch_to.window(driver.window_handles[1])
    driver.refresh()
    time.sleep(4)
    cords0 = pag.locateOnScreen('targetpickup.PNG')
    cords1 = pag.locateOnScreen('targetdeliver.PNG')
    cords2 = pag.locateOnScreen('targetship.PNG')
    if all(v is None for v in [cords0, cords1, cords2]):
      return True
    else:
      return False
	
def locateStockBestbuy():
    driver.switch_to.window(driver.window_handles[2])
    driver.refresh()
    time.sleep(4)
    cords0 = pag.locateOnScreen('bestbuycart.PNG')
    pag.click(cords0)
    time.sleep(2)
    cords1 = pag.locateOnScreen('bestbuygocart.PNG')
    pag.click(cords1)
    if cords0 is None:
      return True
    else:
      return False
	
def locateStockAmazon():
    driver.switch_to.window(driver.window_handles[3])
    driver.refresh()
    time.sleep(4)
    cords = pag.locateOnScreen('amazoncart.PNG')
    pag.click(cords)
    if cords is None:
      return True
    else:
      return False


while True:
    if locateStockWalmart() is True:
        pass
    else:
        print("Walmart has an xbox in stock!")
        frequency = 3500  
        duration = 10000  
        winsound.Beep(frequency, duration)
        break
    if locateStockTarget() is True:
        pass
    else:
        print("Target has an xbox in stock!")
        frequency = 3500  
        duration = 10000  
        winsound.Beep(frequency, duration)
        break
    
    if locateStockBestbuy() is True:
        pass
    else:
        print("Best Buy has an xbox in stock!")
        frequency = 3500  
        duration = 10000  
        winsound.Beep(frequency, duration)
        break

    if locateStockAmazon() is True:
        pass
    else:
        print("Amazon has an xbox in stock!")
        frequency = 3500  
        duration = 10000  
        winsound.Beep(frequency, duration)
        break

	
	
	
	
	
	
	
