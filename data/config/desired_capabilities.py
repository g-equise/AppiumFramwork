from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from data.config import config


def get_desired_capabilities():
    desired_caps = {
        'platformName': 'Android',
        'deviceName': config.DEVICE_NAME,
        'app': config.APK_FILE_NAME,
        'newCommandTimeout': 3600,
        'autoGrantPermissions': True,
        'androidInstallTimeout': 360000
    }

    return desired_caps


BROWSERSTACK_URL = 'http://hub-cloud.browserstack.com/wd/hub'


def get_desired_capabilities_bs():
    desired_cap = {

        "browserstack.user": "cloudx2",
        "browserstack.key": "oFJ8wxyBAvq1rYqvAqey",

        # Set URL of the application under test
        "app": "bs://7bfb42cb71a2054498c7f8f8198a1a95c368ca0f",

        # Specify device and os_version for testing
        "device": "Samsung Galaxy S10e",
        "os_version": "9.0",

        # Set other BrowserStack capabilities
        "project": "First Python project",
        "build": "Python Android",
        "name": "first_test",

        # Set location
        #'browserstack.gpsLocation': '- 34.6344903,-58.4494996'

    }

    return desired_cap


def get_desired_capabilities_bs_maps():
    desired_cap = {

        "browserstack.user": "cloudx2",
        "browserstack.key": "oFJ8wxyBAvq1rYqvAqey",

        # Set URL of the application under test
        "app": "bs://7bfb42cb71a2054498c7f8f8198a1a95c368ca0f",

        # Specify device and os_version for testing
        "device": "Samsung Galaxy S10e",
        "os_version": "9.0",

        # Set other BrowserStack capabilities
        "project": "First Python project",
        "build": "Python Android",
        "name": "first_test",

        # Set location
        'browserstack.gpsLocation': '- 34.6344903,-58.4494996'

    }

    return desired_cap
