import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n_bins = 15
Mfv = 75.09

def get_off_data(OFF_1day,T_off):
    return OFF_1day*T_off

def get_azimov_error(OFF_1day,T_off,T_on):    
    return np.sqrt((OFF_1day*T_off)*(T_on/T_off)**2 + OFF_1day*T_on)

def get_signal_data(table_data,spectrum,T_on):
    signal = np.zeros(45)
    for T,sp in zip(spectrum['T[keV]'], spectrum['spectrum']):
        if T>=0.:
            str_T = int(np.round(T*1e3))/1e3
            try:
                signal = signal+T_on*table_data[str_T]*sp
            except:
                print (f'No data for {str_T} keV')
    return signal

def get_chi2(x, mu, error):
    return sum(((x-mu)**2)/(error**2))