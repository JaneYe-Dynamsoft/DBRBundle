if __package__ or "." in __name__:
    from . import _DynamsoftImageProcessing
else:
    import _DynamsoftImageProcessing


class DynamsoftImageProcessingModule:
    @staticmethod
    def get_version() -> str:
        return _DynamsoftImageProcessing.getversion()
