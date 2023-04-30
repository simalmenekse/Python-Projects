from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "C:\Chrome Driver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 10
five_min = time.time() + 60*5 # 5minutes

game_on = True

while game_on:
    cookie.click() # Adjust the sleep time to click faster or slower
# Check for affordable upgrades every 5 seconds
    money = driver.find_element_by_id("money")
    try:
        cookie_coins = int(money.text)
    except ValueError:
        cookie_coins = int(money.text.replace(",", ""))
    if time.time() > timeout:
        time.sleep(0.1)
    store_items = [item.split(" - ") for item in
    driver.find_element_by_id("store").text.split("\n")]
    for item in store_items:
        if len(item) > 2 or len(item) < 2:
            store_items.remove(item)
    for item in store_items:
        try:
            item[1] = int(item[1])
        except ValueError:
            item[1] = int(item[1].replace(",", ""))
        except IndexError:
            pass

    available_items = []
    unavailable_items = [item.text.split("\n")[0].split(" - ") for item in
                         driver.find_elements_by_class_name("grayed")[0:-1]]
    for item in unavailable_items:
        try:
            item[1] = int(item[1])
        except ValueError:
            item[1] = int(item[1].replace(",", ""))
        except IndexError:
            pass

    for item in store_items:
        if len(item) == 1:
            store_items.remove(item)

    for item in store_items:
        if item not in unavailable_items:
            available_items.append(item)
            # Find the maximum integer using the max() function
            max_integer = 0
            max_string = ""
            # Print the maximum integer
            for sublist in available_items:
                try:
                    if sublist[1] > max_integer:
                        max_integer = sublist[1]
                        max_string = sublist[0]
                except IndexError:
                    pass

                if cookie_coins >= max_integer:
                    item_to_buy = driver.find_element_by_id(f"buy{max_string}")
                    item_to_buy.click()

                if time.time() >= five_min:
                    game_on = False
                    cookies_per_second = driver.find_element_by_id("cps")
                    print(cookies_per_second.text)
            timeout = time.time() + 10