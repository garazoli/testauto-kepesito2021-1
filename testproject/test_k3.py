from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# Oldal betöltése
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k3.html")
time.sleep(2)

# Mező kinyrése az oldalról
input_field = driver.find_element_by_id('title')

# Tesztadatok és elvárt erdmények
test_data = ['abcd1234', 'teszt233@', 'abcd']
expected_results = ['', 'Only a-z and 0-9 characters allewed', 'Title should be at least 8 characters; you entered 4.']


# Függvény a mező törlésére és kitöltésére
def clear_and_fill(text):
    input_field.clear()
    input_field.send_keys(text)
    time.sleep(1)


# Helyes kitöltés esete
def test_valid():
    clear_and_fill(test_data[0])
    message = driver.find_element_by_xpath('//span')
    assert message.text == expected_results[0]


# Illegális karakterek esete
def test_illegal_chars():
    clear_and_fill(test_data[1])
    message = driver.find_element_by_xpath('//span')
    assert message.text == expected_results[1]


# Túl rövid bemenet esete
def test_short_entry():
    clear_and_fill(test_data[2])
    message = driver.find_element_by_xpath('//span')
    assert message.text == expected_results[2]
    driver.close()
