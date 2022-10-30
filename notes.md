# To view media files in brower

image.png

## Step 1: Add in Settings.py

MEDIA_ROOT = Path(BASE_DIR,'media')
MEDIA_URL = '/media/'

## Step 2: add in urls.py

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## Step 3:

form = CandidateForm(request.POST, request.FILES)

## Step 4:

<form method='POST' autocomplete='off' enctype="multipart/form-data">
