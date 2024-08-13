if __package__ or "." in __name__:
    from .core import *
else:
    from core import *

if __package__ or "." in __name__:
    from . import _DynamsoftCaptureVisionRouter
else:
    import _DynamsoftCaptureVisionRouter

from abc import ABC, abstractmethod
from enum import Enum, IntEnum
from typing import Tuple, List


class EnumPresetTemplate(Enum):
    PT_DEFAULT = _DynamsoftCaptureVisionRouter.getPT_DEFAULT()
    PT_READ_BARCODES = _DynamsoftCaptureVisionRouter.getPT_READ_BARCODES()
    PT_RECOGNIZE_TEXT_LINES = _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_TEXT_LINES()
    PT_DETECT_DOCUMENT_BOUNDARIES = (
        _DynamsoftCaptureVisionRouter.getPT_DETECT_DOCUMENT_BOUNDARIES()
    )
    PT_DETECT_AND_NORMALIZE_DOCUMENT = (
        _DynamsoftCaptureVisionRouter.getPT_DETECT_AND_NORMALIZE_DOCUMENT()
    )
    PT_NORMALIZE_DOCUMENT = _DynamsoftCaptureVisionRouter.getPT_NORMALIZE_DOCUMENT()
    PT_READ_BARCODES_SPEED_FIRST = (
        _DynamsoftCaptureVisionRouter.getPT_READ_BARCODES_SPEED_FIRST()
    )
    PT_READ_BARCODES_READ_RATE_FIRST = (
        _DynamsoftCaptureVisionRouter.getPT_READ_BARCODES_READ_RATE_FIRST()
    )
    PT_READ_SINGLE_BARCODE = _DynamsoftCaptureVisionRouter.getPT_READ_SINGLE_BARCODE()
    PT_RECOGNIZE_NUMBERS = _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_NUMBERS()
    PT_RECOGNIZE_LETTERS = _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_LETTERS()
    PT_RECOGNIZE_NUMBERS_AND_LETTERS = (
        _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_NUMBERS_AND_LETTERS()
    )
    PT_RECOGNIZE_NUMBERS_AND_UPPERCASE_LETTERS = (
        _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_NUMBERS_AND_UPPERCASE_LETTERS()
    )
    PT_RECOGNIZE_UPPERCASE_LETTERS = (
        _DynamsoftCaptureVisionRouter.getPT_RECOGNIZE_UPPERCASE_LETTERS()
    )


class EnumCaptureState(IntEnum):
    CS_STARTED = _DynamsoftCaptureVisionRouter.CS_STARTED
    CS_STOPPED = _DynamsoftCaptureVisionRouter.CS_STOPPED
    CS_PAUSED = _DynamsoftCaptureVisionRouter.CS_PAUSED
    CS_RESUMED = _DynamsoftCaptureVisionRouter.CS_RESUMED


class EnumImageSourceState(IntEnum):
    ISS_BUFFER_EMPTY = _DynamsoftCaptureVisionRouter.ISS_BUFFER_EMPTY
    ISS_EXHAUSTED = _DynamsoftCaptureVisionRouter.ISS_EXHAUSTED


class SimplifiedCaptureVisionSettings(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    captured_result_item_types = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_capturedResultItemTypes_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_capturedResultItemTypes_set,
    )
    roi = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_roi_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_roi_set,
    )
    roi_measured_in_percentage = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_roiMeasuredInPercentage_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_roiMeasuredInPercentage_set,
    )
    max_parallel_tasks = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_maxParallelTasks_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_maxParallelTasks_set,
    )
    timeout = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_timeout_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_timeout_set,
    )
    barcode_settings = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_barcodeSettings_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_barcodeSettings_set,
    )
    label_settings = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_labelSettings_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_labelSettings_set,
    )
    min_image_capture_interval = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_minImageCaptureInterval_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_minImageCaptureInterval_set,
    )
    document_settings = property(
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_documentSettings_get,
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_documentSettings_set,
    )

    def __init__(self):
        _DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_init(
            self, _DynamsoftCaptureVisionRouter.new_SimplifiedCaptureVisionSettings()
        )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_SimplifiedCaptureVisionSettings


_DynamsoftCaptureVisionRouter.SimplifiedCaptureVisionSettings_register(
    SimplifiedCaptureVisionSettings
)


class CapturedResult(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftCaptureVisionRouter.CCapturedResult_Release

    def get_original_image_hash_id(self) -> str:
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetOriginalImageHashId(
            self
        )

    def get_original_image_tag(self) -> ImageTag:
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetOriginalImageTag(self)

    def get_rotation_transform_matrix(self) -> List[float]:
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetRotationTransformMatrix(
            self
        )

    def get_items(self) -> List[CapturedResultItem]:
        list = []
        count = _DynamsoftCaptureVisionRouter.CCapturedResult_GetItemsCount(self)
        for i in range(count):
            list.append(_DynamsoftCaptureVisionRouter.CCapturedResult_GetItem(self, i))
        return list

    def __getitem__(self, index: int) -> CapturedResultItem:
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetItem(self, index)

    def get_error_code(self) -> int:
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetErrorCode(self)

    def get_error_string(self) -> str:
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetErrorString(self)

    def get_decoded_barcodes_result(self) -> "DecodedBarcodesResult":
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetDecodedBarcodesResult(
            self
        )

    def get_recognized_text_lines_result(self) -> "RecognizedTextLinesResult":
        return (
            _DynamsoftCaptureVisionRouter.CCapturedResult_GetRecognizedTextLinesResult(
                self
            )
        )

    def get_detected_quads_result(self) -> "DetectedQuadsResult":
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetDetectedQuadsResult(
            self
        )

    def get_normalized_images_result(self) -> "NormalizedImagesResult":
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetNormalizedImagesResult(
            self
        )

    def get_parsed_result(self) -> "ParsedResult":
        return _DynamsoftCaptureVisionRouter.CCapturedResult_GetParsedResult(self)


_DynamsoftCaptureVisionRouter.CCapturedResult_register(CapturedResult)


class CapturedResultReceiver(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
         if type(self) is CapturedResultReceiver:
            raise TypeError("Cannot create an instance of an abstract class.")
         else:
            _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
                self, _DynamsoftCaptureVisionRouter.new_CCapturedResultReceiver(self)
            )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCapturedResultReceiver

    def get_name(self) -> str:
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_GetName(self)

    def set_name(self, name: str) -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_SetName(self, name)

    def on_captured_result_received(self, result: CapturedResult) -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnCapturedResultReceived(
            self, result
        )

    def on_original_image_result_received(
        self, result: OriginalImageResultItem
    ) -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnOriginalImageResultReceived(
            self, result
        )

    def on_decoded_barcodes_received(self, result: "DecodedBarcodesResult") -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnDecodedBarcodesReceived(
            self, result
        )

    def on_recognized_text_lines_received(
        self, result: "RecognizedTextLinesResult"
    ) -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnRecognizedTextLinesReceived(
            self, result
        )

    def on_detected_quads_received(self, result: "DetectedQuadsResult") -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnDetectedQuadsReceived(
            self, result
        )

    def on_normalized_images_received(self, result: "NormalizedImagesResult") -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnNormalizedImagesReceived(
            self, result
        )

    def on_parsed_results_received(self, result: "ParsedResult") -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultReceiver_OnParsedResultsReceived(
            self, result
        )


_DynamsoftCaptureVisionRouter.CCapturedResultReceiver_register(CapturedResultReceiver)


class CapturedResultFilter(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        if type(self) is CapturedResultFilter:
            raise TypeError("Cannot create an instance of an abstract class.")
        else:
            _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
                self, _DynamsoftCaptureVisionRouter.new_CCapturedResultFilter(self)
            )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCapturedResultFilter

    def get_name(self) -> str:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_GetName(self)

    def set_name(self, name: str) -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_SetName(self, name)

    def on_original_image_result_received(
        self, result: OriginalImageResultItem
    ) -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnOriginalImageResultReceived(
            self, result
        )

    def on_decoded_barcodes_received(self, result: "DecodedBarcodesResult") -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnDecodedBarcodesReceived(
            self, result
        )

    def on_recognized_text_lines_received(
        self, result: "RecognizedTextLinesResult"
    ) -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnRecognizedTextLinesReceived(
            self, result
        )

    def on_detected_quads_received(self, result: "DetectedQuadsResult") -> None:
        return (
            _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnDetectedQuadsReceived(
                self, result
            )
        )

    def on_normalized_images_received(self, result: "NormalizedImagesResult") -> None:
        return _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnNormalizedImagesReceived(
            self, result
        )

    def on_parsed_results_received(self, result: "ParsedResult") -> None:
        return (
            _DynamsoftCaptureVisionRouter.CCapturedResultFilter_OnParsedResultsReceived(
                self, result
            )
        )


_DynamsoftCaptureVisionRouter.CCapturedResultFilter_register(CapturedResultFilter)


class CaptureStateListener(ABC):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
            self, _DynamsoftCaptureVisionRouter.new_CCaptureStateListener(self)
        )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCaptureStateListener

    @abstractmethod
    def on_capture_state_changed(self, state: int) -> None:
        pass


_DynamsoftCaptureVisionRouter.CCaptureStateListener_register(CaptureStateListener)


class ImageSourceStateListener(ABC):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
            self, _DynamsoftCaptureVisionRouter.new_CImageSourceStateListener(self)
        )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CImageSourceStateListener

    @abstractmethod
    def on_image_source_state_received(self, state: int) -> None:
        pass


_DynamsoftCaptureVisionRouter.CImageSourceStateListener_register(
    ImageSourceStateListener
)


class BufferedItemsManager:
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CBufferedItemsManager

    def set_max_buffered_items_count(self, count: int) -> None:
        return _DynamsoftCaptureVisionRouter.CBufferedItemsManager_SetMaxBufferedItems(
            self, count
        )

    def get_max_buffered_items_count(self) -> int:
        return _DynamsoftCaptureVisionRouter.CBufferedItemsManager_GetMaxBufferedItems(
            self
        )

    def get_buffered_character_item_set(self) -> "BufferedCharacterItemSet":
        return _DynamsoftCaptureVisionRouter.CBufferedItemsManager_GetBufferedCharacterItemSet(
            self
        )


_DynamsoftCaptureVisionRouter.CBufferedItemsManager_register(BufferedItemsManager)


class CaptureVisionRouter(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_init(
            self, _DynamsoftCaptureVisionRouter.new_CCaptureVisionRouter()
        )
        self._input = None

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCaptureVisionRouter

    def init_settings(self, content: str) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_InitSettings(
            self, content
        )

    def init_settings_from_file(self, file_path: str) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_InitSettingsFromFile(
            self, file_path
        )

    def output_settings(self, template_name: str) -> Tuple[int, str, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_OutputSettings(
            self, template_name
        )

    def output_settings_to_file(
        self, template_name: str, file_path: str
    ) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_OutputSettingsToFile(
            self, template_name, file_path
        )

    def get_simplified_settings(
        self, template_name: str
    ) -> Tuple[int, str, SimplifiedCaptureVisionSettings]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_GetSimplifiedSettings(
            self, template_name
        )

    def update_settings(
        self, template_name: str, settings: SimplifiedCaptureVisionSettings
    ) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_UpdateSettings(
            self, template_name, settings
        )

    def reset_settings(self) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_ResetSettings(self)

    def capture(self, *args) -> CapturedResult:
        ret = _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_Capture(self, *args)
        return ret

    def set_input(self, adapter: ImageSourceAdapter) -> Tuple[int, str]:
        ret = _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_SetInput(self, adapter)
        if ret[0] == 0:
            self._input = adapter
        return ret

    def get_input(self) -> ImageSourceAdapter:
        return self._input

    def add_image_source_state_listener(
        self, listener: ImageSourceStateListener
    ) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_AddImageSourceStateListener(
            self, listener
        )

    def remove_image_source_state_listener(
        self, listener: ImageSourceStateListener
    ) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_RemoveImageSourceStateListener(
            self, listener
        )

    def add_result_receiver(self, receiver: CapturedResultReceiver) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_AddResultReceiver(
            self, receiver
        )

    def remove_result_receiver(
        self, receiver: CapturedResultReceiver
    ) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_RemoveResultReceiver(
            self, receiver
        )

    def add_result_filter(self, filter: CapturedResultFilter) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_AddResultFilter(
            self, filter
        )

    def remove_result_filter(self, filter: CapturedResultFilter) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_RemoveResultFilter(
            self, filter
        )

    def add_capture_state_listener(
        self, listener: CaptureStateListener
    ) -> Tuple[int, str]:
        return (
            _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_AddCaptureStateListener(
                self, listener
            )
        )

    def remove_capture_state_listener(
        self, listener: CaptureStateListener
    ) -> Tuple[int, str]:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_RemoveCaptureStateListener(
            self, listener
        )

    def start_capturing(
        self, template_name: str = "", wait_for_thread_exit: bool = False
    ) -> Tuple[int, str]:
        ret = _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_StartCapturing(
            self, template_name, wait_for_thread_exit
        )
        return ret

    def stop_capturing(
        self, wait_for_remaining_tasks: bool = True, wait_for_thread_exit: bool = True
    ) -> None:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_StopCapturing(
            self, wait_for_remaining_tasks, wait_for_thread_exit
        )

    def pause_capturing(self) -> None:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_PauseCapturing(self)

    def resume_capturing(self) -> None:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_ResumeCapturing(self)

    def get_buffered_items_manager(self) -> BufferedItemsManager:
        return (
            _DynamsoftCaptureVisionRouter.CCaptureVisionRouter_GetBufferedItemsManager(
                self
            )
        )


_DynamsoftCaptureVisionRouter.CCaptureVisionRouter_register(CaptureVisionRouter)


class CaptureVisionRouterModule(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        return _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_GetVersion()

    def __init__(self):
        _DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_init(
            self, _DynamsoftCaptureVisionRouter.new_CCaptureVisionRouterModule()
        )

    __destroy__ = _DynamsoftCaptureVisionRouter.delete_CCaptureVisionRouterModule


_DynamsoftCaptureVisionRouter.CCaptureVisionRouterModule_register(
    CaptureVisionRouterModule
)
