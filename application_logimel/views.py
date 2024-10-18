from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings
from django.utils import translation
from django.shortcuts import redirect
from django.core.mail import send_mail

def accueil(request):
    return render(request, 'accueil.html')

def about(request):
    return render(request, 'about.html')


def nos_service(request):
    return render(request, 'nos_service.html')


def logistique(request):
    return render(request, 'services/logistique.html')


def medical(request):
    return render(request, 'services/medical.html')


def affaire(request):
    return render(request, 'services/affaire.html')


def actualite(request):
    return render(request, 'actualite.html')

def contact(request):
    if request.method == 'POST':
      name = request.POST.get('your Name') 
      email = request.POST.get('Email')
      phone = request.POST.get('Phone')
      sujet = request.POST.get('Sujet')
      message = request.POST.get('Message')

      data = {
          'name': name,
          'email': email,
          'phone': phone,
          'sujet' : sujet,
          'message': message
      }
      message = '''
      New message: {}

      Phone: {}
      From: {}
      '''.format(data['message'], data['phone'], data['email'])
      send_mail(data['sujet'], message, '',['Cabrelboukamba@gmail.com'])

    return render(request, 'contact.html')


from django.conf import settings
from django.utils import translation
from django.shortcuts import redirect

def change_language(request, lang_code):
    if lang_code in dict(settings.LANGUAGES).keys():
        translation.activate(lang_code)
        request.session[translation.LANGUAGE_COOKIE_NAME] = lang_code  # Utiliser LANGUAGE_COOKIE_NAME
        response = redirect(request.META.get('HTTP_REFERER', '/'))
        return response
    return redirect('/')


def description_logimel_plus(request):
    return render(request, 'details/description_logimel_plus.html')
