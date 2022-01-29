from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AudioFileForm


from .assembly_ai import handle_uploaded_file

def index(request):
    return HttpResponse("Hello welcome to the summarizer")


def upload(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['audio_file'])
            return HttpResponseRedirect('/index/')
    else:
        form = AudioFileForm()
    return render(request, 'upload.html', {'form': form})
