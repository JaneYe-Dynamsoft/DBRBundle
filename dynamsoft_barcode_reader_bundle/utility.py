if __package__ or "." in __name__:
    from .cvr import *
else:
    from cvr import *
if __package__ or "." in __name__:
    from .core import *
else:
    from core import *

if __package__ or "." in __name__:
    from . import _DynamsoftUtility
else:
    import _DynamsoftUtility


from abc import ABC, abstractmethod
from typing import List, Tuple


class UtilityModule(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        return _DynamsoftUtility.CUtilityModule_GetVersion()

    def __init__(self):
        _DynamsoftUtility.CUtilityModule_init(
            self, _DynamsoftUtility.new_CUtilityModule()
        )

    __destroy__ = _DynamsoftUtility.delete_CUtilityModule


_DynamsoftUtility.CUtilityModule_register(UtilityModule)


class MultiFrameResultCrossFilter(CapturedResultFilter):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftUtility.CMultiFrameResultCrossFilter_init(
            self, _DynamsoftUtility.new_CMultiFrameResultCrossFilter()
        )

    __destroy__ = _DynamsoftUtility.delete_CMultiFrameResultCrossFilter

    def enable_result_cross_verification(
        self, result_item_types: int, enabled: bool
    ) -> None:
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_EnableResultCrossVerification(
            self, result_item_types, enabled
        )

    def is_result_cross_verification_enabled(self, type: int) -> bool:
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_IsResultCrossVerificationEnabled(
            self, type
        )

    def enable_result_deduplication(self, result_item_types: int, enabled: bool) -> None:
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_EnableResultDeduplication(
            self, result_item_types, enabled
        )

    def is_result_deduplication_enabled(self, type: int) -> bool:
        return (
            _DynamsoftUtility.CMultiFrameResultCrossFilter_IsResultDeduplicationEnabled(
                self, type
            )
        )

    def set_duplicate_forget_time(self, result_item_types: int, time: int) -> None:
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_SetDuplicateForgetTime(
            self, result_item_types, time
        )

    def get_duplicate_forget_time(self, type: int) -> int:
        return _DynamsoftUtility.CMultiFrameResultCrossFilter_GetDuplicateForgetTime(
            self, type
        )


_DynamsoftUtility.CMultiFrameResultCrossFilter_register(MultiFrameResultCrossFilter)


class ProactiveImageSourceAdapter(ImageSourceAdapter, ABC):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftUtility.CMultiFrameResultCrossFilter_init(
            self, _DynamsoftUtility.new_CProactiveImageSourceAdapter(self)
        )

    __destroy__ = _DynamsoftUtility.delete_CProactiveImageSourceAdapter

    @abstractmethod
    def _fetch_image():
        pass

    def has_next_image_to_fetch(self) -> bool:
        return _DynamsoftUtility.CProactiveImageSourceAdapter_HasNextImageToFetch(self)

    def set_image_fetch_interval(self, milliseconds: int) -> None:
        return _DynamsoftUtility.CProactiveImageSourceAdapter_SetImageFetchInterval(
            self, milliseconds
        )

    def get_image_fetch_interval(self) -> int:
        return _DynamsoftUtility.CProactiveImageSourceAdapter_GetImageFetchInterval(
            self
        )

    def start_fetching(self) -> None:
        return _DynamsoftUtility.CProactiveImageSourceAdapter_StartFetching(self)

    def stop_fetching(self) -> None:
        return _DynamsoftUtility.CProactiveImageSourceAdapter_StopFetching(self)


_DynamsoftUtility.CProactiveImageSourceAdapter_register(ProactiveImageSourceAdapter)


class DirectoryFetcher(ProactiveImageSourceAdapter):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftUtility.CDirectoryFetcher_init(
            self, _DynamsoftUtility.new_CDirectoryFetcher()
        )

    __destroy__ = _DynamsoftUtility.delete_CDirectoryFetcher

    def _fetch_image():
        pass

    def set_directory(self, *args) -> Tuple[int, str]:
        return _DynamsoftUtility.CDirectoryFetcher_SetDirectory(self, *args)

    def set_pdf_reading_parameter(self, para: PDFReadingParameter) -> Tuple[int, str]:
        return _DynamsoftUtility.CDirectoryFetcher_SetPDFReadingParameter(self, para)

    def has_next_image_to_fetch(self) -> bool:
        return _DynamsoftUtility.CDirectoryFetcher_HasNextImageToFetch(self)

    def set_pages(self, pages: List[int]) -> Tuple[int, str]:
        return _DynamsoftUtility.CDirectoryFetcher_SetPages(self, pages, len(pages))


_DynamsoftUtility.CDirectoryFetcher_register(DirectoryFetcher)


class FileFetcher(ImageSourceAdapter):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftUtility.CFileFetcher_init(self, _DynamsoftUtility.new_CFileFetcher())

    __destroy__ = _DynamsoftUtility.delete_CFileFetcher

    def set_file(self, *args) -> Tuple[int, str]:
        return _DynamsoftUtility.CFileFetcher_SetFile(self, *args)

    def set_pdf_reading_parameter(self, para: PDFReadingParameter) -> Tuple[int, str]:
        return _DynamsoftUtility.CFileFetcher_SetPDFReadingParameter(self, para)

    def has_next_image_to_fetch(self) -> bool:
        return _DynamsoftUtility.CFileFetcher_HasNextImageToFetch(self)

    def get_image(self) -> ImageData:
        return _DynamsoftUtility.CFileFetcher_GetImage(self)

    def set_pages(self, pages: List[int]) -> Tuple[int, str]:
        return _DynamsoftUtility.CFileFetcher_SetPages(self, pages, len(pages))


_DynamsoftUtility.CFileFetcher_register(FileFetcher)


class ImageManager(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def save_to_file(
        self, image_data: ImageData, path: str, overwrite: bool = True
    ) -> Tuple[int, str]:
        return _DynamsoftUtility.CImageManager_SaveToFile(
            self, image_data, path, overwrite
        )

    def draw_on_image(self, *args):
        return _DynamsoftUtility.CImageManager_DrawOnImage(self, *args)

    def __init__(self):
        _DynamsoftUtility.CImageManager_init(
            self, _DynamsoftUtility.new_CImageManager()
        )

    __destroy__ = _DynamsoftUtility.delete_CImageManager


_DynamsoftUtility.CImageManager_register(ImageManager)
