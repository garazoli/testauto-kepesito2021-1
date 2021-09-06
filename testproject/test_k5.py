from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# Oldal betöltése
driver.get("https://ambitious-sky-0d3acbd03.azurestaticapps.net/k5.html")
time.sleep(2)

play_button = driver.find_element_by_id('spin')
init_button = driver.find_element_by_id('init')


# Applikáció helyes megjelenése
def test_init():
    bingo_cells_list = driver.find_elements_by_xpath('//td')
    assert len(bingo_cells_list) == 25
    numbers_list = driver.find_elements_by_xpath('//ol/li')
    assert len(numbers_list) == 75


# Bingo számok ellnőrzése
def test_game():
    while True:
        play_button.click()
        time.sleep(0.5)
        bingo_results = driver.find_elements_by_xpath('//*[@id="messages"]/li')
        if len(bingo_results) == 1:
            break
    checked_bingo_cells = driver.find_elements_by_xpath('//td[@class="checked"]')
    checked_numbers = driver.find_elements_by_xpath('//li[@class="checked"]')
    checked_bingo_cells_nums = []
    checked_numbers_nums = []
    for i in checked_bingo_cells:
        checked_bingo_cells_nums.append(i.get_attribute('value'))
    for i in checked_numbers:
        checked_numbers_nums.append(i.get_attribute('value'))
    assert checked_bingo_cells in checked_numbers_nums


# Játék újraindítása
def test_restart():
    init_button.click()
    bingo_cells_list = driver.find_elements_by_xpath('//td')
    assert len(bingo_cells_list) == 25
    numbers_list = driver.find_elements_by_xpath('//ol/li')
    assert len(numbers_list) == 75
    checked_bingo_cells = driver.find_elements_by_xpath('//td[@class="checked"]')
    checked_numbers = driver.find_elements_by_xpath('//li[@class="checked"]')
    assert checked_bingo_cells == []
    assert checked_numbers == []
    driver.close()
