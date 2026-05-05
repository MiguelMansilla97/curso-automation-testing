import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# fixtures
@pytest.fixture
def numeros ():
    return 10, 2

@pytest.fixture
def producto_mouse():
    return {"Nombre": "Mouse", "precio": 20}

@pytest.fixture
def carrito_vacio():
    return []

@pytest.fixture
def productos_carrito():
    return [{"Nombre": "Mouse", "precio": 20}, {"Nombre": "Teclado", "precio": 50}, 
            {"Nombre": "Monitor", "precio": 100}, {"Nombre": "Impresora", "precio": 150}]

@pytest.fixture
def chome_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()