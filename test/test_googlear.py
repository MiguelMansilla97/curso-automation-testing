from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver.implicitly_wait(10) # Espera implicita de 10 segundos para que los 
# #elementos se carguen antes de lanzar una excepcion

def test_busqueda_tech( chome_driver ):
    wait = WebDriverWait(chome_driver, 4) # Espera explicita de 10 segundos para esperar a que un elemento cumpla una condicion antes de lanzar una excepcion

    chome_driver.get("https://duckduckgo.com/")

    try:
        input_google = wait.until(EC.presence_of_element_located((By.NAME, "q")))
        input_google.send_keys("talento tech")
        input_google.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"Ocurrio un error: {e}")
    finally:
        chome_driver.quit()