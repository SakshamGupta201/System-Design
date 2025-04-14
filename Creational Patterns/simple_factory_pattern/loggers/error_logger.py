from interfaces.ilog import ILog

# ErrorLogger implementation
class ErrorLogger(ILog):
    def log(self, message: str) -> None:
        print(f"[ERROR] {message}")
