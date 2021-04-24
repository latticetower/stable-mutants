class CVModel:
    def __init__(self, cls, nfolds=5, cls_args, cls_kwargs):
        """
        cls - class name for inner model
        We suppose that it has
        """
        self.cls = cls
        self.nfolds = nfolds
        for i in range(nfolds):
            cls(*cls_args, **cls_kwargs)