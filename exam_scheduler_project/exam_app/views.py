from django.shortcuts import render
from .models import Dept, Course, Exam
from . import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.
def index(request):
    return render(request,'exam_app/index.html')

def course(request):
    return render(request,'exam_app/course.html')

def invigilator(request):
    return render(request,'exam_app/invigilator.html')

def room(request):
    return render(request,'exam_app/room.html')

def schedule(request):
    depts = Dept.objects.all()
    courses = Course.objects.all()
    return render(request,'exam_app/schedule.html',{'depts':depts,'courses':course})

def student(request):
    return render(request,'exam_app/student.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # print(form.cleaned_data["course"])
            cname_curr = form.cleaned_data['course']
            dname_curr = form.cleaned_data["dept"]
            for p in Course.objects.raw('SELECT * FROM exam_app_course WHERE cname = %s',[cname_curr]):
                #print (p.did)
                for d in Dept.objects.raw('SELECT * FROM exam_app_dept WHERE dname = %s',[dname_curr]):
                    if p.did == d.did:
                        print ("No Error")
                    else:
                        print("Error")

                # if p.did equals dept_db
                #     print ("Matching")
                # else
                #     print ("Error")

    return render(request,'exam_app/schedule_form.html', {'form':form})

# class ExamCreateView(CreateView):
#     model = Exam
#     fields = ('dept', 'course')
#     success_url = reverse_lazy('person_changelist')
#
# def load_courses(request):
#     dept_id = request.GET.get('dept')
#     courses = Course.objects.filter(did=dept_id)
#     return render(request, 'course_dropdown_list_options.html', {'courses': courses})
