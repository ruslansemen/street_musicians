from django.urls import path
from .views import index, create


"""
https://host:port/musicians/ GET
https://host:port/musicians/add/ GET
https://host:port/musicians/add/ POST
https://host:port/musicians/<id>/ GET
https://host:port/musicians/<id>/edit GET
https://host:port/musicians/<id>/edit PATCH PUT
https://host:port/musicians/<id>/ DELETE
"""


urlpatterns = [
    path("", index, name="musicians"),
    path("add/", create, name="musicians-add"),
    # path("<id:musician_id>", index, name="musicians-detail"),
]

"""
{% url 'musicians-detail' 1 %}"


/musicians/1/



    https://example.com/login  METHOD: GET
<form action="{% url 'login' }" method="post">
    _______________
    login: ...
    _______________
    password: ...
    _______________
</form>

HTTP Code: 200

    https://example.com/login  METHOD: POST

user = User.objects.create(login, password)
context = {"user": user}

_______________
успешно зарегестрирован {{ user }}
_______________
HTTP Code: 201

"""
