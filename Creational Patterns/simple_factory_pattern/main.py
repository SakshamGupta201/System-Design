from logger_factory import LoggerFactory

# Main program
if __name__ == "__main__":
    # Create instances of different loggers using the factory
    debug_logger = LoggerFactory.create_logger("debug")
    warning_logger = LoggerFactory.create_logger("warning")
    error_logger = LoggerFactory.create_logger("error")

    # Use the loggers
    debug_logger.log("This is a debug message.")
    warning_logger.log("This is a warning message.")
    error_logger.log("This is an error message.")

    # Example: Dynamically choosing a logger
    log_type = "error"  # Can be changed dynamically
    dynamic_logger = LoggerFactory.create_logger(log_type)
    dynamic_logger.log("Dynamic logger in action!")
