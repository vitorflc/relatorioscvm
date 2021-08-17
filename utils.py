import os
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

CONFIG = {}


def loadConfig():
    global CONFIG
    try:
        config = open(os.path.dirname(__file__) + '/config.txt', 'r')
        for line in config:
            constant = line.strip().split('->')
            CONFIG[str(constant[0]).strip()] = str(constant[1]).strip()
        config.close()
    except:
        print('Falha ao ler o config.')
        exit()


def wait_until_clickable(driver, xpath=None, class_name=None, name=None, id=None, duration=10000, frequency=0.01):
    if xpath:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    elif class_name:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
    elif name:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.NAME, name)))
    elif id:
        WebDriverWait(driver, duration, frequency).until(EC.element_to_be_clickable((By.ID, id)))

def wait_until_visible(driver, xpath=None, class_name=None, name=None, id=None, duration=10000, frequency=0.01):
    if xpath:
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    elif class_name:
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
    elif name:
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.NAME, name)))
    elif id:
        WebDriverWait(driver, duration, frequency).until(EC.visibility_of_element_located((By.ID, id)))

def getDriver():
    if CONFIG['browser'] == "firefox":
        options = webdriver.FirefoxOptions()
        if sys.platform == "darwin":
            executable_path = "./bin/geckodriver_mac"
        elif "linux" in sys.platform:
            executable_path = "./bin/geckodriver_linux"
        elif "win32" in sys.platform:
            executable_path = "./bin/geckodriver_win32.exe"
        return webdriver.Firefox(executable_path=executable_path, firefox_options=options, log_path=os.devnull)
    elif CONFIG['browser'] == "chrome":
        prefs = {"profile.managed_default_content_settings.images": 2}          # preferencia de ir sem imagens
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", prefs)
        if sys.platform == "darwin":
            executable_path = "./bin/chromedriver_mac"
        elif "linux" in sys.platform:
            executable_path = "./bin/chromedriver_linux"
        elif "win32" in sys.platform:
            executable_path = "./bin/chromedriver_win32.exe"
        return webdriver.Chrome(executable_path=executable_path, chrome_options=options)


def clickXpath(driver, xpath):
    wait_until_clickable(driver=driver, xpath=xpath)
    element = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].click();", element)

def clickName(driver, Name):
    wait_until_clickable(driver=driver, name=Name)
    element = driver.find_element_by_name(Name)
    driver.execute_script("arguments[0].click();", element)
    
# def seeName(driver, Name):
#     wait_until_visible(driver=driver, name=Name)
#     element = driver.find_element_by_name(Name)
#     driver.execute_script("arguments[0].click();", element)

def clickClassName(driver, className):
    wait_until_clickable(driver=driver, class_name=className)
    element = driver.find_element_by_class_name(className)
    driver.execute_script("arguments[0].click();", element)
    
def clickID(driver, ID):
    wait_until_clickable(driver=driver, id=ID)
    element = driver.find_element_by_id(ID)
    driver.execute_script("arguments[0].click();", element)

def fazLogin(driver):
    clickXpath(driver, '//*[@id="anchor-acessar-unite-oauth2"]')
    wait_until_visible(driver=driver, name='emailAddress')
    driver.find_element_by_name('emailAddress').click()
    driver.find_element_by_name('emailAddress').send_keys(CONFIG['login'])
    driver.find_element_by_name("password").click()
    driver.find_element_by_name("password").send_keys(CONFIG['password'])
    wait_until_clickable(driver=driver, xpath="""//*[@id="nike-unite-loginForm"]/div[6]/input""")
    driver.find_element_by_xpath("""//*[@id="nike-unite-loginForm"]/div[6]/input""").click()

def addMeia(driver):
    wait_until_clickable(driver=driver, xpath="""//*[@id="variacoes"]/div/div[2]/ul/li[2]/label""")
    try: 
        clickXpath(driver, '//*[@id="variacoes"]/div/div[2]/ul/li[3]/label')
    except:
        clickXpath(driver, '//*[@id="tamanho__idM''"]/following-sibling::label')
    clickXpath(driver, '//*[@id="btn-comprar"]')

def preencheCartao(driver):
    driver.find_element_by_id('ccard-number').send_keys(CONFIG['cardNumber'])
    driver.find_element_by_id('ccard-owner').send_keys(CONFIG['cardOwner'])
    driver.find_element_by_id('ccard-document').send_keys(CONFIG['cardDocument'])
    driver.find_element_by_id('exp-month').send_keys(CONFIG['expMonth'])
    driver.find_element_by_id('exp-year').send_keys(CONFIG['expYear'])
    driver.find_element_by_id('security-code').send_keys(CONFIG['securityCode'])
