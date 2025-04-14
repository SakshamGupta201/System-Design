class Logger:
    """
    Singleton class to manage application logs.
    Ensures that only one instance of Logger exists throughout the application.
    Use `Logger()` to get the singleton instance.
    """

    __instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        # Create a new instance only if it doesn't exist
        if cls.__instance is None:
            cls.__instance = super(Logger, cls).__new__(cls)
            cls.__instance.logs = []  # Initialize attributes here
        return cls.__instance

    def add_log(self, message):
        self.logs.append(message)

    def show_logs(self):
        print("Logs:", self.logs)


logger1 = Logger()
logger1.add_log("Saksham is Great!")
logger2 = Logger()
logger2.add_log("Yes I know !")
print("Are logger1 and logger2 the same?", logger1 is logger2)
logger1.show_logs()
