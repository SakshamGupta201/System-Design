class MiddleWareHandler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        else:
            return "Request cannot be handled."


class Authentication(MiddleWareHandler):
    def handle(self, request):
        if request.get("Auth"):
            print("Auth")
            return super().handle(request)
        else:
            return "User not Authenticated"


class AWSMiddleWare(MiddleWareHandler):
    def handle(self, request):
        if request.get("aws"):
            print("AWS middleware is present")
            return super().handle(request)
        else:
            return "AWS middleware is not present"


class MessageMiddleWare(MiddleWareHandler):
    def handle(self, request):
        if request.get("message"):
            print("AWS message is present")
            return "All middleware are present!"
        else:
            return "AWS message is not present"


message_middleware = MessageMiddleWare()
aws_middleware = AWSMiddleWare(message_middleware)
auth_middleware = Authentication(aws_middleware)
request = {"Auth": True, "aws": "/key", "message": "Message"}
print(auth_middleware.handle(request))
