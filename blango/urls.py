import debug_toolbar
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from blango_auth.forms import BlangoRegistrationForm
import blango_auth.views
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls")),
    path(
        "accounts/register/",
        RegistrationView.as_view(form_class=BlangoRegistrationForm),
        name="django_registration_register",
    ),
    path('accounts/', include("django.contrib.auth.urls")),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("django_registration.backends.activation.urls")),
    path('accounts/profile/', blango_auth.views.profile, name="profile"),
]

if settings.DEBUG:
    urlpatterns += [
            path("__debug__", include(debug_toolbar.urls)),
            ]
