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