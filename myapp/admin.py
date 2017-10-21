from django.contrib import admin

# Register your models here.

from myapp.models import Book, Author, Course, Topic, Student, Instructor

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'courses_using_book')
    list_filter=['title']
    search_fields=['^title']

    def courses_using_book(self, obj):
        return ', '.join([course.title for course in obj.course_set.all()])

class AuthorAdmin(admin.ModelAdmin):
    fields = [('firstname', 'lastname'), 'birthdate','country' ]
    list_display = ('firstname', 'lastname', 'country')
    
#class CourseInline(admin.StackedInline):
    #model= Course
    #fields=[('Course_no', 'title')]
    #extra=2    
    
    
class CourseAdmin(admin.ModelAdmin):
    fields = [('course_no', 'title', 'textbook'), ('instructor', 'students') ]
    list_display = ('course_no', 'title', 'teacher')
    list_filter=['course_no', 'title']
    search_fields=['^title','^course_no',]

     
    def teacher(self, obj):
        return ', '.join([instructor.user.first_name+ " "+instructor.user.last_name for instructor in Instructor.objects.filter(course=obj)])
        #return obj.course_set.all()

class CourseInline(admin.StackedInline):
    fields=[('course_no', 'title')]
    model=Course
    extra=2
    
class InstructorAdmin(admin.ModelAdmin):
    inlines = [CourseInline]
    list_display=('user', 'office')
    
    search_fields=['^first_name', '^last_name']
    fieldsets=[
               ('Personal_Info',{'fields':['user']}), 
               ('Other Info', {'fields':['office', 'webpage']} ),]
    

def make_phd(modeladmin,request,queryset):
    queryset.update(level =3)
    make_phd.shortDescription="Level Changed to PHD!!"
def make_masters(modeladmin,request,queryset):
    queryset.update(level =2)
    make_masters.shortDescription="Level Changed to Masters!!"
    
    
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'level')
    actions=[make_phd, make_masters]
    #actions=[make_masters]
    
    
        

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Topic)
admin.site.register(Student, StudentAdmin)
admin.site.register(Instructor, InstructorAdmin)



