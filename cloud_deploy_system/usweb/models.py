#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
File Name: models.py
Author: shalk 
Mail: shalk@qq.com
Created Time: 2016-10-09 09:58:27
Description: 
"""
from django.db import models

class  AnsibleAdHoc(models.Model):
    name = models.CharField(max_length=50)
    host_pattern =  models.CharField(max_length=100)
    module = models.CharField(max_length=30)
    args =  models.CharField(max_length=300)
    host_file = models.CharField(max_length=50)

class CloudManager(models.Model):
    name = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class BashAdHoc(models.Model):
    name = models.CharField(max_length=50)
    cmd =  models.CharField(max_length=300)
     
     
class Files(models.Model):
    name = models.CharField(max_length=50)
    path = models.CharField(max_length=200)

