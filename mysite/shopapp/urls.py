from django.urls import path
from shopapp.views import shop_index, group_list, product_list

app_name = "shopapp"

urlpatterns = [
    path("", shop_index, name="index"),
    path("groups/", group_list, name="group_list"),
    path("products/", product_list, name="product_list")

]