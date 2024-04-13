from django.urls import path
from .views import *
urlpatterns = [

    
    path('', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),


    path('user-list/', Custom_UserListView.as_view(), name='home'),
    path('create/', Custom_UserCreateView.as_view(), name='create_user'),
    path('detail/<int:pk>/', Custom_UserDetailView.as_view(), name='detail_user'),
    path('edit/<int:pk>/', Custom_UserUpdateView.as_view(), name='edit_user'),
    path('delete/<int:pk>/', Custom_UserDeleteView.as_view(), name='delete_user'),


    path('course-list/', CourseListView.as_view(), name='home2'),
    path('create-course/', CourseCreateView.as_view(), name='create_course'),
    path('course-detail/<int:pk>/', CourseDetailView.as_view(), name='detail_course'),
    path('edit-course/<int:pk>/', CourseUpdateView.as_view(), name='edit_course'),
    path('delete-course/<int:pk>/', CourseDeleteView.as_view(), name='delete_course'),
   
    path('enrollment-list/',EnrollmentListView.as_view(), name='home3'),
    path('create-enrollment/', EnrollmentCreateView.as_view(), name='create_enrollment'),
    path('enrollment-detail/<int:pk>/', EnrollmentDetailView.as_view(), name='detail_enrollment'),
    path('edit-enrollment/<int:pk>/', EnrollmentUpdateView.as_view(), name='edit_enrollment'),
    path('delete-enrollment/<int:pk>/', EnrollmentDeleteView.as_view(), name='delete_enrollment'),
   
    path('lesson-list/', LessonListView.as_view(), name='home4'),
    path('create-lesson/', LessonCreateView.as_view(), name='create_lesson'),
    path('lesson-detail/<int:pk>/', LessonDetailView.as_view(), name='detail_lesson'),
    path('edit-lesson/<int:pk>/', LessonUpdateView.as_view(), name='edit_lesson'),
    path('delete-lesson/<int:pk>/', LessonDeleteView.as_view(), name='delete_lesson'),
    

   
]
