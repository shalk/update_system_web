#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
File Name: form.py
Author: shalk 
Mail: shalk@qq.com
Created Time: 2016-10-08 15:19:46
Description: 
"""
from django import forms
class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
