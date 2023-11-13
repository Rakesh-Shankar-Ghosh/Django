from django.urls import path
from app.controllers.productController import *


productRoutes = [

    path('get/product/', ProductController.fetchController,
         name='getMethod'),
    path('create/product/', ProductController.createProduct,
         name='fetch-controller2'),

    path('get/product/<int:product_id>/',
         ProductController.singleProduct,   name='fetch-controller2'),


    path('test/it/', ProductController.testController,   name='fetch-controller2'),
    path('test/do/', ProductController.testController,   name='fetch-controller2'),

    path('async/', ProductController.Tester,   name='fetch-Tester'),

]
