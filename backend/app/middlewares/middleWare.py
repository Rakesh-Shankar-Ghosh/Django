

from django.http import JsonResponse
from django.core.exceptions import ValidationError
import json


class ProductMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path.startswith('/create/product/'):  # ofcourse backend  url
            body_unicode = request.body.decode('utf-8')
            post = json.loads(body_unicode)
            
            response = self.get_response(request)
            print("Middleware called", list(request))
            return response
        else:
            print("Middleware doesn't called")
            return self.get_response(request)


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # your logic here rakesh..... like requireSignin in node you did
        data = 5

        if request.path.startswith('/test/'):  # ofcourse backend  url
            if data == 5:
                response = self.get_response(request)
                print("Middleware called", list(response))
                return response
        else:
            # print("Middleware doesn't called")
            return self.get_response(request)

    # def __call__(self, request):
    #     data = 5
    #     if data == 5:
    #         response = self.get_response(request)
    #         print("middleware called")
    #         return response
    #     else:
    #         print("middleware doesn't called")

    # def __init__(self, get_response):
    #     self.get_response = get_response

    # def rtn(self):
    #     return 81

    # def __call__(self, request):
    #     if request.path.startswith('/test/') and self.rtn() == 8:
    #         print("Middleware Called")
    #         # Condition is met, so invoke the controller
    #         response = ProductController.fetchController(request)
    #         return response
    #     else:
    #         # If the condition is not met, pass the request to the next middleware.
    #         print("Middleware Does not Called")
    #         return self.get_response(request)
