#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 02:58:32 2021

@author: toor
"""

# Python program for KMP Algorithm
def chercherSub(substring, String): # string // string
    
    M = len(substring)
    N = len(String)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(substring, M, lps)
  
    i = 0 # index for String[]
    while i < N:
        if substring[j] == String[i]:
            i += 1
            j += 1
  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and substring[j] != String[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
  
def computeLPSArray(substring, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if substring[i]== substring[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
  

# This code is contributed by Bhavya Jain

if __name__ == "__main__":
    String = "ABABDABACDABABCABAB"
    substring = "ABABCABAB"
    tab = chercherSub(substring, String)
    
    