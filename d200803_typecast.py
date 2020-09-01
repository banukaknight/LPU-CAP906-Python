# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:39:07 2020

@author: banuk
"""
var1 = 123
var2 = "456"
var3 = 12.34
var4 = 'hello'
var5 = True
var6 = 3 + 4j


def printvar():
    print(var1, type(var1))
    print(var5, type(var5))
    print(var6, type(var6))

printvar()

var5 = str(var5)


printvar()