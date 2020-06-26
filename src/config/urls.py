from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


###############admin setting####################

admin.site.site_header = "ClassRoom Admin"
admin.site.site_title = "ClassRoom Admin"
# admin.site.site_url = 'http://coffeehouse.com/'
admin.site.index_title = "Welcome, Administration Panel"
admin.empty_value_display = "**Empty**"

###############################################

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("classroom.urls")),
    path("users/", include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
