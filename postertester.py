# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 09:51:37 2019

@author: DWrenne
"""

#change this
sumoendpoint  = 'https://endpoint1.collection.sumologic.com/receiver/v1/http/xxxxxxxxxxxxxxxxxx'


from SumoPoster import Poster

mynewposter = Poster(sumoendpoint)

data = {}
data['firstname'] = 'Diarmuid'
data['surname'] = 'Wrenne'

mynewposter.post(data)
