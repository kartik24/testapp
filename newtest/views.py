from django.shortcuts import render,redirect
from .models import Product
from .forms import ContactForm, RegisterForm

# Create your views here.
def New(request):
    products = Product.objects.all()
    return render(request, 'newtest/home.html', {'products': products})




def Contact(request):
    form_class = ContactForm

    if request.method == 'POST':

        form = form_class(data=request.POST)
        form.save()
        #email logic
        return redirect('/thanks/')

    else:
        form = form_class;


    return render(request, 'newtest/contact.html', {
    'form': form_class,
})


def Register_form(request):
    form_class = RegisterForm

    if request.method == 'POST':

        form = form_class(data=request.POST)
        form.save()
        #email logic
        return redirect('/thanks/')

    else:
        form = form_class;


    return render(request, 'newtest/register.html', {
    'form': form_class,
})

def Thanks(request):
    return render(request, 'newtest/thanks.html', )