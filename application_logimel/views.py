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

from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Formulaire de contact
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(max_length=15, label="Phone")
    sujet = forms.CharField(max_length=200, label="Sujet")
    message = forms.CharField(widget=forms.Textarea, label="Message")

def contact(request):
    if request.method == 'POST':
      prenom = request.POST.get('prenom')
      nom = request.POST.get('nom')
      email = request.POST.get('mail')
      phone = request.POST.get('phone')
      objet = request.POST.get('objet')
      message = request.POST.get('Message')

      data = {
          'prenom': prenom,
          'nom': nom,
          'email': email,
          'phone': phone,
          'objet' : objet,
          'message': message
      }
      message = '''
      {}
      prenom: {}
      nom: {}
      Phone: {}
      From: {}
      '''.format(data['message'], data['prenom'], data['nom'], data['phone'], data['email'])
      send_mail(data['objet'], message, '',['Cabrelboukamba@gmail.com'])

    return render(request, 'contact.html')

def etudiant(request):

    return render(request, 'services/etudiant.html')


def tourisme_affaire(request):

    return render(request, 'services/tourisme_affaire.html')


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
