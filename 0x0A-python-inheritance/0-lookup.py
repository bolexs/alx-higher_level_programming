#!/usr/bin/python3
 """ Function that returns the list of available attributes"""

 
def lookup(obj):
    """list of available attrs and methods of an obj"""
    return dir(obj)
