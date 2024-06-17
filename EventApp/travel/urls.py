from django.urls import path
from . import views
app_name="travel"
urlpatterns = [
    path("",views.index_view,name='index'),
    path("create/",views.create_view,name='create'),
    path('detail/<int:id>',views.detail,name="detail"),
    path('update/<int:id>',views.update_view,name="update"),
    path('delete/<int:id>',views.delete_view,name="delete"),
]
