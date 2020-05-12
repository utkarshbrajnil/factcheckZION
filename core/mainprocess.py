#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:38:43 2020

@author: aditya
"""


from twitterprocess import top_results
from twitterprocess import to_verify

from verifieduser import verify_list


msg="narendramodi"
df1 = top_results(msg)
list1 = to_verify(df1)
df2 = verify_list(list1)
tweet_list= df1["text"].tolist()
verans0 = df2.loc[list1[0],"verified"]

#outputlist=['*Topic :*' , msg , '||'  , '*Username :*', list1[0] , '||' , '*Tweet :*' , tweet_list[0] , '*Verified :*' , ]
#outputstr=''.join(outputlist)
#print (outputstr)


