from interfaces.ilog import ILog

# WarningLogger implementation
class WarningLogger(ILog):
    def log(self, message: str) -> None:
        print(f"[WARNING] {message}")
