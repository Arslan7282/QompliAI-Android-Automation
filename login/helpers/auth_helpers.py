import time
from asyncio import timeout
from typing import List
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from .element_helpers import ElementHelpers


class AuthHelpers:
    """Helper class for authentication-related operations"""

    EMAIL_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'Email')]"),
        (AppiumBy.XPATH, "//android.widget.EditText[1]"),
        (AppiumBy.ID, "com.qompli.app:id/input_email"),
    ]

    PASSWORD_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.EditText[contains(@hint, 'Password')]"),
        (AppiumBy.XPATH, "//android.widget.EditText[2]"),
        (AppiumBy.ID, "com.qompli.app:id/input_password"),
    ]

    SIGN_IN_BUTTON_SELECTORS = [
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign In'])[2]"),
        (AppiumBy.XPATH, "//android.widget.TextView[@text='Sign In']"),
        (AppiumBy.XPATH, "//*[@text='Sign In']"),
        (AppiumBy.ID, "com.qompli.app:id/btn_sign_in"),
    ]

    NAV_BAR_BUTTON_SELECTORS = [
        (AppiumBy.XPATH, "//android.view.View[@resource-id='root']/android.view.View[2]/android.widget.Button"),
        (AppiumBy.XPATH, "(//android.view.View[@resource-id='root']//android.widget.Button)[1]"),
        (AppiumBy.XPATH, "//android.view.View[@resource-id='root']//android.widget.Button"),
        (AppiumBy.XPATH, "//*[@resource-id='root']//android.widget.Button"),
    ]

    SIGN_OUT_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Sign Out']"),
        (AppiumBy.XPATH, "//android.widget.Button[contains(@text, 'Sign Out')]"),
        (AppiumBy.XPATH, "//*[@text='Sign Out' and @class='android.widget.Button']"),
        (AppiumBy.XPATH, "//*[@text='Sign Out']"),
        (AppiumBy.XPATH, "(//android.widget.Button[@text='Sign Out'])[1]"),
    ]

    NAV_PROPERTY_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Properties']"),
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Properties'])[1]"),
    ]

    NAV_INSPECTIONS_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Inspections']"),
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Inspections'])[1]"),
    ]

    NAV_VIOLATIONS_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Violations']"),
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Violations'])[1]"),
    ]

    NAV_NON_COMPLIANT_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Non-Compliant']"),
        (AppiumBy.XPATH, "//android.widget.TextView[@text='Non-Compliant']"),
    ]

    NAV_CONTRACTS_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Contracts']"),
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Contracts'])[1]"),
    ]

    NAV_MARKETPLACE_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Marketplace']"),
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Marketplace'])[1]"),
    ]

    NAV_PAYMENT_HISTORY_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Payment History']"),
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Payment History'])[1]"),
    ]

    NAV_JOB_FILLING_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Job Filing']"),
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='Job Filing'])[1]"),
    ]

    NAV_QOMPLIGOV_AI_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='QompliGov AI']"),
        (AppiumBy.XPATH, "(//android.widget.TextView[@text='QompliGov AI'])[1]"),
    ]

    NAV_SETTINGS_SELECTORS = [
        (AppiumBy.XPATH, "//android.widget.Button[@text='Settings']"),
        (AppiumBy.XPATH, "//android.widget.TextView[@text='Qompliai']"),
    ]

    SIGN_IN_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='Sign In']")
    # (AppiumBy.XPATH, "//android.widget.TextView[@text='Sign In']"),
    PASSWORD_TOGGLE = (AppiumBy.ID, "com.qompli.app:id/toggle_password")
    SIGN_UP_LINK = (AppiumBy.ID, "com.qompli.app:id/btn_sign_up")
    DASHBOARD = (AppiumBy.XPATH, "//android.widget.TextView[@text='Dashboard']")
    OTP_INPUT = (AppiumBy.ID, "com.qompli.app:id/input_otp")
    OTP_SUBMIT = (AppiumBy.ID, "com.qompli.app:id/btn_submit_otp")
    LOGOUT_BUTTON = (AppiumBy.ID, "com.qompli.app:id/btn_logout")


    def fill_login_form(driver: WebDriver, email: str, password: str, remember: bool = False) -> bool:
        """Fill the login form with email and password"""
        try:
            email: ElementHelpers.safe_send_keys(driver, AuthHelpers.EMAIL_SELECTORS, email)
            time.sleep(0.5)
            password: ElementHelpers.safe_send_keys(driver, AuthHelpers.PASSWORD_SELECTORS, password)
            time.sleep(0.5)
            # Optional: remember me
            if remember:
                remember_checkbox = (AppiumBy.ID, "com.qompli.app:id/checkbox_remember")
                if ElementHelpers.element_exists(driver, [remember_checkbox], timeout=2):
                    ElementHelpers.safe_click(driver, [remember_checkbox])
            return True
        except Exception as e:
            print(f"⚠ Error filling login form: {e}")
            return False

    @staticmethod
    def submit_login(driver: WebDriver) -> bool:
        """Click the Sign In button"""
        return ElementHelpers.safe_click(driver, AuthHelpers.SIGN_IN_BUTTON_SELECTORS)

    def click_nav_bar(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_BAR_BUTTON_SELECTORS)

    def click_properties(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_PROPERTY_SELECTORS)

    def click_inspection(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_INSPECTIONS_SELECTORS)

    def click_violations(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_VIOLATIONS_SELECTORS)

    def click_non_compliant(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_NON_COMPLIANT_SELECTORS)

    def click_contracts(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_CONTRACTS_SELECTORS)

    def click_marketplace(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_MARKETPLACE_SELECTORS)

    def click_payment_history(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_PAYMENT_HISTORY_SELECTORS)

    def click_job_filling(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_JOB_FILLING_SELECTORS)

    def click_qompligov_ai(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_QOMPLIGOV_AI_SELECTORS)

    def click_setting(driver: WebDriver) -> bool:
        return ElementHelpers.safe_click(driver, AuthHelpers.NAV_SETTINGS_SELECTORS)

    @staticmethod
    def check_dashboard(driver: WebDriver) -> bool:
        """Check if dashboard is visible"""
        return ElementHelpers.element_exists(driver, AuthHelpers.DASHBOARD)

    @staticmethod
    def enter_otp(driver: WebDriver, otp: str) -> bool:
        """Enter OTP code"""
        return ElementHelpers.safe_send_keys(driver, [AuthHelpers.OTP_INPUT], otp)

    @staticmethod
    def submit_otp(driver: WebDriver) -> bool:
        """Submit OTP code"""
        return ElementHelpers.safe_click(driver, [AuthHelpers.OTP_SUBMIT])

    @staticmethod
    def check_error_message(driver: WebDriver, error_texts: List[str], timeout: int = 5) -> bool:
        """Check if any error message is visible"""
        for text in error_texts:
            selector = (AppiumBy.XPATH, f"//*[contains(@text, '{text}')]")
            if ElementHelpers.element_exists(driver, [selector], timeout):
                return True
        return False

    @staticmethod
    def is_button_enabled(driver: WebDriver, selector: tuple, timeout: int = 5) -> bool:
        """Check if a button is enabled"""
        try:
            element = ElementHelpers.wait_for_element(driver, [selector], timeout)
            return element.get_attribute("enabled") == "true"
        except Exception:
            return False

    @staticmethod
    def logout(driver: WebDriver) -> bool:
        """Logout from the app"""
        return ElementHelpers.safe_click(driver, AuthHelpers.SIGN_OUT_SELECTORS)

    @staticmethod
    def is_password_visible(driver: WebDriver) -> bool:
        """Check if password is visible (not masked)"""
        try:
            element = ElementHelpers.wait_for_element(driver, [AuthHelpers.PASSWORD_SELECTOR])
            return len(element.text) > 0
        except Exception:
            return False

    @staticmethod
    def toggle_password_visibility(driver: WebDriver) -> bool:
        """Toggle password visibility"""
        return ElementHelpers.safe_click(driver, [AuthHelpers.PASSWORD_TOGGLE])

    @staticmethod
    def navigate_to_signup(driver: WebDriver) -> bool:
        """Navigate to Sign Up page"""
        return ElementHelpers.safe_click(driver, [AuthHelpers.SIGN_UP_LINK])
