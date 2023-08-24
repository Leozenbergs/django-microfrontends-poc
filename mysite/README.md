# Configure django for micro-frontends

In the file `/mysite/mysite/settings.py/`, you have to add the following configuration:

``` python
# this is to allow our server to serve on localhost
ALLOWED_HOSTS = ['*'] # Here

# let the django django know where to look for templates
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': ['../simple-react/build'], # Here
'APP_DIRS': True,
'OPTIONS': {
.......
# these help django find the static files
STATIC_URL = '/static/'

# And Here
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "../simple-react/build/static"),
]
STATIC_ROOT = "static/"
```

Then on your URLs, you will need to implement the `TemplateView` for the `micro-frontend` url in your application:

``` python
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView
urlpatterns = [
 path(‘admin/’, admin.site.urls),
      ...other routes ...
 re_path(‘’, TemplateView.as_view(template_name=”index.html”)), # Here
]
```

And that's it, enjoy coding :) 