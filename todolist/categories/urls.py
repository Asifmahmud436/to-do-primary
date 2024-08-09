# from django.contrib import admin
from django.urls import path,include
from categories.views import add_categories
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add_categories/', add_categories,name='add_categories'),
    # path('categories/', include('tasks.urls')),
]
