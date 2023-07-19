from .models import RequestResponseLog
from time import time
from datetime import datetime


class RequestResponseLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('[RequestResponseLog middleware]')
        response = self.get_response(request)
        print(request.method)
        print(request.path)
        print(datetime.now().strftime('%d/%b/%Y %H:%M:%S'))
        print(int(time()))

        return response
