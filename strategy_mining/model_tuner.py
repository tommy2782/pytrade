#!/usr/bin/env python
# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import math
from math import log
from sklearn import metrics,preprocessing,cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.linear_model as lm
import pandas as p
from time import gmtime, strftime
import scipy
import sys
import sklearn.decomposition
from sklearn.metrics import mean_squared_error
from string import punctuation
from sklearn.neighbors import RadiusNeighborsRegressor, KNeighborsRegressor
import time
from scipy import sparse
from itertools import combinations
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, ExtraTreesClassifier
import operator
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn import svm
from sklearn import tree
from sklearn import linear_model, metrics
from sklearn.neural_network import BernoulliRBM
from sklearn.pipeline import Pipeline
# parse the command paramaters
from optparse import OptionParser
from model_base import get_date_str

def main(options, args):
    if options.utildate == None:
        options.utildate = get_date_str()
    fsampleY = open(options.input + "/" + options.utildate + "/train.csv", "r")
    l_X = []
    l_y = []

    for line in fsampleY:
        tokens = line.split(",")
        features = []
        for i in range(len(tokens)):
            if i < len(tokens)-1:
                features.append(float(tokens[i]))
            else:
                l_y.append(int(tokens[i]))
        l_X.append(features)
    X = np.array(l_X)
    y = np.array(l_y)
    assert(X.shape[0] == y.shape[0])
    if int(options.short) > 0:
        print "using short data for test purpose"
        X = X[0:int(options.short)]
        y = y[0:int(options.short)]
    
    print "preparing models"
    if options.isregress == True:
        model_predictor = GradientBoostingRegressor(max_features=0.6, learning_rate = 0.05, max_depth=5, n_estimators=300)
    else :
        model_predictor = GradientBoostingClassifier(max_features=0.6, learning_rate=0.05, max_depth=5, n_estimators=300)
    #model_predictor = GradientBoostingClassifier()
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.3, random_state=0)
    # print cross_validation.cross_val_score(model_predictor, X, y)
    clf = model_predictor.fit(X_train, y_train)

    if options.isregress:
        pred = model_predictor.predict(X_test)
    else:
        pred = model_predictor.predict_proba(X_test)
#    tpred = model_predictor.predict(X_test)
 #   score = model_predictor.score(X_test, tpred)
 #   print "score=", score
    assert(len(pred) == X_test.shape[0])
    dpred = {}
    for i in range(len(pred)):
        if options.isregress:
            dpred[i] = pred[i]
        else:
            dpred[i] = pred[i,1]
    dpred = sorted(dpred.iteritems(),key=operator.itemgetter(1))
    tp5 =0
    p5 = 0
    tp7 = 0
    p7 = 0
    tp6 = 0
    p6 = 0
    tp8 = 0
    p8 = 0
    tp9 = 0
    p9 = 0
    for preds in dpred:
        if preds[1] > 0.5:
            p5 += 1
            if y_test[preds[0]] == 1:
                tp5 +=1
        if preds[1] > 0.6:
            p6 +=1
            if y_test[preds[0]] == 1:
                tp6 += 1
        if preds[1] > 0.65:
            p7 +=1
            if y_test[preds[0]] == 1:
                tp7 += 1
        if preds[1] > 0.8:
            p8 +=1
            if y_test[preds[0]] == 1:
                tp8 += 1
        if preds[1] > 0.98:
            p9 +=1
            if y_test[preds[0]] == 1:
                tp9 += 1
    if p5 > 0 :  print "threshold 0.5:", tp5*1.0/p5, p5
    if p6 > 0 :  print "threshold 0.6:", tp6*1.0/p6, p6
    if p7 > 0 :  print "threshold 0.65:", tp7*1.0/p7, p7
    if p8 > 0 :  print "threshold 0.8:", tp8*1.0/p8, p8
    if p9 > 0 :  print "threshold 0.98:", tp9*1.0/p9, p9


    if options.isregress :
        pred = model_predictor.predict(X_train)
    else:
        pred = model_predictor.predict_proba(X_train)
    dpred = {}
    for i in range(len(pred)):
        if options.isregress:
            dpred[i] = pred[i]
        else:
            dpred[i] = pred[i,1]
    dpred = sorted(dpred.iteritems(),key=operator.itemgetter(1))
    tp5 =0
    p5 = 0
    tp7 = 0
    p7 = 0
    tp6 = 0
    p6 = 0
    tp8 = 0
    p8 = 0
    tp9 = 0
    p9 = 0
    for preds in dpred:
        if preds[1] > 0.5:
            p5 += 1
            if y_train[preds[0]] == 1:
                tp5 +=1
        if preds[1] > 0.6:
            p6 +=1
            if y_train[preds[0]] == 1:
                tp6 += 1
        if preds[1] > 0.65:
            p7 +=1
            if y_train[preds[0]] == 1:
                tp7 += 1
        if preds[1] > 0.8:
            p8 +=1
            if y_train[preds[0]] == 1:
                tp8 += 1
        if preds[1] > 0.98:
            p9 +=1
            if y_train[preds[0]] == 1:
                tp9 += 1
    if p5 > 0 :  print tp5*1.0/p5, p5
    if p6 > 0 :  print tp6*1.0/p6, p6
    if p7 > 0 :  print tp7*1.0/p7, p7
    if p8 > 0 :  print tp8*1.0/p8, p8
    if p9 > 0 :  print tp9*1.0/p9, p9

    #{{{ prediction
    print "prediction ..."
    stock_predict_out = file(options.input + "/" + options.utildate + "/predict.csv", "w")
    for line in file(options.input + "/" + options.utildate + "/last.csv", "r"):
        tokens = line.split(",")
        l_features = []
        for i in range(len(tokens)):
            if 0 == i:
                print >> stock_predict_out, "%s," % tokens[i],
            elif 1 == i:
                print >> stock_predict_out, "%s," % tokens[i],
            else:
                l_features.append(float(tokens[i].strip()))
        l_features2 = []
        l_features2.append(l_features)
        np_features = np.array(l_features2)
        if np_features.shape[1] != X.shape[1] :
            assert(false)
        if options.isregress:
            pred = model_predictor.predict(np_features)
            print >> stock_predict_out, "%f" % pred
        else:
            pred = model_predictor.predict_proba(np_features)
            print >> stock_predict_out, "%f" % pred[0,1]
    stock_predict_out.close()

    #}}}

def parse_options(paraser): # {{{
    """
    parser command line
    """
    parser.add_option("--input", dest="input",action = "store", default="data/prices_series/", help = "the input filename dir")
    parser.add_option("--short", dest="short",action = "store", default=-1, help = "using short data")
    parser.add_option("--utildate", dest="utildate",action = "store", default=None, help = "the last date to train")
    parser.add_option("--isregress", dest="isregress",action = "store_true", default=True, help = "using repgress model or classify?")
    return parser.parse_args()
#}}} 

# execute start here
if __name__ == "__main__": #{{{
    parser = OptionParser()
    (options, args) = parse_options(parser)
    main(options, args)
# }}}
