from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AudioFileForm
from .models import Lecture


from .assembly_ai import handle_uploaded_file

def index(request):
    lecture_list = Lecture.objects.all().order_by('-date_uploaded')
    if len(lecture_list) > 20:
        lecture_list = lecture_list[0:20]
    return render(request, 'home.html', {'lecture_list': lecture_list})


@login_required
def upload(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.user, request.POST['name'], request.FILES['audio_file'], request.user)
            messages.success(request, f'Successfully uploaded {request.POST["name"]}!')
            return HttpResponseRedirect('upload')
    else:
        form = AudioFileForm()
    return render(request, 'upload.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    lecture_list = Lecture.objects.filter(Q(name__icontains=query) | Q(audio_file__icontains=query))
    return render(request, 'search.html', {'lecture_list': lecture_list})
