from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# Oldal betöltése
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k4.html")
time.sleep(2)

# Oldal értékeinek és a gomb kinyerése
char_set = driver.find_element_by_xpath('/html/body/div/div/p[3]')
char = driver.find_element_by_id('chr')
op = driver.find_element_by_id('op')
num = driver.find_element_by_id('num')
button = driver.find_element_by_id('submit')

# Tesztadat - az összes érvényes karakter
test_data_chars = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"


# Függvény a karakterek listába szedéséhez karakterenként
def split(string):
    return list(string)


char_set_list = (split(test_data_chars))


# Az applikáció helyesen betöltődik
def test_char_table():
    assert char_set.text == test_data_chars


# Megjelenik-e egy érvényes művelet
def test_operation_appear():
    assert char.text in char_set_list
    assert op.text is '-' or '+'
    assert type(int(num.text)) is int


# A gombnyomás után helyesen végződik-e el a művelet
def test_working():
    button.click()
    time.sleep(2)
    result = driver.find_element_by_id('result')
    x = 0
    # Ezzel a ciklussal találom meg az eredmény indexét a listában
    for i in char_set_list:
        if i != result.text:
            x += 1
            continue
        else:
            x += 1
            return x

    # Itt az eredményt összehasonlítom a listában a művelet elvégzése utáni listaértékkel
    if op.text == '+':
        assert result.text == char_set_list[x + int(num.text)]
    else:
        assert result.text == char_set_list[x - int(num.text)]
    driver.close()
