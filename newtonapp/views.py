from django.shortcuts import render, redirect
from .forms import RegisterForm, Message, SubsForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
           user  = form.save(commit=False)
           user.is_active = False
           user.save()
           current_site = get_current_site(request)
           mail_subject = 'Activete your blog account.'
           message = render_to_string('newtonapp/acc_active_email.html', {
               'user' : user,
               'domain' : current_site.domain,
               'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
               'token': account_activation_token.make_token(user),
           })
           to_email = form.cleaned_data.get('email')
           email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
           email.send()
           return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegisterForm()
    return render(request, 'newtonapp/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def home(request):
   
    if request.method == "POST":
        form = Message(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Message()
    context = {
    'form':form
    }
    return render(request, 'newtonapp/homepage.html', context)
    



def blogview(request):
    if request.method == "POST":
        form = SubsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = SubsForm()
    context = {
        'form': form
    }   
    return render(request, 'newtonapp/blog.html', context)
    