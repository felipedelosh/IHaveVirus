from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from datetime import datetime
import time
import random
import string

"""
Estoy siendo atacado todos los días por http://89.208.107.49
Esto es para tratar de defenderme
"""


"""
URL attacks me:

ListURL.txt
"""

options = Options()
options.headless = False

# Inicializa el controlador de Firefox
driver = webdriver.Firefox(options=options)

def currentDate():
    return datetime.now().strftime("%Y-%m-%d")

def restoreLog():
    try:
        with open('log.log', 'r', encoding="UTF-8") as f:
            return f.read()
    except:
        print("============NOT FIND LOG FILE=========")
    return ""


_LOGS_ = f"{currentDate()}\n{restoreLog()}"
def updateLOG():
    with open('log.log', 'w', encoding="UTF-8") as f:
        f.write(_LOGS_)


# SITE URL PARAMS
_ip = "89.208.107.49"

# Never be same in the week
_FAKE_PAGES_LIST = [
    "findpubdue.live",
    "aycanrem.live",
    "lastwayking.live",
    "kihisee.live",
    "rootyeprely.live"
]
_user = "63fkp0n"
_o = "uh7pmz8"

def calculateNewUser(qty_letters_usser):
    """
    Return [a-z]*qty
    """
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(qty_letters_usser))
    return letters

def generate_random_id(length=24):
    prefix = f"t{random.randint(1, 4)}~"
    characters = string.ascii_lowercase + string.digits
    random_id = ''.join(random.choice(characters) for _ in range(length))
    return prefix + random_id

def generate_custom_fp(length=22):
    characters = string.ascii_letters + string.digits
    random_fp = ''.join(random.choice(characters) for _ in range(length))
    return random_fp + '%3D%3D'

def getSecurityToken():
    """
    The page contains a sid & fp loke a tokens
    Exaple
    &sid=t1~dem2e4bc4fujgn033wkb2r2u&fp=MlFTGuXKlT25neTD1K7eBA%3D%3D
    """
    return f"&sid={generate_random_id(24)}&fp={generate_custom_fp(22)}"


def getURLByIp():
    return f"{_ip}{calculateNewUser(8)}"

def getRndFakePage():
    return random.choice(_FAKE_PAGES_LIST)

# Examples
# IP+ USER + PARAMS
def finalDestinationUrl():
    return f"http://{_ip}/{calculateNewUser(8)}/?u={_user}&o={_o}&f=1{getSecurityToken()}"


# Recarga la página varias veces
for _ in range(1000000):
    _url = finalDestinationUrl()
    try:
        driver.get(_url)
        _LOGS_ += f"get:{_url}\n"
        _LOGS_ += f"currentURL:{driver.current_url}\n"
        print(f"get:{_url}")
        print(f"currentURL:{driver.current_url}")
    except WebDriverException as e:
        if "ERR_CERT_AUTHORITY_INVALID" in str(e) or "NET::ERR_CERT_DATE_INVALID" in str(e):
            _LOGS_ += f"secure_connection_failed:{_url}\n"
            print(f"secure_connection_failed:{_url}")
        else:
            _LOGS_ += f"error:{_url}\n"
            print(f"error:{_url}")

    # SAVE LOG
    #updateLOG()
    time.sleep(0.2)  # Espera 0.4 segundos entre recargas para no sobrecargar

# Cierra el navegador
driver.quit()
