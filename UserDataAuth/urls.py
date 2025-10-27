from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home_view, name="home"),
    path('login/', views.UserLogin_view, name="login"),
    path('signup/', views.UserSignup_view, name="signup"),
    path("users/", views.userDetails_view, name="users"),
    path("insert/", views.usersInsert_view, name="insert"),
    path("update/<int:id>/", views.usersUpdate_view, name="update"),
    path("delete/<int:id>/", views.usersDelete_view, name="delete"),
    path("logout/", views.logout_view, name="logout"),
]
