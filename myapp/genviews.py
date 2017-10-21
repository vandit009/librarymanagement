from django.views import generic
from myapp.models import Course, Topic
from random import randint
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse_lazy
from myapp.forms import TopicForm
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

class IndexView(generic.ListView):
    model = Course  # Use when not using get_queryset()
    template_name = 'myapp/index.html'
    context_object_name = 'courselist'
    def get_queryset(self):
        return self.model.objects.all()[:5]
    
    def get_context_data(self,**kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        #pass the cookie of index visit to the page
        index_visits = int(self.request.COOKIES.get('index_visits', '0'))
        context['index_visits'] = index_visits+1
        #luckynum count
        if not 'luckynum' in self.request.session or not self.request.session['luckynum']:
            self.request.session['luckynum'] =  randint(1,10)
        else:
            pass
        context['luckynum']=self.request.session['luckynum']
        return context
    
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        
            
        # count the index visits
        index_visits = int(request.COOKIES.get('index_visits', '0'))
        response=self.render_to_response(self.get_context_data())
        if 'index_last_visit' in request.COOKIES:
            last_visit = request.COOKIES['index_last_visit']
            last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
            if (datetime.now() - last_visit_time).seconds > 0:
                response.set_cookie('index_visits', index_visits+1)
                response.set_cookie('index_last_visit', datetime.now())
        else:
            response.set_cookie('index_visits', index_visits+1)
            response.set_cookie('index_last_visit', datetime.now())
            
        return response


class DetailView(generic.DetailView):
    model=Course
    template_name='myapp/detail.html'
    context_object_name= 'course'
    
    def get_object(self):
        course_no = self.kwargs.get('course_no', None);
        return get_object_or_404(Course, course_no=course_no)

class CreateView(generic.CreateView):
    model=Topic
    template_name='myapp/addtopic.html'
    form_class = TopicForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        return super(CreateView, self).form_valid(form)
    
    def get_success_url(self): 
        return reverse_lazy('myapp:topic') 
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(myform=form,))
    
