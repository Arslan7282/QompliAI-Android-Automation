import unittest
import time
import sys
import os

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from config import (
    get_android_options,
    APPIUM_SERVER_URL,
    TEST_CREDENTIALS,
    APP_PACKAGE
)
from helpers.auth_helpers import AuthHelpers
from helpers.element_helpers import ElementHelpers


# ============================================
# Central reusable mapping for all menu titles
# ============================================
MENU_TITLES = {
    "Dashboard": "//android.widget.TextView[@text='Dashboard']",
    "Properties": "(//android.widget.TextView[@text='Properties'])[1]",
    "Inspections": "(//android.widget.TextView[@text='Inspections'])[1]",
    "Violations": "(//android.widget.TextView[@text='Violations'])[1]",
    "Non-Compliant": "//android.widget.TextView[@text='Non-Compliant']",
    "Contracts": "(//android.widget.TextView[@text='Contracts'])[1]",
    "Marketplace": "(//android.widget.TextView[@text='Marketplace'])[1]",
    "Payment History": "(//android.widget.TextView[@text='Payment History'])[1]",
    "Job Filing": "(//android.widget.TextView[@text='Job Filing'])[1]",
    "QompliGov AI": "(//android.widget.TextView[@text='QompliGov AI'])[1]",
    "Settings": "//android.widget.TextView[@text='Qompliai']"
}


class SignInTests(unittest.TestCase):

    # ============================
    # Helper: Get title text
    # ============================
    def get_title(self, name):
        xpath = MENU_TITLES[name]
        try:
            elem = ElementHelpers.wait_for_element(
                self.driver, [(AppiumBy.XPATH, xpath)]
            )
            return elem.text
        except:
            return None

    # ============================
    # Helper: Find tooltip text
    # ============================
    def get_tooltip_text(self, expected_substring, timeout=6):
        """
        Finds tooltip text matching expected_substring anywhere in TextViews.
        Returns text if found, None if not found.
        """
        end_time = time.time() + timeout
        while time.time() < end_time:
            # search all text views
            elems = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
            for e in elems:
                txt = e.text or ""
                if expected_substring in txt:
                    return txt
            time.sleep(0.3)
        return None


    # ============================
    # Init / Cleanup
    # ============================
    @classmethod
    def setUpClass(cls):
        options = get_android_options()
        cls.driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        try:
            if self.driver.current_package != APP_PACKAGE:
                self.driver.activate_app(APP_PACKAGE)
        except:
            self.driver.activate_app(APP_PACKAGE)

    # ============================
    # Sign-in screen handler
    # ============================
    def ensure_sign_in_page(self):
        selectors = [
            (AppiumBy.XPATH, "//*[@text='Sign In']"),
            (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint,'Email')]"),
        ]
        return ElementHelpers.element_exists(self.driver, selectors, timeout=3)


    # ============================
    # TC-SI-000: Tooltip for invalid email
    # ============================
    def test_000_invalid_email_tooltip(self):
        print("\n=== TC-SI-000: Invalid Email Tooltip Check ===")

        # Ensure we are on the sign-in screen
        self.ensure_sign_in_page()

        # Enter invalid email
        ElementHelpers.safe_send_keys(
            self.driver,
            [(AppiumBy.XPATH, "//android.widget.EditText[contains(@hint,'Email')]")],
            "dgfg"
        )

        # Try to trigger validation
        try:
            self.driver.hide_keyboard()
        except:
            pass

        # Tap Sign In to force validation
        AuthHelpers.submit_login(self.driver)
        time.sleep(1)

        # EXPECTED TEXT FROM YOUR SCREENSHOT
        expected = "Please include an '@' in the email address"

        tooltip_text = self.get_tooltip_text(expected)

        print("Tooltip Found:", tooltip_text)

        self.assertIsNotNone(
            tooltip_text,
            f"Tooltip not found! Expected part: {expected}"
        )


    # ============================
    # TC-SI-001 valid email
    # ============================
    def test_001_sign_in(self):
        email = TEST_CREDENTIALS.get("valid_email")
        password = TEST_CREDENTIALS.get("valid_password")

        if not email or not password:
            self.fail("Missing credentials in config.py")

        self.ensure_sign_in_page()

        # Email
        ElementHelpers.safe_send_keys(
            self.driver,
            [(AppiumBy.XPATH, "//android.widget.EditText[contains(@hint,'Email')]")],
            email
        )
        AuthHelpers.submit_login(self.driver)

        # Password
        ElementHelpers.safe_send_keys(
            self.driver,
            [(AppiumBy.XPATH, "//android.widget.EditText[contains(@hint,'Password')]")],
            password
        )
        AuthHelpers.submit_login(self.driver)
        time.sleep(4)

        title = self.get_title("Dashboard")
        print("Dashboard:", title)
        self.assertIsNotNone(title, "Dashboard title not visible.")

    # ============================
    # Navigation Test Builder
    # ============================
    def navigate_and_verify(self, click_func, title_name):
        AuthHelpers.click_nav_bar(self.driver)
        click_func(self.driver)
        time.sleep(3)
        title = self.get_title(title_name)
        print(f"{title_name} Title:", title)
        self.assertIsNotNone(title, f"{title_name} title not found")

    # ============================
    # TC-SI-002 → TC-SI-011
    # ============================
    def test_002_properties(self):
        self.navigate_and_verify(AuthHelpers.click_properties, "Properties")

    def test_003_violations(self):
        self.navigate_and_verify(AuthHelpers.click_violations, "Violations")

    def test_004_non_compliant(self):
        self.navigate_and_verify(AuthHelpers.click_non_compliant, "Non-Compliant")

    def test_005_contracts(self):
        self.navigate_and_verify(AuthHelpers.click_contracts, "Contracts")

    def test_006_marketplace(self):
        self.navigate_and_verify(AuthHelpers.click_marketplace, "Marketplace")

    def test_007_payment_history(self):
        self.navigate_and_verify(AuthHelpers.click_payment_history, "Payment History")

    def test_008_job_filing(self):
        self.navigate_and_verify(AuthHelpers.click_job_filling, "Job Filing")

    def test_009_qompligov(self):
        self.navigate_and_verify(AuthHelpers.click_qompligov_ai, "QompliGov AI")

    def test_010_settings(self):
        self.navigate_and_verify(AuthHelpers.click_setting, "Settings")

    # ============================
    # Logout
    # ============================
    def test_011_logout(self):
        AuthHelpers.click_nav_bar(self.driver)
        AuthHelpers.logout(self.driver)
        time.sleep(2)
        self.assertTrue(self.ensure_sign_in_page(), "Sign-in screen not shown after logout.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
