import os

APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")


# os.getenv is a simple Python helper to read an environment variable from the current process.
APPIUM_CAPS = {
    "platformName": os.getenv("APPIUM_PLATFORM_NAME", "Android"),
    "platformVersion": os.getenv("APPIUM_PLATFORM_VERSION", "12"),
    "deviceName": os.getenv("APPIUM_DEVICE_NAME", "JFQO7PFEU44XBIIJ"),
    "automationName": os.getenv("APPIUM_AUTOMATION_NAME", "UiAutomator2"),
    "appPackage": os.getenv("APPIUM_APP_PACKAGE", "com.qompli.app"),
    "appActivity": os.getenv("APPIUM_APP_ACTIVITY", "com.qompli.app.MainActivity"),
    "newCommandTimeout": 300,
    "autoGrantPermissions": True,
}

VALID_EMAIL = os.getenv("TEST_USER_EMAIL", "tayyabuserios4@yopmail.com")
VALID_PASSWORD = os.getenv("TEST_USER_PASSWORD", "Alpha789@tay@")
INVALID_PASSWORD = os.getenv("TEST_USER_INVALID_PASSWORD", "WrongPass123!")

SELECTORS = {
    "email_input": os.getenv("EMAIL_INPUT_ID", "com.qompliai.mobile:id/input_email"),
    "password_input": os.getenv("PASSWORD_INPUT_ID", "com.qompliai.mobile:id/input_password"),
    "remember_me_toggle": os.getenv("REMEMBER_TOGGLE_ID", "com.qompliai.mobile:id/toggle_remember_me"),
    "sign_in_button": os.getenv("SIGN_IN_BUTTON_ID", "com.qompliai.mobile:id/btn_sign_in"),
    "forgot_password_button": os.getenv("FORGOT_PASSWORD_BUTTON_ID", "com.qompliai.mobile:id/btn_forgot_password"),
    "success_toast": os.getenv("SUCCESS_TOAST_XPATH", '//android.widget.Toast[@text="Login Successful"]'),
    "error_toast": os.getenv("ERROR_TOAST_XPATH", '//android.widget.Toast[@text="Invalid Credentials"]'),
    "email_error_label": os.getenv("EMAIL_ERROR_ID", "com.qompliai.mobile:id/error_email"),
    "password_error_label": os.getenv("PASSWORD_ERROR_ID", "com.qompliai.mobile:id/error_password"),
    "forgot_password_screen_id": os.getenv("FORGOT_SCREEN_ID", "com.qompliai.mobile:id/forgot_password_title"),
}

