from interfaces.ilog import ILog

# InfoLogger implementation (optional)
class InfoLogger(ILog):
    def log(self, message: str) -> None:
        print(f"[INFO] {message}")
