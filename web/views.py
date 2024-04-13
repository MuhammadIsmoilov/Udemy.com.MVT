from django.shortcuts import render,redirect
from .models import Custom_User,Course, Enrollment,Lesson
from django.views import generic
from django.urls import reverse_lazy,reverse 

from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout 


class Custom_UserListView(generic.ListView):
    model = Custom_User
    template_name = "base.html"

class Custom_UserCreateView(generic.CreateView):
    model = Custom_User
    template_name = "create_user.html"
    fields = '__all__'
    success_url = reverse_lazy('home')

class Custom_UserDetailView(generic.DetailView):
    model = Custom_User
    template_name = "user_detail.html"

class Custom_UserUpdateView(generic.UpdateView):
    model = Custom_User 
    template_name = 'edit_user.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

class Custom_UserDeleteView(generic.DeleteView):
    model = Custom_User
    template_name = 'delete_user.html'
    success_url = reverse_lazy('home')

class CourseListView(generic.ListView):
    model = Course
    template_name = "base_course.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Custom_user'] = Custom_User.objects.all()
        return context 


    
    
class CourseCreateView(generic.CreateView):
    model = Course
    template_name = "create_course.html"
    fields = '__all__'
    success_url = reverse_lazy('home2')

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = "course_detail.html"

class CourseUpdateView(generic.UpdateView):
    model = Course
    template_name = 'edit_course.html'
    fields = '__all__'
    success_url = reverse_lazy('home2')

class CourseDeleteView(generic.DeleteView):
    model = Course
    template_name = 'delete_course.html'
    success_url = reverse_lazy('home2')


class EnrollmentListView(generic.ListView):
    model = Enrollment
    template_name = "base_enrollment.html"

class EnrollmentCreateView(generic.CreateView):
    model = Enrollment
    template_name = "create_enrollment.html"
    fields = '__all__'
    success_url = reverse_lazy('home3')

class EnrollmentDetailView(generic.DetailView):
    model = Enrollment
    template_name = "enrollment_detail.html"

class EnrollmentUpdateView(generic.UpdateView):
    model =Enrollment
    template_name = 'edit_enrollment.html'
    fields = '__all__'
    success_url = reverse_lazy('home3')

class EnrollmentDeleteView(generic.DeleteView):
    model = Enrollment
    template_name = 'delete_enrollment.html'
    success_url = reverse_lazy('home3')


class LessonListView(generic.ListView):
    model = Lesson
    template_name = "base_lesson.html"

class LessonCreateView(generic.CreateView):
    model = Lesson
    template_name = "create_lesson.html"
    fields = '__all__'
    success_url = reverse_lazy('home4')

class LessonDetailView(generic.DetailView):
    model = Lesson
    template_name = "lesson_detail.html"

class LessonUpdateView(generic.UpdateView):
    model = Lesson
    template_name = 'edit_lesson.html'
    fields = '__all__'
    success_url = reverse_lazy('home4')

class LessonDeleteView(generic.DeleteView):
    model = Lesson
    template_name = 'delete_lesson.html'
    success_url = reverse_lazy('home4')


def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "signup.html", {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect("login")
