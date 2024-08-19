from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import random
import string

"""
Estoy siendo atacado todos los dóías por http://89.208.107.49
Esto es para tratar de defenderme
"""


"""
URL attacks me:

https://n0pkf36.findpubdue.live/lqkcgvut/?u=63fkp0n&o=uh7pmz8&f=1&sid=t1~t0edj5cp4iejludsvza1vobl&fp=Md%2Bb%2FogcsL6hTN%2FIdl07EQ%3D%3D
https://n0pkf36.findpubdue.live/vnjpyomd/?u=63fkp0n&o=uh7pmz8&f=1&sid=t2~saav2u21tvhgu0fe4vblc3jh&fp=PgJxGtpSbeXystT1Izv8Cg%3D%3D
"""

options = Options()
options.headless = False

# Inicializa el controlador de Firefox
driver = webdriver.Firefox(options=options)

# URL a la que deseas acceder
_ip = "http://89.208.107.49/"
_base_url = "https://n0pkf36.findpubdue.live/"
_url= f"{_base_url}vnjpyomd"

# Abre la página
driver.get(_url)


def calculateNewUser(qty_letters_usser):
    """
    Return [a-z]*qty
    """
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(qty_letters_usser))
    return letters



# Recarga la página varias veces
for _ in range(1000):  # Cambia el valor si quieres recargar más o menos veces
    driver.refresh()
    time.sleep(1)  # Espera 1 segundo entre recargas para no sobrecargar

# Cierra el navegador
driver.quit()
