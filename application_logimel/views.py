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
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupération des données nettoyées
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']

            # Format du message à envoyer
            full_message = '''
            New message: {}

            Phone: {}
            From: {}
            '''.format(message, phone, email)

            # Envoi de l'email
            try:
                send_mail(sujet, full_message, '', ['Cabrelboukamba@gmail.com'])
                return HttpResponse("Message envoyé avec succès !")
            except Exception as e:
                return HttpResponse(f"Erreur lors de l'envoi du message : {e}")
        else:
            return HttpResponse("Formulaire invalide. Veuillez vérifier vos informations.")

    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})



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
