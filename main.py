import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from utils import loadConfig

loadConfig()  # le o arquivo com as informações desejadas de se retirar do website
# posteriormente quero interagir com o Excel, retirar as infos de lá e colocar lá um relatório.

wd = webdriver.Chrome('chromedriver')     # permite definir 'wd' para chamar o método Chrome para o webdriver
wd.get("https://www.rad.cvm.gov.br/ENET/frmConsultaExternaCVM.aspx") # Link de extração dos relatórios divulgados pela CVM

