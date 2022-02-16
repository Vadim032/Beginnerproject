import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME
    )

    driver.maximize_window()
    yield driver
    driver.quit()