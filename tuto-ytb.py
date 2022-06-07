# -*- coding: utf-8 -*-
"""
Created on Wed May 18 23:09:25 2022

@author: Samson Thibaut
"""

from pytube import YouTube

print('Download started')
YouTube('https://www.youtube.com/watch?v=WXfTq4c9JmE').streams.filter(res='720p').first().download()
print('Download ended')
