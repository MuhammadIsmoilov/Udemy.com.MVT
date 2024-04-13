# #### Student: Muhammad Ismoilov
# #### Project: Online Learning Platform (udemy.com)

# # Models: Course, Lesson, Enrollment, User
# # Features: CRUD on Course, Lesson, Enrollment
# # Templates: Course, Lesson, Enrollment




from django.db import models
from django.urls import reverse


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.pk})

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"

    def __str__(self):
        return self.lesson_name

    def get_absolute_url(self):
        return reverse("lesson_detail", kwargs={"pk": self.pk}) 

class Custom_User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=12)

    
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.first_name+" "+self.last_name

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})

class Enrollment(models.Model):
    student = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now = True)

    class Meta:
        unique_together = ['student','course']