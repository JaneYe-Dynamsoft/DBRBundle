import dynamsoft_image_processing
from dynamsoft_core import *
import dynamsoft_license

if __package__ or "." in __name__:
    from . import _DynamsoftBarcodeReader
else:
    import _DynamsoftBarcodeReader


from enum import Enum, IntEnum
from typing import List


class EnumBarcodeFormat(Enum):
    BF_NULL = _DynamsoftBarcodeReader.BF_NULL
    BF_ALL = _DynamsoftBarcodeReader.BF_ALL
    BF_DEFAULT = _DynamsoftBarcodeReader.BF_DEFAULT
    BF_ONED = _DynamsoftBarcodeReader.BF_ONED
    BF_GS1_DATABAR = _DynamsoftBarcodeReader.BF_GS1_DATABAR
    BF_CODE_39 = _DynamsoftBarcodeReader.BF_CODE_39
    BF_CODE_128 = _DynamsoftBarcodeReader.BF_CODE_128
    BF_CODE_93 = _DynamsoftBarcodeReader.BF_CODE_93
    BF_CODABAR = _DynamsoftBarcodeReader.BF_CODABAR
    BF_ITF = _DynamsoftBarcodeReader.BF_ITF
    BF_EAN_13 = _DynamsoftBarcodeReader.BF_EAN_13
    BF_EAN_8 = _DynamsoftBarcodeReader.BF_EAN_8
    BF_UPC_A = _DynamsoftBarcodeReader.BF_UPC_A
    BF_UPC_E = _DynamsoftBarcodeReader.BF_UPC_E
    BF_INDUSTRIAL_25 = _DynamsoftBarcodeReader.BF_INDUSTRIAL_25
    BF_CODE_39_EXTENDED = _DynamsoftBarcodeReader.BF_CODE_39_EXTENDED
    BF_GS1_DATABAR_OMNIDIRECTIONAL = (
        _DynamsoftBarcodeReader.BF_GS1_DATABAR_OMNIDIRECTIONAL
    )
    BF_GS1_DATABAR_TRUNCATED = _DynamsoftBarcodeReader.BF_GS1_DATABAR_TRUNCATED
    BF_GS1_DATABAR_STACKED = _DynamsoftBarcodeReader.BF_GS1_DATABAR_STACKED
    BF_GS1_DATABAR_STACKED_OMNIDIRECTIONAL = (
        _DynamsoftBarcodeReader.BF_GS1_DATABAR_STACKED_OMNIDIRECTIONAL
    )
    BF_GS1_DATABAR_EXPANDED = _DynamsoftBarcodeReader.BF_GS1_DATABAR_EXPANDED
    BF_GS1_DATABAR_EXPANDED_STACKED = (
        _DynamsoftBarcodeReader.BF_GS1_DATABAR_EXPANDED_STACKED
    )
    BF_GS1_DATABAR_LIMITED = _DynamsoftBarcodeReader.BF_GS1_DATABAR_LIMITED
    BF_PATCHCODE = _DynamsoftBarcodeReader.BF_PATCHCODE
    BF_CODE_32 = _DynamsoftBarcodeReader.BF_CODE_32
    BF_PDF417 = _DynamsoftBarcodeReader.BF_PDF417
    BF_QR_CODE = _DynamsoftBarcodeReader.BF_QR_CODE
    BF_DATAMATRIX = _DynamsoftBarcodeReader.BF_DATAMATRIX
    BF_AZTEC = _DynamsoftBarcodeReader.BF_AZTEC
    BF_MAXICODE = _DynamsoftBarcodeReader.BF_MAXICODE
    BF_MICRO_QR = _DynamsoftBarcodeReader.BF_MICRO_QR
    BF_MICRO_PDF417 = _DynamsoftBarcodeReader.BF_MICRO_PDF417
    BF_GS1_COMPOSITE = _DynamsoftBarcodeReader.BF_GS1_COMPOSITE
    BF_MSI_CODE = _DynamsoftBarcodeReader.BF_MSI_CODE
    BF_CODE_11 = _DynamsoftBarcodeReader.BF_CODE_11
    BF_TWO_DIGIT_ADD_ON = _DynamsoftBarcodeReader.BF_TWO_DIGIT_ADD_ON
    BF_FIVE_DIGIT_ADD_ON = _DynamsoftBarcodeReader.BF_FIVE_DIGIT_ADD_ON
    BF_MATRIX_25 = _DynamsoftBarcodeReader.BF_MATRIX_25
    BF_POSTALCODE = _DynamsoftBarcodeReader.BF_POSTALCODE
    BF_NONSTANDARD_BARCODE = _DynamsoftBarcodeReader.BF_NONSTANDARD_BARCODE
    BF_USPSINTELLIGENTMAIL = _DynamsoftBarcodeReader.BF_USPSINTELLIGENTMAIL
    BF_POSTNET = _DynamsoftBarcodeReader.BF_POSTNET
    BF_PLANET = _DynamsoftBarcodeReader.BF_PLANET
    BF_AUSTRALIANPOST = _DynamsoftBarcodeReader.BF_AUSTRALIANPOST
    BF_RM4SCC = _DynamsoftBarcodeReader.BF_RM4SCC
    BF_KIX = _DynamsoftBarcodeReader.BF_KIX
    BF_DOTCODE = _DynamsoftBarcodeReader.BF_DOTCODE
    BF_PHARMACODE_ONE_TRACK = _DynamsoftBarcodeReader.BF_PHARMACODE_ONE_TRACK
    BF_PHARMACODE_TWO_TRACK = _DynamsoftBarcodeReader.BF_PHARMACODE_TWO_TRACK
    BF_PHARMACODE = _DynamsoftBarcodeReader.BF_PHARMACODE


class EnumLocalizationMode(IntEnum):
    LM_AUTO = _DynamsoftBarcodeReader.LM_AUTO
    LM_CONNECTED_BLOCKS = _DynamsoftBarcodeReader.LM_CONNECTED_BLOCKS
    LM_STATISTICS = _DynamsoftBarcodeReader.LM_STATISTICS
    LM_LINES = _DynamsoftBarcodeReader.LM_LINES
    LM_SCAN_DIRECTLY = _DynamsoftBarcodeReader.LM_SCAN_DIRECTLY
    LM_STATISTICS_MARKS = _DynamsoftBarcodeReader.LM_STATISTICS_MARKS
    LM_STATISTICS_POSTAL_CODE = _DynamsoftBarcodeReader.LM_STATISTICS_POSTAL_CODE
    LM_CENTRE = _DynamsoftBarcodeReader.LM_CENTRE
    LM_ONED_FAST_SCAN = _DynamsoftBarcodeReader.LM_ONED_FAST_SCAN
    LM_REV = _DynamsoftBarcodeReader.LM_REV
    LM_SKIP = _DynamsoftBarcodeReader.LM_SKIP


class EnumDeblurMode(IntEnum):
    DM_DIRECT_BINARIZATION = _DynamsoftBarcodeReader.DM_DIRECT_BINARIZATION
    DM_THRESHOLD_BINARIZATION = _DynamsoftBarcodeReader.DM_THRESHOLD_BINARIZATION
    DM_GRAY_EQUALIZATION = _DynamsoftBarcodeReader.DM_GRAY_EQUALIZATION
    DM_SMOOTHING = _DynamsoftBarcodeReader.DM_SMOOTHING
    DM_MORPHING = _DynamsoftBarcodeReader.DM_MORPHING
    DM_DEEP_ANALYSIS = _DynamsoftBarcodeReader.DM_DEEP_ANALYSIS
    DM_SHARPENING = _DynamsoftBarcodeReader.DM_SHARPENING
    DM_BASED_ON_LOC_BIN = _DynamsoftBarcodeReader.DM_BASED_ON_LOC_BIN
    DM_SHARPENING_SMOOTHING = _DynamsoftBarcodeReader.DM_SHARPENING_SMOOTHING
    DM_REV = _DynamsoftBarcodeReader.DM_REV
    DM_SKIP = _DynamsoftBarcodeReader.DM_SKIP


class EnumQRCodeErrorCorrectionLevel(IntEnum):
    QRECL_ERROR_CORRECTION_H = _DynamsoftBarcodeReader.QRECL_ERROR_CORRECTION_H
    QRECL_ERROR_CORRECTION_L = _DynamsoftBarcodeReader.QRECL_ERROR_CORRECTION_L
    QRECL_ERROR_CORRECTION_M = _DynamsoftBarcodeReader.QRECL_ERROR_CORRECTION_M
    QRECL_ERROR_CORRECTION_Q = _DynamsoftBarcodeReader.QRECL_ERROR_CORRECTION_Q


class EnumExtendedBarcodeResultType(IntEnum):
    EBRT_STANDARD_RESULT = _DynamsoftBarcodeReader.EBRT_STANDARD_RESULT
    EBRT_CANDIDATE_RESULT = _DynamsoftBarcodeReader.EBRT_CANDIDATE_RESULT
    EBRT_PARTIAL_RESULT = _DynamsoftBarcodeReader.EBRT_PARTIAL_RESULT


class SimplifiedBarcodeReaderSettings(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    barcode_format_ids = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_barcodeFormatIds_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_barcodeFormatIds_set,
    )
    expected_barcodes_count = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_expectedBarcodesCount_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_expectedBarcodesCount_set,
    )
    grayscale_transformation_modes = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_grayscaleTransformationModes_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_grayscaleTransformationModes_set,
    )
    grayscale_enhancement_modes = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_grayscaleEnhancementModes_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_grayscaleEnhancementModes_set,
    )
    localization_modes = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_localizationModes_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_localizationModes_set,
    )
    deblur_modes = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_deblurModes_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_deblurModes_set,
    )
    min_result_confidence = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_minResultConfidence_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_minResultConfidence_set,
    )
    min_barcode_text_length = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_minBarcodeTextLength_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_minBarcodeTextLength_set,
    )
    barcode_text_regex_pattern = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_barcodeTextRegExPattern_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_barcodeTextRegExPattern_set,
    )
    max_threads_in_one_task = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_maxThreadsInOneTask_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_maxThreadsInOneTask_set,
    )
    scale_down_threshold = property(
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_scaleDownThreshold_get,
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_scaleDownThreshold_set,
    )

    def __init__(self):
        _DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_init(
            self, _DynamsoftBarcodeReader.new_SimplifiedBarcodeReaderSettings()
        )

    __destroy__ = _DynamsoftBarcodeReader.delete_SimplifiedBarcodeReaderSettings


_DynamsoftBarcodeReader.SimplifiedBarcodeReaderSettings_register(
    SimplifiedBarcodeReaderSettings
)


class BarcodeDetails(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    __destroy__ = _DynamsoftBarcodeReader.delete_CBarcodeDetails

    def __init__(self):
        _DynamsoftBarcodeReader.CBarcodeDetails_init(
            self, _DynamsoftBarcodeReader.new_CBarcodeDetails()
        )


_DynamsoftBarcodeReader.CBarcodeDetails_register(BarcodeDetails)


class OneDCodeDetails(BarcodeDetails):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self, *args):
        _DynamsoftBarcodeReader.COneDCodeDetails_init(
            self, _DynamsoftBarcodeReader.new_COneDCodeDetails(*args)
        )

    __destroy__ = _DynamsoftBarcodeReader.delete_COneDCodeDetails
    start_chars_bytes = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_startCharsBytes_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_startCharsBytes_set,
    )
    stop_chars_bytes = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_stopCharsBytes_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_stopCharsBytes_set,
    )
    check_digit_bytes = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_checkDigitBytes_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_checkDigitBytes_set,
    )
    start_pattern_range = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_startPatternRange_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_startPatternRange_set,
    )
    middle_pattern_range = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_middlePatternRange_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_middlePatternRange_set,
    )
    end_pattern_range = property(
        _DynamsoftBarcodeReader.COneDCodeDetails_endPatternRange_get,
        _DynamsoftBarcodeReader.COneDCodeDetails_endPatternRange_set,
    )


_DynamsoftBarcodeReader.COneDCodeDetails_register(OneDCodeDetails)


class QRCodeDetails(BarcodeDetails):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(
        self,
        rows: int = -1,
        columns: int = -1,
        error_correction_level: int = EnumQRCodeErrorCorrectionLevel.QRECL_ERROR_CORRECTION_H.value,
        version: int = -1,
        model: int = -1,
        mode: int = -1,
        page: int = -1,
        total_page: int = -1,
        parity_data: int = -1,
    ):
        _DynamsoftBarcodeReader.CQRCodeDetails_init(
            self,
            _DynamsoftBarcodeReader.new_CQRCodeDetails(
                rows,
                columns,
                error_correction_level,
                version,
                model,
                mode,
                page,
                total_page,
                parity_data,
            ),
        )

    __destroy__ = _DynamsoftBarcodeReader.delete_CQRCodeDetails
    rows = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_rows_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_rows_set,
    )
    columns = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_columns_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_columns_set,
    )
    error_correction_level = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_errorCorrectionLevel_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_errorCorrectionLevel_set,
    )
    version = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_version_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_version_set,
    )
    model = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_model_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_model_set,
    )
    mode = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_mode_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_mode_set,
    )
    page = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_page_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_page_set,
    )
    total_page = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_totalPage_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_totalPage_set,
    )
    parity_data = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_parityData_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_parityData_set,
    )
    data_mask_pattern = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_dataMaskPattern_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_dataMaskPattern_set,
    )
    codewords = property(
        _DynamsoftBarcodeReader.CQRCodeDetails_codewords_get,
        _DynamsoftBarcodeReader.CQRCodeDetails_codewords_set,
    )


_DynamsoftBarcodeReader.CQRCodeDetails_register(QRCodeDetails)


class PDF417Details(BarcodeDetails):
    thisown = property(
        lambda self: self.this.own(),
        lambda self, v: self.this.own(v),
        doc="The membership flag",
    )

    def __init__(
        self,
        rows: int = -1,
        columns: int = -1,
        level: int = -1,
        has_left_row_indicator: int = -1,
        has_right_row_indicator: int = -1,
    ):
        _DynamsoftBarcodeReader.CPDF417Details_init(
            self,
            _DynamsoftBarcodeReader.new_CPDF417Details(
                rows, columns, level, has_left_row_indicator, has_right_row_indicator
            ),
        )

    rows = property(
        _DynamsoftBarcodeReader.CPDF417Details_rows_get,
        _DynamsoftBarcodeReader.CPDF417Details_rows_set,
    )
    columns = property(
        _DynamsoftBarcodeReader.CPDF417Details_columns_get,
        _DynamsoftBarcodeReader.CPDF417Details_columns_set,
    )
    error_correction_level = property(
        _DynamsoftBarcodeReader.CPDF417Details_errorCorrectionLevel_get,
        _DynamsoftBarcodeReader.CPDF417Details_errorCorrectionLevel_set,
    )
    has_left_row_indicator = property(
        _DynamsoftBarcodeReader.CPDF417Details_hasLeftRowIndicator_get,
        _DynamsoftBarcodeReader.CPDF417Details_hasLeftRowIndicator_set,
    )
    has_right_row_indicator = property(
        _DynamsoftBarcodeReader.CPDF417Details_hasRightRowIndicator_get,
        _DynamsoftBarcodeReader.CPDF417Details_hasRightRowIndicator_set,
    )
    __destroy__ = _DynamsoftBarcodeReader.delete_CPDF417Details


_DynamsoftBarcodeReader.CPDF417Details_register(PDF417Details)


class DataMatrixDetails(BarcodeDetails):
    thisown = property(
        lambda self: self.this.own(),
        lambda self, v: self.this.own(v),
        doc="The membership flag",
    )

    def __init__(
        self,
        rows: int = -1,
        columns: int = -1,
        data_region_rows: int = -1,
        data_region_columns: int = -1,
        data_region_number: int = -1,
    ):
        _DynamsoftBarcodeReader.CDataMatrixDetails_init(
            self,
            _DynamsoftBarcodeReader.new_CDataMatrixDetails(
                rows, columns, data_region_rows, data_region_columns, data_region_number
            ),
        )

    rows = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_rows_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_rows_set,
    )
    columns = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_columns_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_columns_set,
    )
    data_region_rows = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionRows_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionRows_set,
    )
    data_region_columns = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionColumns_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionColumns_set,
    )
    data_region_number = property(
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionNumber_get,
        _DynamsoftBarcodeReader.CDataMatrixDetails_dataRegionNumber_set,
    )
    __destroy__ = _DynamsoftBarcodeReader.delete_CDataMatrixDetails


_DynamsoftBarcodeReader.CDataMatrixDetails_register(DataMatrixDetails)


class AztecDetails(BarcodeDetails):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self, rows: int = -1, columns: int = -1, layer_number: int = -1):
        _DynamsoftBarcodeReader.CAztecDetails_init(
            self, _DynamsoftBarcodeReader.new_CAztecDetails(rows, columns, layer_number)
        )

    rows = property(
        _DynamsoftBarcodeReader.CAztecDetails_rows_get,
        _DynamsoftBarcodeReader.CAztecDetails_rows_set,
    )
    columns = property(
        _DynamsoftBarcodeReader.CAztecDetails_columns_get,
        _DynamsoftBarcodeReader.CAztecDetails_columns_set,
    )
    layer_number = property(
        _DynamsoftBarcodeReader.CAztecDetails_layerNumber_get,
        _DynamsoftBarcodeReader.CAztecDetails_layerNumber_set,
    )
    __destroy__ = _DynamsoftBarcodeReader.delete_CAztecDetails


_DynamsoftBarcodeReader.CAztecDetails_register(AztecDetails)


class BarcodeResultItem(CapturedResultItem):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    def get_format(self) -> int:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetFormat(self)

    def get_format_string(self) -> str:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetFormatString(self)

    def get_text(self) -> str:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetText(self)

    def get_bytes(self) -> bytes:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetBytes(self)

    def get_location(self) -> Quadrilateral:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetLocation(self)

    def get_confidence(self) -> int:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetConfidence(self)

    def get_angle(self) -> int:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetAngle(self)

    def get_module_size(self) -> int:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetModuleSize(self)

    def get_details(self) -> BarcodeDetails:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_GetDetails(self)

    def is_dpm(self) -> bool:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_IsDPM(self)

    def is_mirrored(self) -> bool:
        return _DynamsoftBarcodeReader.CBarcodeResultItem_IsMirrored(self)


_DynamsoftBarcodeReader.CBarcodeResultItem_register(BarcodeResultItem)


class DecodedBarcodesResult(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    def __init__(self):
        raise AttributeError("No constructor defined - class is abstract")

    __destroy__ = _DynamsoftBarcodeReader.CDecodedBarcodesResult_Release

    def get_original_image_hash_id(self) -> str:
        return _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetOriginalImageHashId(
            self
        )

    def get_original_image_tag(self) -> ImageTag:
        return _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetOriginalImageTag(self)

    def get_rotation_transform_matrix(self) -> List[float]:
        return (
            _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetRotationTransformMatrix(
                self
            )
        )

    def get_items(self) -> List[BarcodeResultItem]:
        list = []
        count = _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetItemsCount(self)
        for i in range(count):
            list.append(_DynamsoftBarcodeReader.CDecodedBarcodesResult_GetItem(self, i))
        return list

    def get_error_code(self) -> int:
        return _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetErrorCode(self)

    def get_error_string(self) -> str:
        return _DynamsoftBarcodeReader.CDecodedBarcodesResult_GetErrorString(self)


_DynamsoftBarcodeReader.CDecodedBarcodesResult_register(DecodedBarcodesResult)


class BarcodeReaderModule(object):
    thisown = property(
        lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag"
    )

    @staticmethod
    def get_version() -> str:
        return _DynamsoftBarcodeReader.CBarcodeReaderModule_GetVersion()

    def __init__(self):
        _DynamsoftBarcodeReader.CBarcodeReaderModule_init(
            self, _DynamsoftBarcodeReader.new_CBarcodeReaderModule()
        )

    __destroy__ = _DynamsoftBarcodeReader.delete_CBarcodeReaderModule


_DynamsoftBarcodeReader.CBarcodeReaderModule_register(BarcodeReaderModule)
