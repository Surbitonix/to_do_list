from django.db import models

class List(models.Model):
	item = models.CharField(max_length=200)
	description = models.CharField(default=" ",max_length=250)
	completed = models.BooleanField(default=False)


	#this is used by the admin page
	def __str__(self):
		
		return ("ITEM - " + self.item+ 
				" | DESCRIPTION - "+self.description+
				" | STATUS - "+str(self.completed))

