# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:23:00 2019

@author: Joseph
Defines URL patterns for learning_logs.
"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
		#Home page
		path('', views.index, name='index'),
]