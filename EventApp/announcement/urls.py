from django.urls import path
from . import views
app_name="announcement"
urlpatterns = [
    path('create',views.create_view,name="create"),
    path('delete/<int:id>',views.delete_view,name="delete"),
    path('update/<int:id>',views.update_view,name="update"),
    path('detail/<int:id>',views.detail_view,name="detail"),
]
