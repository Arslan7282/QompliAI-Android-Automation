import pytest
from appium import webdriver

from login.constants import APPIUM_SERVER_URL, APPIUM_CAPS


@pytest.fixture(scope="session")
def driver():
    try:
        # Try Appium 2.x API (newer version)
        from appium.options.android import UiAutomator2Options
        options = UiAutomator2Options()
        for key, value in APPIUM_CAPS.items():
            options.set_capability(key, value)
        driver = webdriver.Remote(
            command_executor=APPIUM_SERVER_URL,
            options=options,
        )
    except ImportError:
        # Fallback to Appium 1.x API (older version)
        driver = webdriver.Remote(
            command_executor=APPIUM_SERVER_URL,
            desired_capabilities=APPIUM_CAPS,
        )

    driver.implicitly_wait(5)
    yield driver
    driver.quit()

