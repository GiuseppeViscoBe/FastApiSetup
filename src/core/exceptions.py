class BaseAppException(Exception):
    """Base exception for our application"""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class ResourceNotFoundException(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=404)

class DuplicateResourceException(BaseAppException):
    def __init__(self, message: str):
        super().__init__(message, status_code=409)