#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:09:01 2020

@author: ryzary
"""


import glassdoor_scraper as gs
import pandas as pd

path = '/Users/ryzary/Desktop/projects/glassdoor/chromedriver'

df = gs.get_jobs('Business Analyst',1000,False,path,2)


df.to_csv('glassdoor_jobs.csv',index=False)
