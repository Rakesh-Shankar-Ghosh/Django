from django.db import connections
from django.http import JsonResponse
import os
from dotenv import load_dotenv


def dbSetting():
    try:
        load_dotenv()
        database_settings = {
            'ENGINE': os.getenv('DB_ENGINE'),
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            # Required for transaction support in async views (Django >= 3.2)



        }
        return dict(database_settings)
    except Exception as err:
        print("Error:", str(err))


def testdbConnection(database_name):
    try:
        connection = connections[database_name]
        res = connection.ensure_connection()

        print("Database Connection successfull with:", database_name)
        # return JsonResponse({'message': 'Connected to the database', 'database': database_name})

    except Exception as e:
        print("Failed to connect to the database:", database_name)
        print("Error:", str(e))
        # return JsonResponse({'message': 'Failed to connect to the database', 'database': database_name, 'error': str(e)})


# use it if you use controller
# def dbSetting():
#     try:
#         load_dotenv()
#         database_settings = {
#             'ENGINE': os.getenv('DB_ENGINE'),
#             'NAME': os.getenv('DB_NAME'),
#             'USER': os.getenv('DB_USER'),
#             'PASSWORD': os.getenv('DB_PASSWORD'),
#             'HOST': os.getenv('DB_HOST'),
#             'PORT': os.getenv('DB_PORT'),
#         }
#         return dict(database_settings)
#     except Exception as err:
#         print("Error:", str(err))


# def testdbConnection(database_name):
#     try:
#         connection = connections[database_name]
#         res = connection.ensure_connection()
#         return JsonResponse({'message': 'Connected to the database', 'database': database_name})

#     except Exception as e:
#         return JsonResponse(
#             {'message': 'Failed to connect to the database', 'database': database_name, 'error': str(e)})
