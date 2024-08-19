from selenium import webdriver
from selenium.webdriver.firefox.options import Options
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
...
"""

options = Options()
options.headless = False

# Inicializa el controlador de Firefox
driver = webdriver.Firefox(options=options)

# URL a la que deseas acceder
_ip = "http://89.208.107.49/"
_base_url = "https://n0pkf36.findpubdue.live/"

def calculateNewUser(qty_letters_usser):
    """
    Return [a-z]*qty
    """
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(qty_letters_usser))
    return letters


def getURL():
    return f"{_ip}{calculateNewUser(8)}"



# Recarga la página varias veces
for _ in range(1000):
    try:
        driver.get(getURL())
        print(f"get:{getURL()}")
    except:
        print(f"error:{getURL()}")

    time.sleep(5)  # Espera 1 segundo entre recargas para no sobrecargar

# Cierra el navegador
driver.quit()
