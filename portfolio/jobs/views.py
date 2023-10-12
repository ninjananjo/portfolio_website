from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Job
from .forms import MessageForm


def homepage(request):
    jobs = Job.objects.order_by('-date_completed')
    if request.method == 'POST':
        completed_form = MessageForm(request.POST)
        if completed_form.is_valid():
            completed_form.save()
            message = str(completed_form.cleaned_data['name'] + ' (' +
                          completed_form.cleaned_data['email'] + ')\n' +
                          completed_form.cleaned_data['message']
                          )
            send_mail('Portfolio Website Message',
                      message,
                      settings.EMAIL_HOST_USER,
                      [settings.EMAIL_HOST_USER],
                      fail_silently=False
                      )
            note = 'Message sent'
            new_form = MessageForm()
            return render(request, 'jobs/home.html', {'jobs': jobs, 'form': new_form, 'note': note})
    else:
        form = MessageForm()
        return render(request, 'jobs/home.html', {'jobs': jobs, 'form': form})


def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})


def contact(request):
    if request.method == 'POST':
        completed_form = MessageForm()
        if completed_form.is_valid():
            completed_form.save()
            #TODO Add email alert
            note = 'Message sent'
            new_form = MessageForm()
            return render(request, 'jobs/contact.html', {'form': new_form, 'note': note})
    else:
        form = MessageForm()
        return render(request, 'jobs/contact.html', {'form': form})
