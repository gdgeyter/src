from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm

# Create your views here.
def home(request):
    title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "My Title %s" %(request.user)

    # if request.method == 'POST':

    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,

    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name

        # if not instance.full_name:
        #     instance.full_name = "Justin"
        instance.save()
        context = {
            "title": 'Thank you',

        }
        print(instance.email)
        print(instance.timestamp)


    return render(request, "home.html", context)

def contact(request):
    title = 'Contact Us'
    title_align_center = True
    form = ContactForm(request.POST or None)

    if form.is_valid():
        # for key, value in  form.cleaned_data.items():
        #     print(key,value)
        form_email = form.cleaned_data.get('email')
        form_message = form.cleaned_data.get('message')
        form_full_name = form.cleaned_data.get('full_name')
        # print(email, message, full_name)
        subject = 'site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'gertdegeyter@gmail.com']
        contact_message = "%s :%s via %s"%(
            form_full_name,
            form_message,
            form_email)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

    context = {
        "form": form,
        "title": title,
        "title_align_center": title_align_center
    }


    return render(request, "forms.html", context)








