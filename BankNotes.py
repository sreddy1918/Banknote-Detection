# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 21:52:33 2024

@author: sredd
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float