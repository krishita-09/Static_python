class DataCleaningError(Exception):     #creating a custom exception which can be raised
    def __init__(self, message="Problem while trying to clean data"):
        self.message = message
        super().__init__(self.message)
