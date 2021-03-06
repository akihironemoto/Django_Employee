from django.db import models
from django.utils import timezone


class Department(models.Model):
	"""
	部署名を表すクラス
	"""
	name = models.CharField('部署名', max_length=20)
	created_at = models.DateTimeField('日付', default=timezone.now)

	def __str__(self):
		return self.name


class Club(models.Model):
	"""
	所属しているクラブ活動を表す
	"""
	name = models.CharField('部活名', max_length=20)
	created_at = models.DateTimeField('日付', default=timezone.now)

	def __str__(self):
		return self.name


class Employee(models.Model):
	"""
	社員を表すクラス
	"""
	first_name = models.CharField('名', max_length=20)
	last_name = models.CharField('姓', max_length=20)
	email = models.EmailField('メールアドレス', blank=True)
	department = models.ForeignKey(
		Department, verbose_name='部署', on_delete=models.PROTECT,
	)
	club = models.ManyToManyField(
		Club, verbose_name='部活',
		)
	created_at = models.DateTimeField('日付', default=timezone.now)

	def __str__(self):
		return '{0} {1} {2}'.format(self.last_name, self.first_name, self.department)
