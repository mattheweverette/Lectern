from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AudioFileForm
from .models import Lecture


from .tasks import get_transcript

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
            name = request.POST['name']
            file = request.FILES['audio_file']
            with open(f'media/{file.name}', "wb+") as destination:
                for chunk in request.FILES['audio_file'].chunks():
                    destination.write(chunk)

            lecture = Lecture.create(name, file.name, request.user)
            lecture.save()

            get_transcript.delay(lecture, f'media/{file.name}')
            messages.success(request, f'Successfully uploaded {name}!')
            return HttpResponseRedirect('upload')
    else:
        form = AudioFileForm()
    return render(request, 'upload.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    lecture_list = Lecture.objects.filter(Q(name__icontains=query) | Q(audio_file__icontains=query))
    return render(request, 'search.html', {'lecture_list': lecture_list})


def lecture(request, slug):
    post = Lecture.objects.get(slug=slug)
    return render(request, 'lecture.html', {'post': post})


def about(request):
    return render(request, 'about.html')
