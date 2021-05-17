from django.db import models

# Create your models here.
class Faculty(models.Model):
    
    professor_name = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = "faculty" # replace plural with singular verb "Faculty" instead of "Facultys"

    def __str__(self):
        return self.professor_name


class Department(models.Model):

    department_name = models.CharField (max_length = 100)
    professor_name = models.ForeignKey(Faculty, on_delete= models.CASCADE)
    


    class Meta:
        verbose_name_plural = "department"

    def __str__(self):
        return self.department_name



class Grade(models.Model):
    grad_level = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "grade"

    def __str__(self):
        return self.grad_level


class Certificate(models.Model):
    degree_type = models.CharField(max_length = 100)

    class Meta:
        verbose_name_plural = "certificate"

    def __str__(self):
        return self.degree_type



class School(models.Model):

    school_name = models.CharField(max_length = 200)

    class Meta:
        verbose_name_plural = "school"

    def __str__(self):
        return self.school_name


class Student(models.Model):

    full_name = models.CharField(max_length = 100)
    graduation_year = models.IntegerField()
    department = models.ForeignKey(Department, on_delete= models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete= models.CASCADE)
    certificate_type = models.ForeignKey(Certificate, on_delete= models.CASCADE)
    

    class Meta:
        verbose_name_plural = "student"

    def __str__(self):
        return self.full_name


# class School(models.Model):
#     name = models.CharField(max_length =400)
#     address = models.CharField(max_length = 300)
#     zip_code = models.IntegerField()
    
# class Student(models.Model):
#     school = models.ForeignKey(School, on_delete=models.CASCADE)

# >>> from models.models import Student
# >>> student = Student(full_name="Jack Stevens",graduation_year=2004)
# >>> student.save()