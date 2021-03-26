class StringTransformer():

    DEFAULT_PREFIX = "default_prefix"
    DEFAULT_SUFFIX = "default_suffix"

    def __init__(self, prefix:str = DEFAULT_PREFIX, suffix: str = DEFAULT_SUFFIX):
        self.prefix = prefix
        self.suffix = suffix

    def transform(self, string):
        return f"{self.prefix}_{string}_{self.suffix}"