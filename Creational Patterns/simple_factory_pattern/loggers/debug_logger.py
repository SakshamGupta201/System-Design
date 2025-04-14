from interfaces.ilog import ILog

# DebugLogger implementation
class DebugLogger(ILog):
    def log(self, message: str) -> None:
        print(f"[DEBUG] {message}")
