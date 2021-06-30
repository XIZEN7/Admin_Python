from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('', admin.site.urls),
]

# Admin header
admin.site.site_header = 'Admin'
admin.site.index_title = 'Administrador'
