#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: anroco

In python how to get a substring of a string?

En python ¿como obtener un substring de un string?
'''

#create a str
s = 'Textual data in Python'
print(s)

#s[start:stop] the start index is inclusive and the end index is exclusive.
s_new = s[8:15]
print(s_new)

#if the start index isn't defined, is taken from the beginning of the string.
s_new = s[-6:]
print(s_new)

#if the end index isn't defined, is taken until the end of the string
s_new = s[:7]
print(s_new)

#if neither is defined, returns the full string
s_new = s[:]
print(s_new)
