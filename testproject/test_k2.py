from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# Oldal betöltése
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k2.html")
time.sleep(2)

# Oldal elemeinek és a gombok kinyerése
base_color = driver.find_element_by_id('randomColorName')
test_color = driver.find_element_by_id('testColorName')
start_button = driver.find_element_by_id('start')
stop_button = driver.find_element_by_id('stop')
all_colors = driver.find_element_by_id('allcolors')

# A színek listába konvertálása
all_colors_list = all_colors.text.replace('"', '').split(', ')


# Betöltődéskor helyesen jelenik-e meg az applikáció
def test_init():
    assert base_color.text in all_colors_list
    assert not test_color.is_displayed()


# A játék elundul, és megállítható
def test_start_stop():
    start_button.click()
    time.sleep(2)
    assert test_color.text in all_colors_list  # Vizsgálom, hogy megjelent-e szín a jobb oldalon
    stop_button.click()
    time.sleep(2)
    new_test_color = driver.find_element_by_id('testColorName')
    assert test_color.text == new_test_color.text  # Vizsgálom, hogy nem változott a szín a megállítás óta


# Annak a vizsgálata, hogy eltaláltam-e a színt
def test_working():
    result = driver.find_element_by_id('result')
    if base_color.text != test_color.text:
        assert result.text == 'Incorrect!'
    else:
        assert result.text == 'Correct!'
        driver.close()
