from appium.options.android import UiAutomator2Options
import os

# Appium Server Configuration
APPIUM_SERVER_URL = os.getenv("APPIUM_SERVER_URL", "http://127.0.0.1:4723")
# App Configuration
APP_PACKAGE = os.getenv("APP_PACKAGE", "com.qompli.app")
APP_ACTIVITY = os.getenv("APP_ACTIVITY", "com.qompli.app.MainActivity")
# Wait Timeouts (in seconds)
WAIT_TIMEOUT = int(os.getenv("WAIT_TIMEOUT", "10"))
SHORT_WAIT = int(os.getenv("SHORT_WAIT", "2"))
LONG_WAIT = int(os.getenv("LONG_WAIT", "5"))

# Test Credentials
TEST_CREDENTIALS = {
    "valid_email": os.getenv("TEST_USER_EMAIL", "tayyabuserios4@yopmail.com"),
    "valid_password": os.getenv("TEST_USER_PASSWORD", "Alpha789@tay@"),
    "invalid_email": os.getenv("TEST_USER_INVALID_EMAIL", "wrong@example.com"),
    "invalid_password": os.getenv("TEST_USER_INVALID_PASSWORD", "Wrong123!"),
    "malformed_email": os.getenv("TEST_USER_MALFORMED_EMAIL", "user1@qompliai"),
    "valid_otp": os.getenv("TEST_USER_OTP", "123456"),
}

# Android Capabilities
def get_android_options():
    options = UiAutomator2Options()
    options.platform_name = os.getenv("APPIUM_PLATFORM_NAME", "Android")
    options.device_name = os.getenv("APPIUM_DEVICE_NAME", "vivo 1907_19")
    options.platform_version = os.getenv("APPIUM_PLATFORM_VERSION", "12.0")
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.automation_name = os.getenv("APPIUM_AUTOMATION_NAME", "UiAutomator2")
    options.no_reset = os.getenv("APPIUM_NO_RESET", "true").lower() == "true"
    options.full_reset = os.getenv("APPIUM_FULL_RESET", "false").lower() == "true"
    options.new_command_timeout = int(os.getenv("APPIUM_NEW_COMMAND_TIMEOUT", "300"))
    options.auto_grant_permissions = os.getenv("APPIUM_AUTO_GRANT_PERMISSIONS", "true").lower() == "true"

    return options

