from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile('^[_a-z0-9-]+(.[_a-z0-9-]+)@[a-z0-9-]+(.[a-z0-9-]+)(.[a-z]{2,4})$')

class LogInManager(models.Manager):
	def validate_and_create_user(self, postData):
		errors = []
		if len(postData['firstname']) < 2:
			errors.append('firstname should be more than two characters.')
			return (False, errors)
		else:

			pw_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			user = self.create(firstname=postData['firstname'], lastname=postData['lastname'], email = postData['email'], password = pw_hash)
			return (True, user)

	def validate_and_login(self, form):
		errors = []
		user = self.get(email = form['email'])
		print "HIHIHI" + user.password + "----" + form['password']
		try:
			print "HIHIHI" + user.password + "----" + form['password']
			if bcrypt.checkpw(form['password'].encode(), user.password.encode()):
				return (True, user)
			else:
				errors.append('Incorrect password')
				return (False, errors)
		except:
			errors.append('Incorrect username or password')
			return (False, errors)
	

class User(models.Model):
	firstname = models.CharField(max_length = 255, default='DEFAULT')
	lastname = models.CharField(max_length = 255, default='DEFAULT')
	email = models.CharField(max_length = 255, default='DEFAULT')
	password = models.CharField(max_length = 255, default='DEFAULT')
	objects = LogInManager()