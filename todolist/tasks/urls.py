# from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('add_tasks/', views.add_tasks,name='add_tasks'),
    path('edit_tasks/<int:id>', views.edit_tasks,name='edit_tasks'),
    path('delete_tasks/<int:id>', views.delete_tasks,name='delete_tasks'),
    # path('categories/', include('tasks.urls')),
]
