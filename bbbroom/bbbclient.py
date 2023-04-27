from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


GREENLIGHT_URL = 'https://webconf-next.uni-osnabrueck.de/b/tim-0sr-kmb-cho'
WEBUI_URL = 'http://127.0.0.1:5000'

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)
driver.fullscreen_window()


def open_webui():
    driver.get(WEBUI_URL)


def wait_for(element, timeout=20):
    WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located(element))


def find_css(selector):
    return driver.find_element(By.CSS_SELECTOR, selector)

def join_room():
    driver.get(GREENLIGHT_URL)
    driver.fullscreen_window()

    # wait for Greenlight to load
    wait_for((By.CLASS_NAME, 'join-form'))

    # join meeting
    elem = driver.find_element(By.CLASS_NAME, 'join-form')
    elem.send_keys('Magic room')
    elem = driver.find_element(By.ID, 'room-join')
    elem.click()

    # wait for audio dialog and close dialog
    wait_for((By.CSS_SELECTOR, 'button[data-test="closeModal"]'))
    elem = driver.find_element(By.CSS_SELECTOR,
                               'button[data-test="closeModal"]')
    elem.click()

    # Hide public chat
    wait_for((By.CSS_SELECTOR, 'div[data-test="chatButton"]'))
    find_css('div[data-test="chatButton"]').click()


def whiteboard():
    wait_for((By.CSS_SELECTOR, 'button[data-test="whiteboardOptionsButton"]'))
    find_css('button[data-test="whiteboardOptionsButton"]').click()

    wait_for((By.CSS_SELECTOR, 'li[data-test="presentationFullscreen"]'))
    find_css('li[data-test="presentationFullscreen"]').click()
