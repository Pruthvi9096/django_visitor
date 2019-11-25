from django.db import models
from datetime import datetime

class VisitFor(models.Model):
	name = models.CharField(max_length=50)
	department = models.ForeignKey('Department',on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Department(models.Model):
	department_name = models.CharField(max_length=25)

	def __str__(self):
		return self.department_name

class Visitor(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField(max_length=254)
	phone = models.CharField(max_length=20)
	address = models.TextField(max_length=250)

	def __str__(self):
		return self.name

class Visit(models.Model):
	visitor_name = models.ForeignKey('Visitor',on_delete=models.CASCADE)
	visitor_phone = models.CharField(max_length=20)
	visitor_email = models.EmailField(max_length=250)
	visit_to = models.ForeignKey('VisitFor',on_delete=models.CASCADE)
	department = models.ForeignKey('Department',on_delete=models.CASCADE)
	purpose = models.CharField(max_length=150)
	checkOut_time = models.DateTimeField(null=True)
	checkIn_time = models.DateTimeField(null=True)
	
    


