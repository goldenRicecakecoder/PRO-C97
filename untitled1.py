# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eYUxO20tCe9-7cpmZu4j_4H6P71aTXro
"""

year = 450
if(year % 4 == 0 and year % 100 != 0 or year % 400==0):
  print("This year is a leap year")
else:
  print("This year isint a leap year")