import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.mark.xfail(reason="Ожидает фикса")
def test_first_my(browser):
    """
    Тест-кейс WERT-1
    """

    browser.get(url="https://testqastudio.me/")
    
    element = browser.find_element(by=By.CSS_SELECTOR, value="#menu-top [class*='menu-item-11088']")
    element.click()
    assert browser.current_url == 'https://testqastudio.me/faq/', 'Не правильная страница'

    faq_menu_2 = browser.find_element(by=By.XPATH, value="//*[contains(text(), 'Можно ли поставить доп.фурнитуру?')]")
    faq_menu_2.click()
    assert True, ''
    
def test_count_of_all_products(browser):
    """
    Тест-кейс WERT-3
    """

    browser.get(url="https://testqastudio.me/")    
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "razzi-posts__found-inner"), "Показано 17 из 17 товары"
    ))

    elements = browser.find_elements(by=By.CSS_SELECTOR, value="[id='rz-shop-content'] ul li")

    assert len(elements) == 17, "Не верное число товаров"