from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Job
from .forms import AddJobForm, ApplicationForm


def job_detail(request, job_id):
    job =Job.objects.get(pk=job_id)

    return render(request, 'job/job_detail.html', {'job': job})

@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            return redirect('dashboard')

    else:
        form = ApplicationForm()

    return  render(request, 'job/apply_for_job.html',{'form': form, 'job':job})

@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm()

    return render(request, 'job/add_job.html', {'form': form})


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm(instance=job)

    return render(request, 'job/edit_job.html', {'form': form, 'job': job})