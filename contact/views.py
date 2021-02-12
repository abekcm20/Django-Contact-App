from django.shortcuts import render,redirect
from .models import contact

# Create your views here.
def index(request):
    contacts = contact.objects.all()
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = contact.objects.filter(full_name__icontains=search_input)
    else:
        contacts = contact.objects.all()
        search_input = ''

    return render(request, 'index.html', {'contacts': contacts ,'search_input':search_input})


def addcontact(request):
    if request.method == 'POST':
        new_contact = contact(
          full_name =request.POST['fullname'],
          relationship =request.POST['relationship'],
          email =request.POST['email'],
          phone_number =request.POST['phone-number'],
          address =request.POST['address']
        )
        new_contact.save()
        return redirect('/')
    return render(request, 'new.html')
def contactprofile(request,pk):
    contactpro = contact.objects.get(id=pk)
    return render(request,'contact-profile.html',{'contactpro': contactpro})

def editcontact(request,pk):
    contactpro = contact.objects.get(id=pk)
    if request.method == 'POST':
        contactpro.full_name = request.POST['fullname']
        contactpro.relationship = request.POST['relationship']
        contactpro.email = request.POST['e-mail']
        contactpro.phone_number = request.POST['phone-number']
        contactpro.address= request.POST['address']
        contactpro.save()
        return redirect('/profile/'+str(contactpro.id))
    return render(request,'edit.html',{'contactpro': contactpro})

def deletecontact(request,pk):
    contactpro = contact.objects.get(id=pk)
    if request.method == 'POST':
        contactpro.delete()
        return redirect('/')
    return render(request,'delete.html',{'contactpro': contactpro})