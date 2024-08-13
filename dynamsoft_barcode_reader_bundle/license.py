if __package__ or "." in __name__:
    from . import _DynamsoftLicense
else:
    import _DynamsoftLicense
from typing import Tuple

class LicenseManager(object):
    thisown = property(
        lambda self: self.this.own(),
        lambda self, value: self.this.own(value),
        doc="The membership flag",
    )

    @staticmethod
    def init_license(license: str) -> Tuple[int, str]:
        return _DynamsoftLicense.CLicenseManager_InitLicense(license)

    @staticmethod
    def set_device_friendly_name(name: str) -> Tuple[int, str]:
        return _DynamsoftLicense.CLicenseManager_SetDeviceFriendlyName(name)

    @staticmethod
    def set_max_concurrent_instance_count(count_for_this_device: int) -> Tuple[int, str]:
        return _DynamsoftLicense.CLicenseManager_SetMaxConcurrentInstanceCount(
            count_for_this_device
        )

    @staticmethod
    def get_device_uuid(uuid_generation_method: int) -> Tuple[int, str, str]:
        return _DynamsoftLicense.CLicenseManager_GetDeviceUUID(uuid_generation_method)

    @staticmethod
    def set_license_cache_path(directory_path: str) -> Tuple[int, str]:
        return _DynamsoftLicense.CLicenseManager_SetLicenseCachePath(directory_path)

    def __init__(self):
        _DynamsoftLicense.CLicenseManager_init(
            self, _DynamsoftLicense.new_CLicenseManager()
        )

    __destroy__ = _DynamsoftLicense.delete_CLicenseManager


_DynamsoftLicense.CLicenseManager_register(LicenseManager)


class LicenseModule(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        return _DynamsoftLicense.CLicenseModule_GetVersion()

    def __init__(self):
        _DynamsoftLicense.CLicenseModule_init(
            self, _DynamsoftLicense.new_CLicenseModule()
        )

    __destroy__ = _DynamsoftLicense.delete_CLicenseModule


_DynamsoftLicense.CLicenseModule_register(LicenseModule)
