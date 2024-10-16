from django.urls import path

from logilmel_company_dj import settings
from django.conf.urls.static import static
from .views import accueil, about, actualite, contact, nos_service, logistique, medical, affaire, change_language, description_logimel_plus

urlpatterns = [
    path('', accueil, name="accueil"),
    path('about', about, name="about"),
    path('actualite', actualite, name="actualite"),
    path('nos_service/', nos_service, name="nos_service"),
    path('nos_service/logistique/', logistique, name='logistique'),
    path('nos_service/medical/', medical, name='medical'),
    path('nos_service/affaire/', affaire, name='affaire'),

    path('contact', contact, name="contact"),


    path('description_logimel_plus', description_logimel_plus, name="description_logimel_plus"),

    path('change_language/<str:lang_code>/', change_language, name='change_language'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)