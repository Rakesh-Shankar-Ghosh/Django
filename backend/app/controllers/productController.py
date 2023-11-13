
from django.core.exceptions import ValidationError
from django.http import JsonResponse

from django.views.decorators.http import require_http_methods

from django.middleware.csrf import get_token

from app.models import *

from django.views.decorators.csrf import csrf_exempt

import json


import asyncio
from asgiref.sync import sync_to_async
from django.http import HttpResponse


class ProductController:

    @require_http_methods(['GET'])
    def fetchController(request):
        try:
            # Fetch all objects from the database asynchronously
            data = bapon.objects.all().values()

            response_data = {
                'success': True,
                'message': 'Data Fetched Successfully From Database',
                'data': list(data),
                'csrf_token':  get_token(request)
            }
            return JsonResponse(response_data, status=200)
        except Exception as error:
            response_data = {
                'success': False,
                'message': 'Something went wrong',
                'error': str(error)
            }
            return JsonResponse(response_data, status=500)

# Without Validation
    # @csrf_exempt
    # @require_http_methods(['POST'])
    # def createProduct(request):
    #     try:
    #         body_unicode = request.body.decode('utf-8')
    #         post = json.loads(body_unicode)
    #         name = post['name']
    #         price = post['price']
    #         quantity = post['quantity']

    #         # Extract data from the request

    #         # Check if the name is not empty
    #         if not name:
    #             raise ValueError('The name field cannot be empty.')

    #         product = bapon(name=name, price=price, quantity=quantity)
    #         product.save()

    #         if product:
    #             response_data = {
    #                 'success': True,
    #                 'message': 'Product created successfully',
    #                 'data': {
    #                     'id': product.id,
    #                     'name': product.name,
    #                     'price': product.price,
    #                     'quantity': product.quantity
    #                 }
    #             }
    #             return JsonResponse(response_data, status=201)
    #     except Exception as error:
    #         response_data = {
    #             'success': False,
    #             'message': 'Something went wrong',
    #             'error': str(error)
    #         }
    #         return JsonResponse(response_data, status=500)

    @require_http_methods(['GET'])
    def singleProduct(request, product_id):
        try:
            # Fetch the single product from the database
            product = bapon.objects.get(pk=product_id)

            response_data = {
                'success': True,
                'message': 'Product Fetched Successfully',
                'result': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'quantity': product.quantity
                },
                'csrf_token': get_token(request)
            }
            return JsonResponse(response_data, status=200)
        except bapon.DoesNotExist:
            response_data = {
                'success': False,
                'message': 'Product not found',
            }
            return JsonResponse(response_data, status=404)
        except Exception as error:
            response_data = {
                'success': False,
                'message': 'Something went wrong',
                'error': str(error)
            }
            return JsonResponse(response_data, status=500)

    @require_http_methods(['GET'])
    def testController(request):
        try:
            response_data = {
                'success': True,
                'message': 'Test Controller get data Successfully',
                'data': 20,
                'csrf_token':  get_token(request)
            }

            return JsonResponse(response_data, status=200)
        except Exception as error:
            response_data = {
                'success': False,
                'message': 'Something went wrong',
                'error': str(error)
            }
            return JsonResponse(response_data, status=500)

    # This bellow function is async function which sync form is test

    async def Tester(request):
        if request.method == 'GET':
            try:
                # Fetch all objects from the database asynchronously
                data = await sync_to_async(list)(bapon.objects.all().values())

                response_data = {
                    'success': True,
                    'message': 'Data Fetched Successfully From Database',
                    'data': data,  # coz data is already listed
                    'csrf_token': get_token(request)
                }

                return JsonResponse(response_data, status=200)

            except Exception as error:
                response_data = {
                    'success': False,
                    'message': 'Something went wrong',
                    'error': str(error)
                }
                return JsonResponse(response_data, status=404)
        else:
            return JsonResponse("Invalid HTTP method. This view only supports GET requests.")


# With Validation


    @csrf_exempt
    @require_http_methods(['POST'])
    def createProduct(request):
        try:
            body_unicode = request.body.decode('utf-8')
            post = json.loads(body_unicode)
            name = post['name']
            price = post['price']
            quantity = post['quantity']

            # Perform validation
            if not name:
                raise ValidationError("Name field is required.")
            if not isinstance(price, (float, int)) or price < 0:
                raise ValidationError("Price must be a non-negative number.")
            if not isinstance(quantity, int) or quantity < 0:
                raise ValidationError(
                    "Quantity must be a non-negative integer.")

            product = bapon(name=name, price=price, quantity=quantity)
            product.full_clean()  # Validate the model instance
            product.save()

            if product:
                response_data = {
                    'success': True,
                    'message': 'Product created successfully',
                    'data': {
                        'id': product.id,
                        'name': product.name,
                        'price': product.price,
                        'quantity': product.quantity
                    }
                }
                return JsonResponse(response_data, status=201)
        except ValidationError as error:
            response_data = {
                'success': False,
                'message': 'Validation Error',
                'error': str(error)
            }
            return JsonResponse(response_data, status=400)
        except Exception as error:
            response_data = {
                'success': False,
                'message': 'Something went wrong',
                'error': str(error)
            }
            return JsonResponse(response_data, status=500)
