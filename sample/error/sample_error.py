class SampleError(Exception):
    def __init__(self, exception, status, code, message):
        self.exception = exception
        self.status = status
        self.code = code
        self.message = message
