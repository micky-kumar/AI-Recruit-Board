from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from apps.job.models import Job
from apps.userprofile.models import Userprofile

def page(request):
    jobs = Job.objects.all()[0:3]
    return render(request, 'core/home.html', {'jobs':jobs})

def ai_jobs(request):
    ai_jobs = {}
    for job in Job.objects.all():
        if job.skill_set == Userprofile.skill_set:
            ai_jobs['skill_set'] = job
    return render(request, 'ai/ai_jobs.html', ai_jobs)


def ai_job(request):
    jobs = Job.objects.all()[0:3]
    return render(request, 'userprofile/ai_job.html', {'jobs': jobs})


def resume(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['resume']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)  # FIXME bypassed on resume.html
        context['url'] = fs.url(name)  # FIXME bypassed on resume.html
        context['name'] = name
    # context['upload_time'] =          FIXME insert timestamp
    return render(request, 'userprofile/resume.html', context)

# if userprofile.skills == jobs.skills:
# {{ jobs.title }}
# {{ job.description }}
# <a href="{% url %}">job detail</a>

# print(os.link(page,))