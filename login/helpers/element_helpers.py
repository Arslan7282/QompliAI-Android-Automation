import os
import time
from datetime import datetime
from typing import List, Tuple, Optional
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from appium.webdriver.webdriver import WebDriver


class ElementHelpers:
    """Simplified helper class for element interactions and utilities"""

    @staticmethod
    def element_exists(driver: WebDriver, selectors: List[Tuple], timeout: int = 5) -> bool:
        """Check if any element from the list of selectors exists"""
        for by, selector in selectors:
            try:
                WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((by, selector))
                )
                return True
            except (TimeoutException, NoSuchElementException):
                continue
        return False
    # dfsasdfasd
    @staticmethod
    def wait_for_element(driver: WebDriver, selectors: List[Tuple], timeout: int = 3):
        """Wait for and return the first element found from the list of selectors"""
        last_exception = None
        for by, selector in selectors:
            try:
                return WebDriverWait(driver, timeout).until(
                    EC.presence_of_element_located((by, selector))
                )
            except (TimeoutException, NoSuchElementException) as e:
                last_exception = e
        raise TimeoutException(f"Element not found with any selector. Last error: {last_exception}")

    @staticmethod
    def safe_send_keys(driver: WebDriver, selectors: List[Tuple], text: str, clear_first: bool = True) -> bool:
        """Safely send keys to an element"""
        try:
            element = ElementHelpers.wait_for_element(driver, selectors)
            if clear_first:
                element.clear()
            element.send_keys(text)
            return True
        except Exception as e:
            print(f"⚠ Error sending keys: {e}")
            return False

    @staticmethod
    def safe_click(driver: WebDriver, selectors: List[Tuple]) -> bool:
        """Safely click an element"""
        try:
            element = ElementHelpers.wait_for_element(driver, selectors)
            element.click()
            time.sleep(0.3)
            return True
        except Exception as e:
            print(f"⚠ Error clicking element: {e}")
            return False

    @staticmethod
    def take_screenshot(driver: WebDriver, filename: Optional[str] = None) -> str:
        """Take a screenshot and save it to screenshots directory"""
        screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        if not filename:
            filename = f"screenshot_{datetime.now():%Y%m%d_%H%M%S}.png"
        filepath = os.path.join(screenshots_dir, filename)
        try:
            driver.save_screenshot(filepath)
            print(f"✓ Screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            print(f"⚠ Failed to save screenshot: {e}")
            return ""

    @staticmethod
    def get_page_source(driver: WebDriver, save_to_file: bool = False, filename: Optional[str] = None) -> str:
        """Get page source and optionally save to file"""
        try:
            page_source = driver.page_source
            if save_to_file:
                page_sources_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "page_sources")
                os.makedirs(page_sources_dir, exist_ok=True)
                if not filename:
                    filename = f"page_source_{datetime.now():%Y%m%d_%H%M%S}.xml"
                filepath = os.path.join(page_sources_dir, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(page_source)
                print(f"✓ Page source saved: {filepath}")
            return page_source
        except Exception as e:
            print(f"⚠ Failed to get page source: {e}")
            return ""
