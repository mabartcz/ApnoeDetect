# AD_lunch - toolkit for apnoe and desat detection
# Martin Barton 2020 FBMI CVUT, NUDZ
# ma.barton@seznam.cz

from __future__ import print_function

import sys
import struct
import os
import scipy
import traceback
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
from shutil import copy
from dfileTK import *
import pickle
from scipy import stats

import numpy as np
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv1D, GlobalAveragePooling1D, MaxPooling1D
from keras.utils import plot_model
import matplotlib.pyplot as plt
from keras_sequential_ascii import keras2ascii

def The_answer(real, predict, text):
    # Pocitani vysledku
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for c in range(len(real)):
        if real[c] == 1 and predict[c] == 1:
            TP += 1
        elif real[c] == 0 and predict[c] == 0:
            TN += 1
        elif real[c] == 0 and predict[c] == 1:
            FP += 1
        elif real[c] == 1 and predict[c] == 0:
            FN += 1

    print(str(text))
    print("TP: " + str(TP))
    print("TN: " + str(TN))
    print("FP: " + str(FP))
    print("FN: " + str(FN))
    print("Sensitivity:\t" + str(round(((TP) / (TP + FN)) * 100, 2)) + " %")
    print("Specificity:\t" + str(round(((TN) / (TN + FP)) * 100, 2)) + " %")
    print("Accuracy:\t\t" + str(round(((TP + TN) / (TP + TN + FP + FN)) * 100, 2)) + " %")


def apnoe_detection(new_file):
    #-------Detekce Apnoe------------------------------------------------------------------------------
    # Nacteni dat
    data = DFile(new_file)
    #data.tag_info()
    #data.chan_info()

    # Preprocess (filtrace, outliers, segmentace, ...)
    data_segments, data_tags = data.preprocess_flow_slide()
    print("Preprocess done.")

    model = load_model("flow_model_200_nice.h5")

    keras2ascii(model)
    print("Keras model loaded")

    X_data = np.expand_dims(data_segments, 2)
    print("Apnoe detection done.")
    y_data = model.predict(X_data, 128, verbose=1)

    print(sum(y_data))
    print(y_data[0:20])

    #Rozhodovaci hladinka
    for count, ele in enumerate(y_data):
        if ele < 0.9:
            y_data[count] = 0
        else:
            y_data[count] = 1

    #The_answer(data_tags[:,0],y_data, "1D CNN results" )

    y_data = np.squeeze(y_data)
    data_tags[:, 0] = y_data
    #Prevedeni dat k ulozeni
    tags = tag_seg2tags_slide(data_tags, "O+", "O-")

    AP_total = int(np.shape(tags)[0]/2)


    # Ulozeni do .d file
    data.save_tags(tags, s_class=100, e_class=101, s_tag="O+", e_tag="O-")
    print("Tags saved to file.")

    # orig_s = data.tag_orig_s
    # orig_e = data.tag_orig_e
    # compare2tag_sets(orig_s,orig_e,tags)
    #--------------------------------------------------------------------------------------------------

    return AP_total

def saturation_detection(new_file):
    #-------Detekce spo2------------------------------------------------------------------------------
    # Nacteni dat
    data = DFile(new_file)
    #data.tag_info()
    #data.chan_info()

    # Preprocess (filtrace, outliers, segmentace, ...)
    data_segments, data_tags = data.preprocess_spo2_slide()
    print("Probehlo zpracovani dat.")

    model = load_model("spo2_model_200.h5")
    keras2ascii(model)
    print("Nacten Keras model")

    X_data = np.expand_dims(data_segments, 2)
    print("Zacatek detekce apnoe.")
    y_data = model.predict(X_data, 128, verbose=1)

    #Rozhodovaci hladinka
    for count, ele in enumerate(y_data):
        if ele < 0.8:
            y_data[count] = 0
        else:
            y_data[count] = 1

    # The_answer(data_tags[:,0],y_data, "1D CNN results" )

    y_data = np.squeeze(y_data)
    data_tags[:, 0] = y_data


    #Prevedeni dat k ulozeni
    tags = tag_seg2tags_slide(data_tags, "S+", "S-")

    SP_total = int(np.shape(tags)[0]/2)

    # Ulozeni do .d file
    data.save_tags(tags, s_class=102, e_class=103, s_tag="S+", e_tag="S-")
    print("Tags saved to file.")

    #--------------------------------------------------------------------------------------------------

    return SP_total

def init_copy(file_path):
    # Kontrola jestli je vlozen .d file
    if not file_path.endswith(".d"):
        sys.exit("Not .d file !")

    # Zkopiruje .d file do stejneho umisteni s priponou _AUTO.d
    new_file = file_path[0:-2] + "_AUTO.d"
    copy(file_path,new_file)
    print("Copy finished.")

    return new_file
