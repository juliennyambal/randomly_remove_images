#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:34:28 2017

@author: julien
"""

import numpy as np
import os
import random

import argparse

# construct the argument parse and parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", required=True, help="Path to the images")
ap.add_argument("-n", "--numimages", required=True, help="Number of images to deletes")
args = vars(ap.parse_args())


#path = os.getcwd()
#i_path = path+'/0'

print "Path of action: ", args["path"]
print "Number of images to delete: ", args["numimages"]

images  = os.listdir(args["path"])
#if 'random.py' in images:
#    print os.remove('random.py')
#else:
#    print 'not there'
index = np.random.permutation(len(images))
#for i in range(len(images)):
#    index.append(np.random.randint(len(images)))

#6041 is the number of images from the vacant set. The gaol is to have
#balanced datasets

number_to_remove = int(args["numimages"])

to_throw = index[:number_to_remove]

#check the order of the path to the file
for idx in to_throw:
    #print images[idx]
    os.remove(os.path.join(args["path"],images[idx]))


