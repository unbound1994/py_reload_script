import unittest
import time

from selenium.common.exceptions import NoSuchElementException
from BrowserInit import BrowserInit

"""Базовые методы для всех файлов"""

driver = BrowserInit().driver


def open_page(url):
    driver.get(url)


def refresh():
    driver.refresh()


def closeWindow():
    driver.close()


def find_elem(locator):
    try:
        return driver.find_element(*locator)
    except NoSuchElementException:
        return False


def waiter(sec):
    time.sleep(sec)


if __name__ == '__main__':
    unittest.main()
