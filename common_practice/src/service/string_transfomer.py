class StringTransformer():

    DEFAULT_PREFIX = "default_prefix"
    DEFAULT_SUFFIX = "default_prefix"

    def __init__(self):
        self.prefix = DEFAULT_PREFIX
        self.suffix = DEFAULT_SUFFIX

    def __init__(self, prefix:str, suffix: str):
        self.prefix = prefix
        self.suffix = suffix

    def transform(self, string):
        return f"{self.prefix}_{string}_{self.suffix}"