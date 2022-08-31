from django.shortcuts import render, redirect
from about.models import Developer
from about.forms import contactUsForm 

# Create your views here.
def about(request):
    developers = Developer.objects.all()
    context = {
        'developers':developers
    }
    return render(request,'about/about.html',context)


def contact_us_view(request):
    if request.method == 'POST':
        form = contactUsForm(request.POST)
        print (form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            errors = form.errors.items()
            form = contactUsForm()
            context = {'errors':errors, 'form':form}
            return render(request, 'about/contact-us.html', context=context)
    else:
        form = contactUsForm()
        context = {'form':form}
        return render(request, 'about/contact-us.html', context=context)
