#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:12:59 2022

@author: zhoujianfeng
"""

#Hash Table
#Q1
def MovieChooser (flight_length, movie_lengths):
    for i in range(0, len(movie_lengths)):
        for j in range(i+1, len(movie_lengths)):
            if movie_lengths[i]+ movie_lengths[j] == flight_length:
                return True
    return False


fl = 240
ml = [120,138,117,240]
print (MovieChooser(fl,ml))



#Q2
def PermutationPanlindrome(str_1):
    str_2 = set()
    for i in str_1:
        if i != ',' and i != ' ' :
            if i in str_2:
                str_2.remove(i)
            else:
                str_2.add(i)
    if len(str_2) > 1:
        return False
    return True
            
            
print(PermutationPanlindrome('civic')) 
print(PermutationPanlindrome('ivicc'))             
print(PermutationPanlindrome('civil'))       
print(PermutationPanlindrome('livci'))           

#Q3(Regular expression operation)
import re
#result = re.sub(pattern, repl, string, count=0, flags=0)
def WordCloud(sample):
    sample = re.sub('[^A-Za-z0-9]+',' ', sample.lower())
    dict_sample = dict()
    list_sample = sample.split(' ')
    for i in list_sample:
        if i not in dict_sample:
            dict_sample[i] = 1
        else:
            dict_sample[i] += 1
    return dict_sample

sample = 'Dada Nexus Limited (NASDAQ: DADA) (“Dada” or the “Company”) is a leading platform for local on-demand retail and delivery in China. The Company operates JD-Daojia (“JDDJ”), one of China’s largest local on-demand retail platforms for retailers and brand owners, and Dada Now, a leading local on-demand delivery platform open to merchants and individual senders across various industries and product categories. The Company’s two platforms are inter-connected and mutually beneficial. The Dada Now platform enables improved delivery experience for participants on the JDDJ platform through its readily accessible fulfillment solutions and strong on-demand delivery infrastructure. Meanwhile, the vast volume of on-demand delivery orders from the JDDJ platform increases order volume and density for the Dada Now platform.'
print (WordCloud(sample))



        
    
    

