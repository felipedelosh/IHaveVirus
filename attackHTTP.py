from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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

https://n0pkf36.findpubdue.live/lqkcgvut/?u=63fkp0n&o=uh7pmz8&f=1&sid=t1~t0edj5cp4iejludsvza1vobl&fp=Md%2Bb%2FogcsL6hTN%2FIdl07EQ%3D%3D
https://n0pkf36.findpubdue.live/vnjpymod/?u=63fkp0n&o=uh7pmz8&f=1&sid=t2~saav2u21tvhgu0fe4vblc3jh&fp=PgJxGtpSbeXystT1Izv8Cg%3D%3D
https://n0pkf36.aycanrem.live/xyxnihui/?u=63fkp0n&o=uh7pmz8&f=1&sid=t4~kyaz4wemqibazztgozu52xnv&fp=6Hsu7We1SMxgE36BjBtYvw%3D%3D
https://n0pkf36.aycanrem.live/fbnopstn/?u=63fkp0n&o=uh7pmz8&f=1&sid=t1~zfansszdwb3csgk5fbxp5v40&fp=0zNK8x040n85RsPDbQRlbw%3D%3D
https://n0pkf36.lastwayking.live/vplsqjcq/?u=63fkp0n&o=uh7pmz8&f=1&sid=t2~3hentehcpiyfynvjwarxwsvm&fp=J0tGtZLaeppAA9svwVencw%3D%3D
https://n0pkf36.lastwayking.live/ounuqvsi/?u=63fkp0n&o=uh7pmz8&f=1&sid=t1~dem2e4bc4fujgn033wkb2r2u&fp=dZgngM70hemNUGuErnKGCA%3D%3D
https://n0pkf36.lastwayking.live/chdthuix/?u=63fkp0n&o=uh7pmz8&f=1&sid=t1~dem2e4bc4fujgn033wkb2r2u&fp=MlFTGuXKlT25neTD1K7eBA%3D%3D
...
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


# URL a la que deseas acceder
_ip = "http://89.208.107.49/"
_base_url = "https://n0pkf36.findpubdue.live/"
_FAKE_PAGES_LIST = [
    "findpubdue.live",
    "aycanrem.live",
    "lastwayking.live",
    "kihisee.live"
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
# https://n0pkf36.kihisee.live/fqitthsw/?u=63fkp0n&o=uh7pmz8&f=1&sid=t4~gp4vdvsnabw0rlejkbh0kdt3&fp=i9Ev4R9boJ5ZBrUR1Q7nYw%3D%3D
# https://n0pkf36.kihisee.live/ajewwcvw/?u=63fkp0n&o=uh7pmz8&f=1&sid=t4~gp4vdvsnabw0rlejkbh0kdt3&fp=PffWcRnbu79onJaibHwHdw%3D%3D
def finalDestinationUrl():
    return f"https://n0pkf36.{getRndFakePage()}/{calculateNewUser(8)}/?u={_user}&o={_o}&f=1{getSecurityToken()}"


# Recarga la página varias veces
for _ in range(1000000):
    _url = finalDestinationUrl()
    try:
        driver.get(_url)
        _LOGS_ = _LOGS_ + f"get:{_url}\n"
        _LOGS_ = _LOGS_ + f"currentURL:{driver.current_url}\n"
        print(f"get:{_url}")
        print(f"currentURL:{driver.current_url}")
    except:
        _LOGS_ = _LOGS_ + f"error:{_url}\n"
        print(f"error:{_url}")

    # SAVE LOG
    updateLOG()
    time.sleep(100)  # Espera 1 segundo entre recargas para no sobrecargar

# Cierra el navegador
driver.quit()
