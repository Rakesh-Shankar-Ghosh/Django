from django.urls import path
from ..controllers.AuthController import *


authRoutes = [

    path('login/', loginController, name='login-controller'),
    # path('register/', registerController,   name='register-controller2'),
    path('fetch/', fetchController,   name='fetch-controller2'),
]
