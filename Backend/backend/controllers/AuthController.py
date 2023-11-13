from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse


def something():
    return 8


def something2():
    return {'name': 'John',
            'age': 25,
            'city': 'New York'}


@require_http_methods(['GET'])
def fetchController(request):
    try:
        # Fetch all objects from the database asynchronously
        # data = await userModel.objects.all().values()

        response_data = {
            'success': True,
            'message': 'Data Fetched Successfully',
            'data': 0
        }
        return JsonResponse(response_data, status=200)
    except Exception as error:
        response_data = {
            'success': False,
            'message': 'Something went wrong',
            'error': str(error)
        }
        return JsonResponse(response_data, status=500)


async def loginController(request):
    pass
