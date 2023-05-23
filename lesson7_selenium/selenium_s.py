from fake_useragent import UserAgent

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.common.exceptions import InvalidSelectorException, \
    ElementClickInterceptedException
from time import sleep

CHECK_USER = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'

ua = UserAgent()
user_agent = ua.random

# FireFox
# service = Service("/home/user/PycharmProjects/Parsing/lesson7_selenium/geckodriver")
# binary = FirefoxBinary('/usr/bin/firefox')

service = Service()
options = Options()
# options.add_experimental_option("useAutomationExtension", False)
# options.add_experimental_option("excludeSwitches",["enable-automation"])
# options.add_argument('disable-infobars')
# options.add_argument(f'user-agent={user_agent}')
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("cookie=qrator_jsr=1683908627.519.taGZepVVaHSweQyt"
                     "-4rtp10lq4ccq51ad3l1cju2h9lgnl3ep-00; qrator_ssid=1683908628.318.RVUkbetygSwsXN6j-vijn4thl0l8t2sguvrv70clrgl6uq2oo; qrator_jsid=1683908627.519.taGZepVVaHSweQyt-b0f8f67imhe9065vlrjb2elvs27s6viv; _slid_server=; ggr-widget-test=0; GACookieStorage=undefined; st_uid=af908d08974d8b8726a18b8e229b5b4a; _ym_uid=168390863620123027; _ym_d=1683908636; _singleCheckout=true; _unifiedCheckout=true; _showSberPay=true; _clientTypeInBasket=true; _gaexp=GAX1.2.IUgFRjY7S7qnkK4uRsCZRw.19540.3; x-api-option=srch-2705; _ym_isad=2; ___dmpkit___=398e64a2-61df-4cf4-ac91-01fc0fac71bc; uxs_uid=66f51900-f0e1-11ed-bb46-e32ecd36ed0c; adrdel=1; adrcid=A6zzygbL63AfsJOBxHHEwAQ; iap.uid=ffc218d398194bee8232b9daa07c87cb; aplaut_distinct_id=sP3gLpQuhCTG; _regionID=34; cookie_accepted=true; tmr_lvid=ff4911688958472547feb80acea5c467; tmr_lvidTS=1683908647719; tmr_detect=0%7C1683908650037; _ga_Z72HLV7H6T=GS1.1.1683908636.1.1.1683908654.0.0.0; _ga=GA1.2.814016764.1683908637; _gid=GA1.2.754620211.1683908655; _gat_UA-20946020-1=1")

# Firefox
# options.set_preference("dom.webdriver.enabled", False)
# options.set_preference("general.useragent.override", user_agent)

driver = webdriver.Chrome(options=options)
# driver.get("https://leroymerlin.ru/catalogue/arki-mezhkomnatnye/")
driver.get("https://www.all4tattoo.ru/piercing/tools/")
# driver.get(CHECK_USER)

# WebDriverWait(driver, 10).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

result = []
flag = True
while flag:
    WebDriverWait(driver, 10).until(lambda driver: driver.execute_script(
        'return document.readyState') == 'complete')

    try:
        elements = driver.find_elements(By.CLASS_NAME, 'thumbnail')
        if len(elements) < 30 :
            flag = False
    except InvalidSelectorException:
        break

    for card in elements:
        card_dict = {}
        link = card.find_element(By.TAG_NAME, "a")
        name = link.get_attribute('title')
        img = card.find_element(By.TAG_NAME, "img")
        price = card.find_element(By.CLASS_NAME, "price")

        card_dict['link'] = link.get_attribute('href')
        card_dict['name'] = name
        card_dict['img'] = img.get_attribute('src')
        card_dict['price'] = price.text.split(' ')[0]

        result.append(card_dict)

    try:
        next_page = driver.find_element(By.XPATH,
                                        '//a[contains(text(), "Туда")]')
        next_page.click()
    except (InvalidSelectorException, ElementClickInterceptedException) as \
            error:
        break

print(result)

driver.close()
