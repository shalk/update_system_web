import os

from django.shortcuts import render,get_object_or_404

from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse 
from django.views.generic import ListView,DetailView

from .models import AnsibleAdHoc,CloudManager,Files
import updatesystem
# Create your views here.
from .form import UploadFileForm


def index(request):
    cloudmanager_list = CloudManager.objects.all()
    context = {'cloudmanager_list': cloudmanager_list}
    return render(request,"usweb/index.html",context)

def handle_uploaded_file(f):
    filename = f.name
    cwd = os.path.dirname(__file__)
    filepath = os.path.join(cwd,'static/upload/{}'.format(filename))
    try:
        with open(filepath,'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
        return filepath
    except Exception as error:
        print(error.message)
        return None

def upload(request,status=None):
    if request.method == 'POST':
        file_path = handle_uploaded_file(request.FILES['myfile'])
        if file_path is not None:
            file1 = Files(name=os.path.basename(file_path),path=file_path)
            file1.save()

        #return HttpResponseRedirect(reverse("usweb:upload"),{'upload_success':True})
        return render(request,"usweb/upload.html",{'upload_success':True})
    else:
        return render(request,"usweb/upload.html",{'upload_success':status})

class AdHocView(DetailView):
    model = AnsibleAdHoc
    template = "usweb/adhoc.html"

class FilesView(ListView):
    model = Files
    template_name = 'usweb/files.html'

def update(request):
    return render(request,"usweb/update.html")

def status(request):
    return render(request,"usweb/status.html")

def about(request):
    return render(request,"usweb/about.html")

def do_check_before(request):
    pass
