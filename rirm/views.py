from django.shortcuts import render
from .models import Register

# Create your views here.
def index(request):
    return render(request,'index.html')

def handleregister(request):
    if (request.method == 'GET'):
        return render(request, "register.html",{})

    if (request.method == 'POST'):
        Name = request.POST["Name"]
        URL = request.POST["URL"]
        phone_number = request.POST["phone_number"]


        # save to db
        e = Register(Name=Name, URL=URL, phone_number=phone_number)
        e.save()

        return render(request, "show1.html", {"msg": "Registered Successfully"})


def search(request):
    if (request.method == 'GET'):
        return render(request, 'read.html')

    if (request.method == 'POST'):
        Name = request.POST['Name']

        try:
            eobj = Register.objects.get(Name=Name)

        except:
            return render(request, "read.html", {"msg": "No Records found...!"})

        else:
            return render(request, "namedisplay.html", {"name": eobj})
        ################hkk############
        ####kmgkmhkmkmhkmkhkdmh