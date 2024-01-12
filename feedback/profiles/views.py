from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm

# Create your views here.

def store_file(file):
    with open("temp/image.png", "wb+") as dest:
        #Looping over UploadedFile.chunks() instead of using read() ensures that large files don’t overwhelm your system’s memory.
        # https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html",{
            "form": form
            })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            store_file(request.FILES["image"])
            return HttpResponseRedirect("/profiles")
        return render(request, "profiles/create_profile.html",{
            "form": submitted_form
            })