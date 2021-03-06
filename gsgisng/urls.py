from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from profiles.forms import MyRegistrationForm
from profiles.regbackend import RegBackend

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin app
    url(r'^admin/', include(admin.site.urls)),
    # Registration
    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'}),
    url(r'^accounts/register/$',
        'registration.views.register',
        {'form_class' : MyRegistrationForm,
         'backend': 'profiles.regbackend.RegBackend'},
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^avatar/', include('avatar.urls')),
    # Shp uploader
    url(r'^api/', include('pybab.api.urls')),
    # Django cms
    url(r'^', include('cms.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
