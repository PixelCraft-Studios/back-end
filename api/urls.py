from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('/', ),
  path('get-cards/', get_cards),
  path('create-card/', create_card),
  path('select-card/<int:card_id>/', select_card),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

