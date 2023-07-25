from .models import RequestResponseLog
from time import time


class RequestResponseLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)

        RequestResponseLog.objects.create(
            method=request.method,
            status_code=response.status_code,
            path=request.path,
            time=round((time() - start), 3),
        )
        return response
