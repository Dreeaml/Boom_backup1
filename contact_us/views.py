from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import ContactForm
from django.http import HttpResponse 

from django.views.generic import View

from django.core.mail import EmailMessage



# Create your views here.

def contact_us(request):
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                sender_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']

                try:
                    send_mail(subject, message, sender_email, ['boomentrepreneurship@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('success')
        return render(request, "contact_us.html", {'form': form})