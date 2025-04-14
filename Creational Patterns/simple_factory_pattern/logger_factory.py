from loggers.debug_logger import DebugLogger
from loggers.warning_logger import WarningLogger
from loggers.error_logger import ErrorLogger
# Uncomment the line below if you add InfoLogger
# from loggers.info_logger import InfoLogger

# Factory class to create logger instances
class LoggerFactory:
    @staticmethod
    def create_logger(logger_type: str):
        if logger_type.lower() == "debug":
            return DebugLogger()
        elif logger_type.lower() == "warning":
            return WarningLogger()
        elif logger_type.lower() == "error":
            return ErrorLogger()
        # Uncomment the block below if you add InfoLogger
        # elif logger_type.lower() == "info":
        #     return InfoLogger()
        else:
            raise ValueError(f"Invalid logger type: {logger_type}")
