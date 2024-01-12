from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

def store_file(file):
    with open("temp/image.png", "wb+") as dest:
        #Looping over UploadedFile.chunks() instead of using read() ensures that large files don’t overwhelm your system’s memory.
        # https://docs.djangoproject.com/en/5.0/topics/http/file-uploads/
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        return render(request, "profiles/create_profile.html")

    def post(self, request):
        store_file(request.FILES["image"])
        return HttpResponseRedirect("/profiles")