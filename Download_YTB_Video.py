# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 07:56:32 2022

@author: Samson Thibaut
"""

import pywhatkit as pw
from pytube import YouTube

# step 1 : create object from youtube class
yt = YouTube("https://www.youtube.com/watch?v=KErqMcZR0KA")

# step 2 : download the video very quickly
yt.streams.get_highest_resolution().download()


