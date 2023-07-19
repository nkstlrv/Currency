from .models import RequestResponseLog
from time import time


class RequestResponseLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        middleware_time = round((time() - start), 3)
        print(middleware_time)

        return response
