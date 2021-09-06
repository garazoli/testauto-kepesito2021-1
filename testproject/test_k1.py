from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# Oldal betöltése
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k1.html")
time.sleep(2)

# Oldal mezőinek és a submit gomb kinyerése
input_a = driver.find_element_by_id('a')
input_b = driver.find_element_by_id('b')
submit_button = driver.find_element_by_id('submit')
result = driver.find_element_by_id('result')

# Tesztadatok és elvárt eredmények
test_data_a = ['', '2', '']
test_data_b = ['', '3', '']
expected_results = ['', '10', 'NaN']


# Függvény a form törlésére, kitöltésére és az adatok beküldésére
def clear_and_fill_form(a, b):
    input_a.clear()
    input_b.clear()
    input_a.send_keys(a)
    input_b.send_keys(b)
    submit_button.click()
    time.sleep(1)


# Betöltéskor az oldal helyes megjelenésének ellenőrzése
def test_init():
    assert input_a.text == test_data_a[0]
    assert input_b.text == test_data_b[0]
    assert not result.is_displayed()


# Helyes számítás ellenörzése
def test_correct():
    clear_and_fill_form(test_data_a[1], test_data_b[1])
    assert result.text == expected_results[1]


# Üres kitöltés esete
def test_empty():
    clear_and_fill_form(test_data_a[2], test_data_b[2])
    assert result.text == expected_results[2]
    driver.close()
