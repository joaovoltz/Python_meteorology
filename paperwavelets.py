# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 01:30:22 2024

@author: voltz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pywt
from statsmodels.robust import mad

###############################################################################
df = pd.read_hdf(r'D:\Dados_SM\Richard_Rn.hdf')
#Conversão diária
dfc = df.resample('d', convention='end').mean()

df2 = pd.read_csv(r'D:\Dados_SM\Dados_SM_2015_2023.csv', index_col=0, parse_dates=(True))
#Conversão diária
dfd = df2.resample('d', convention='end').mean()

#plt.plot(dfd['NEE_uStar_f']) # Observar variável
###############################################################################

# Load CO2 flux data 2015 JAN - MAR
c2015 = (dfc['2015-01-01':'2015-03-31'])
sigma1 = mad(c2015['NEE_uStar_f']) #Campari?

# Define the mother wavelet
mother1 = pywt.ContinuousWavelet('morl')

# Define the scales to use in the analysis
scales = np.arange(1, 128)

# Perform the wavelet transform
wavelet_coeffs1, _ = pywt.cwt(c2015['NEE_uStar_f'], scales, mother1)

# Calculate the power spectrum
power1 = (abs(wavelet_coeffs1)) ** 2

# Calculate the global wavelet spectrum
global_power1 = power1.sum(axis=1)

# Calculate the period and scale
period = 1 / scales
scale = scales * np.ones((dfc.shape[0], 1))

###############################################################################
# Load CO2 flux data 2015 ABR - JUN
d2015 = (dfc['2015-04-01':'2015-06-30'])

sigma2 = mad(d2015['NEE_uStar_f']) #Campari?

# Define the mother wavelet
mother2 = pywt.ContinuousWavelet('morl')

# Define the scales to use in the analysis
scales = np.arange(1, 128)

# Perform the wavelet transform
wavelet_coeffs2, _ = pywt.cwt(d2015['NEE_uStar_f'], scales, mother2)

# Calculate the power spectrum
power2 = (abs(wavelet_coeffs2)) ** 2

# Calculate the global wavelet spectrum
global_power2 = power2.sum(axis=1)

# Calculate the period and scale
period = 1 / scales
scale = scales * np.ones((dfc.shape[0], 1))
###############################################################################
# Load CO2 flux data 2015 JUL - SET
e2015 = (dfc['2015-06-01':'2015-09-30'])
sigma3 = mad(e2015['NEE_uStar_f']) #Campari?

# Define the mother wavelet
mother3 = pywt.ContinuousWavelet('morl')

# Define the scales to use in the analysis
scales = np.arange(1, 128)

# Perform the wavelet transform
wavelet_coeffs3, _ = pywt.cwt(e2015['NEE_uStar_f'], scales, mother3)

# Calculate the power spectrum
power3 = (abs(wavelet_coeffs3)) ** 2

# Calculate the global wavelet spectrum
global_power3 = power3.sum(axis=1)

# Calculate the period and scale
period = 1 / scales
scale = scales * np.ones((dfc.shape[0], 1))
###############################################################################
# Load CO2 flux data 2015 OUT - DEZ
f2015 = (dfc['2015-10-01':'2015-12-31'])
sigma4 = mad(f2015['NEE_uStar_f']) #Campari?

# Define the mother wavelet
mother4 = pywt.ContinuousWavelet('morl')

# Define the scales to use in the analysis
scales = np.arange(1, 128)

# Perform the wavelet transform
wavelet_coeffs4, _ = pywt.cwt(f2015['NEE_uStar_f'], scales, mother4)

# Calculate the power spectrum
power4 = (abs(wavelet_coeffs4)) ** 2

# Calculate the global wavelet spectrum
global_power4 = power4.sum(axis=1)

# Calculate the period and scale
period = 1 / scales
scale = scales * np.ones((dfc.shape[0], 1))
###############################################################################
###############################################################################
# Load CO2 flux data 2022 JAN - MAR
c2022 = (dfd['2022-01-01':'2022-03-31'])
sigma5 = mad(c2015['NEE_uStar_f']) #Campari?

# Define the mother wavelet
mother5 = pywt.ContinuousWavelet('morl')

# Define the scales to use in the analysis
scales = np.arange(1, 128)

# Perform the wavelet transform
wavelet_coeffs5, _ = pywt.cwt(c2022['NEE_uStar_f'], scales, mother5)

# Calculate the power spectrum
power5 = (abs(wavelet_coeffs5)) ** 2

# Calculate the global wavelet spectrum
global_power5 = power5.sum(axis=1)

# Calculate the period and scale
period = 1 / scales
scale = scales * np.ones((dfc.shape[0], 1))

###############################################################################
# Load CO2 flux data 2022 ABR - JUN
d2022 = (dfd['2022-04-01':'2022-06-30'])

sigma6 = mad(d2022['NEE_uStar_f']) #Campari?

# Define the mother wavelet
mother6 = pywt.ContinuousWavelet('morl')

# Define the scales to use in the analysis
scales = np.arange(1, 128)

# Perform the wavelet transform
wavelet_coeffs6, _ = pywt.cwt(d2022['NEE_uStar_f'], scales, mother6)

# Calculate the power spectrum
power6 = (abs(wavelet_coeffs6)) ** 2

# Calculate the global wavelet spectrum
global_power6 = power6.sum(axis=1)

# Calculate the period and scale
period = 1 / scales
scale = scales * np.ones((dfc.shape[0], 1))
###############################################################################
# Load CO2 flux data 2022 JUL - SET
e2022 = (dfd['2022-06-01':'2022-09-30'])
sigma7 = mad(e2022['NEE_uStar_f']) #Campari?

# Define the mother wavelet
mother7 = pywt.ContinuousWavelet('morl')

# Define the scales to use in the analysis
scales = np.arange(1, 128)

# Perform the wavelet transform
wavelet_coeffs7, _ = pywt.cwt(e2022['NEE_uStar_f'], scales, mother7)

# Calculate the power spectrum
power7 = (abs(wavelet_coeffs7)) ** 2

# Calculate the global wavelet spectrum
global_power7 = power7.sum(axis=1)

# Calculate the period and scale
period = 1 / scales
scale = scales * np.ones((dfc.shape[0], 1))
###############################################################################
# Load CO2 flux data 2022 OUT - DEZ
f2022 = (dfd['2022-10-01':'2022-12-31'])
sigma8 = mad(f2022['NEE_uStar_f']) #Campari?

# Define the mother wavelet
mother8 = pywt.ContinuousWavelet('morl')

# Define the scales to use in the analysis
scales = np.arange(1, 128)

# Perform the wavelet transform
wavelet_coeffs8, _ = pywt.cwt(f2022['NEE_uStar_f'], scales, mother8)

# Calculate the power spectrum
power8 = (abs(wavelet_coeffs8)) ** 2

# Calculate the global wavelet spectrum
global_power8 = power8.sum(axis=1)

# Calculate the period and scale
period = 1 / scales
scale = scales * np.ones((dfc.shape[0], 1))

###############################################################################

#Plot the wavelet power spectrum
fig, axs = plt.subplots(2, 4, figsize=(10, 16))
#2015
axs[0,0].contourf(c2015.index, np.log2(period), np.log2(power1), cmap='YlOrRd')
axs[0,0].set_xlabel('Time')
axs[0,0].set_xticks([])
axs[0,0].set_xlabel('Jan - Mar')

axs[0,1].contourf(d2015.index, np.log2(period), np.log2(power2), cmap='YlOrRd')
axs[0,1].set_xlabel('Time')
axs[0,1].set_xlabel('Apr - Jun')
axs[0,1].set_xticks([])

axs[0,2].contourf(e2015.index, np.log2(period), np.log2(power3), cmap='YlOrRd')
axs[0,2].set_xlabel('Time')
axs[0,2].set_xlabel('Jul - Set')
axs[0,2].set_xticks([])

axs[0,3].contourf(f2015.index, np.log2(period), np.log2(power4), cmap='YlOrRd')
axs[0,3].set_xlabel('Time')
axs[0,3].set_xlabel('Oct - Dec')
axs[0,3].set_xticks([])

#2021
axs[1,0].contourf(c2022.index, np.log2(period), np.log2(power5), cmap='YlOrRd')
axs[1,0].set_xlabel('Time')
axs[1,0].set_xticks([])
axs[1,0].set_xlabel('Jan - Mar')

axs[1,1].contourf(d2022.index, np.log2(period), np.log2(power6), cmap='YlOrRd')
axs[1,1].set_xlabel('Time')
axs[1,1].set_xticks([])
axs[1,1].set_xlabel('Apr - Jun')

axs[1,2].contourf(e2022.index, np.log2(period), np.log2(power7), cmap='YlOrRd')
axs[1,2].set_xlabel('Time')
axs[1,2].set_xticks([])
axs[1,2].set_xlabel('Jul - Set')

axs[1,3].contourf(f2022.index, np.log2(period), np.log2(power8), cmap='YlOrRd')
axs[1,3].set_xlabel('Time')
axs[1,3].set_xticks([])
axs[1,3].set_xlabel('Oct - Dec')