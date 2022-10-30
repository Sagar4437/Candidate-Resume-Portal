from django.shortcuts import redirect, render
from django.contrib import messages
from ResumeApp.models import Candidate
from .forms import CandidateForm

# Create your views here.
def home(request):
    form = CandidateForm()
    candidates = Candidate.objects.all()
    if request.method=='POST':
        form = CandidateForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Candidate added Successfully')
        return redirect(home)
    return render(request,'home.html',{'form':form,'candidates':candidates})

def details(request,id):
    candidate = Candidate.objects.get(id=id)
    city = candidate.job_city[1:-1]
    Candidate.objects.filter(id=id).update(job_city=city)
    return render(request,'details.html', {'candidate':candidate})
    