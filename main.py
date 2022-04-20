import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, \
    NoSuchElementException, StaleElementReferenceException


service = Service(ADD YOUR USER ADDRESS E.G. user/....)
driver = webdriver.Chrome(service=service)
webpage = "https://orteil.dashnet.org/cookieclicker/"
driver.get(webpage)


def cookie_count():
    count = driver.find_element(By.ID, value="cookies")
    try:
        total_num = int(count.text.split()[0].replace(",", ""))
    except IndexError:
        pass
    return total_num

cookie = driver.find_element(By.ID, value="bigCookie")


timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes
COOKIE_COUNT = 200
products = []


def get_products():
    global product_int
    for x in range(18):
        value = f"product{x}"
        # print(value)
        product = driver.find_element(By.ID, value=value)
        product_int = product.text
        # products.append(product_int)
    return product_int


products_price = []

while True:
    count_cookie = cookie_count()
    cookie.click()
    # if count_cookie > COOKIE_COUNT:
    #     print(COOKIE_COUNT)
    #     COOKIE_COUNT = COOKIE_COUNT*2

    if time.time() > timeout:
        try:
            driver.find_element(By.ID, value="upgrade0").click()
        except (StaleElementReferenceException, NoSuchElementException) as w:
            pass

        for x in range(18):
            value = f"productPrice{x}"
            product = driver.find_element(By.ID, value=value)
            product_text = product.text
            if product_text == "":
                # print("nahh")
                pass
            else:
                prices = product.text.replace(",", "")
                products_price.append(prices)
        for h in reversed(products_price):
            # print(h)
            current_index = products_price.index(h)
            # print(current_index)
            price_value = f"product{current_index}"
            try:
                driver.find_element(By.ID, value=price_value).click()
            except (ElementClickInterceptedException, ElementNotInteractableException, NoSuchElementException) as e:
                pass

        timeout = time.time() + 5
    if time.time() > five_min:
        break

driver.quit()
