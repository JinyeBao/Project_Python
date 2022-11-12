#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 18:10:26 2022

@author: zhoujianfeng
"""
import math
def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        return 0
    low = math.inf
    max_dif = -math.inf
    for i in stock_prices:
        max_dif = max(max_dif, i-low)
        low = min(low, i)
    return max_dif

stock_prices = [10,7,5,8,9,11,12]
print(get_max_profit(stock_prices))


def get_max_product(list_of_ints):
    if len(list_of_ints) < 3:
        return False
    max_ = max(list_of_ints[0], list_of_ints[1])
    max_2 = list_of_ints[0]*list_of_ints[1]
    max_product = - math.inf
    low_ = min(list_of_ints[0], list_of_ints[1])
    low_2 = max_2
    for i in range(2, len(list_of_ints)):
        max_product = max(max_product, max_2 * list_of_ints[i])
        max_2 = max(max_2, list_of_ints[i] * max_)
        max_ = max(max_, list_of_ints[i])
        low_2 = max(low_2, list_of_ints[i] * low_)
        low_ = min(low_, list_of_ints[i])
    return max(max_product, low_2 * max_)

s = [-10,7,5,8,9,-11,-12]    
print(get_max_product(s))
    

def get_products_of_all_ints_except_at_index(list_int):
    list_product = []
    for i in range(len(list_int)):
        product_before = 1
        product_after = 1
        for j in range(0,i):
            product_before *= list_int[j]
        for u in range(i+1,len(list_int)):
            product_after *= list_int[u]
        list_product.append(product_before * product_after)
    return list_product

print(get_products_of_all_ints_except_at_index([1,7,3,4]))


    
    
