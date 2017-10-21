# Import necessary classes
from django.shortcuts import render_to_response 
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from myapp.models import Course, Book, Author, Student, Instructor
from myapp.models import Topic
from myapp.forms import TopicForm, InterestForm, MyRegistrationForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from pip._vendor import requests
from django.db.transaction import commit
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template import RequestContext 
from datetime import datetime


auth=User.objects.all()

def welcome(request):
    
    hi='Welcome To The Course APP'
    
    return render_to_response('myapp/welcome.html', {'hi': hi, 'auth': auth, 'user':request.user,}) 
# Create your views here.
def index(request):        # This is your index view function
    # Access db to get list of courses. limit 10
    courselist = Course.objects.all()[:10]        
    #response = HttpResponse()        # Create empty response object

    # For each course, create a str to write to response
    #for course in courselist:
        #para = '<p>' + str(course) + '</p>'      # This is the new string
        #response.write(para) # Add each str as a <p> to response obj
    return render_to_response('myapp/index.html', {'courselist': courselist, 'auth': auth, 'user':request.user},) 

                   
# Create your views here.
def about(request):        # This is your index view function
    # Access db to get list of courses. limit 10
          
   # response = HttpResponse()        # Create empty response object
   # request.session.set_test_cookie()
    # For each course, create a str to write to response
    #abc="This APP let you view and select courses to register in"
    c=RequestContext(request)
    visits = int(request.COOKIES.get('visits', '0'))
    if 'last_visit' in request.COOKIES:
        last_visit = request.COOKIES['last_visit']
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - last_visit_time).seconds > 0:
            response =render_to_response('myapp/about.html',{'visits':visits+1},c)
            response.set_cookie('visits', visits+1)
            response.set_cookie('last_visit', datetime.now())
    else:
        response =render_to_response('myapp/about.html',{'visits':visits+1},c)
        response.set_cookie('visits', visits+1)
        response.set_cookie('last_visit', datetime.now())
    
    return response
    #para = '<p>' + str(abc) + '</p>'      # This is the new string
    #response.write(para) # Add each str as a <p> to response obj
    #return render_to_response('myapp/about.html' , {'index' : index(request),'abc': abc, 'auth': auth, 'user':request.user},) 


# Create your views here.
@login_required(redirect_field_name='user_login')
def detail(request, course_no):        
        #  courselist = Course.objects.all()[:10]        
        #response = HttpResponse() 
        a=get_object_or_404(Course,course_no=course_no)
       #print(course_no)       
        #for course in courselist:
            #if (int(course_no)==int(course.course_no)):
               # para = '<p>' + str(course.course_no) + '</p>' 
               # para1 = '<p>' + str(course.title) + '</p>' 
               # para2 = '<p>' + str(course.textbook) + '</p>' 
               # response.write(para)
                #response.write(para1)
                #response.write(para2)
            #else:
               # a=get_object_or_404(Course,course_no=course_no)
        
        return render_to_response('myapp/detail.html', {'course': a,'auth':auth,'user' : request.user,}) 
def topics(request):
    topiclist = Topic.objects.all()[:10]
    #if request.session.test_cookie_worked():
       # request.session.delete_test_cookie()
    return render(request,'myapp/topics.html', {'topiclist': topiclist, 'user' :request.user,})
    #else:
       # return HttpResponse('Please enable cookies and try again.')
    

def addtopic(request):
    topiclist = Topic.objects.all()
    if request.method=='POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.num_responses=1
            topic.save()
        return HttpResponseRedirect(reverse('myapp:topics'))
    else:
        form=TopicForm()
        #return render_to_response('myapp/addtopic.html', {'form':form, 'topiclist':topiclist})
        return render(request, 'myapp/addtopic.html', {'form':form,'topiclist':topiclist,'user' : request.user,})
def topicdetail(request, topic_id):
    topic= get_object_or_404(Topic, id=topic_id)
    if request.method=='POST':
        form= InterestForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['interested'] == '1':
                a=form.cleaned_data['age']
                topic.avg_age=(topic.avg_age*topic.num_responses)
                topic.num_responses+=1
                topic.avg_age=((a+topic.avg_age)/topic.num_responses)
                topic.save()
        return HttpResponseRedirect(reverse('myapp:topics'))
    else:
        form=InterestForm()
        #return render_to_response('myapp/topicdetail.html', {'form':form, 'topic':topic})
        return render(request, 'myapp/topicdetail.html', {'form':form, 'topic':topic,'user' : request.user})
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password) 
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('myapp:index'))
            else:
                return HttpResponse('Your account is disabled.')
        else:
            return HttpResponse('Invalid login details.') 
    else:
        return render(request, 'myapp/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(('welcome')))
@login_required
def mycourses(request):
    stu=hasattr(request.user,'student')
    message="You are not a student!"
    try:
        stu=Student.objects.filter(user=request.user)
        courselist=Course.objects.filter(students=stu)
    except Student.DoesNotExist:
           message="You are not a student!"
    
    
     
    
    return render(request,'myapp/mycourses.html' , {'user':request.user, 'courselist' : courselist, 'message': message })


def instructor(request,id):        
        #  courselist = Course.objects.all()[:10]        
        #response = HttpResponse() 
        a=get_object_or_404(Instructor, user_id=id)
        

       #print(course_no)       
        #for course in courselist:
            #if (int(course_no)==int(course.course_no)):
               # para = '<p>' + str(course.course_no) + '</p>' 
               # para1 = '<p>' + str(course.title) + '</p>' 
               # para2 = '<p>' + str(course.textbook) + '</p>' 
               # response.write(para)
                #response.write(para1)
                #response.write(para2)
            #else:
               # a=get_object_or_404(Course,course_no=course_no)
        
        return render_to_response('myapp/instructor.html', {'a': a,'auth':auth,'user' : request.user,}) 
@login_required
def mystudents(request):
    ins=hasattr(request.user,'instructor')
    message="You are not allowed to see this stuff!"
    try:
        ins=Instructor.objects.filter(user=request.user)
    except Instructor.DoesNotExist:
           message="You are not a instructor!"
    courselist=Course.objects.filter(instructor=ins)
    #studentlist=Student.objects.filter(instructor=ins)
     
    
    return render(request,'myapp/mystudents.html' , {'user':request.user, 'courselist' : courselist,'message': message })
def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("http://127.0.0.3:8080/")
    else:
        form = MyRegistrationForm()
    return render(request, "myapp/register.html", {
        'form': form,
    })