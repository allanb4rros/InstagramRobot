import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from search_and_follow_Instagram import search_and_follow_insta

@pytest.fixture

def driver():
    chrome_options = Options()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-popup-blocking')  # Desativa o bloqueio de pop-ups
    chrome_options.add_argument('--disable-notifications')  # Desativa o bloqueio de notificações
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def test_search_and_follow(driver):
    usernames = ["user1", "user2", "user3"]
    total_followed = search_and_follow_insta("https://instagram.com.br", usernames)
    assert total_followed == len(usernames)

def test_search_and_follow_empty(driver):
    usernames = []
    total_followed = search_and_follow_insta("https://instagram.com.br", usernames)
    assert total_followed == 0
