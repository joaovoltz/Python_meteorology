

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pywt
from statsmodels.robust import mad

# Load CO2 flux data
df = pd.read_csv('/home/voltz/Documentos/joaovoltz/lumet/Dados_SM_2015_2023.csv', index_col=0, parse_dates=True)
dfc = df.resample('d',convention='end').mean()
c2022 = (dfc['2022-01-01':'2022-03-31'])

#plt.plot(dfc['NEE_uStar_f'])

#NEE_uStar_f_mediana = df.NEE_uStar_f.median()
#df.fillna(NEE_uStar_f_mediana, inplace=True)

# Calculate the standard deviation of the data
#dfv = (dfc['2019-01-01':'2019-03-20'])

sigma = mad(c2022['NEE_uStar_f'])


# Define the mother wavelet
mother = pywt.ContinuousWavelet('morl')

# Define the scales to use in the analysis
scales = np.arange(1, 128)

# Perform the wavelet transform
wavelet_coeffs, _ = pywt.cwt(c2022['NEE_uStar_f'], scales, mother)

# Calculate the power spectrum
power = (abs(wavelet_coeffs)) ** 2

# Calculate the global wavelet spectrum
global_power = power.sum(axis=1)

# Calculate the period and scale
period = 1 / scales
scale = scales * np.ones((dfc.shape[0], 1))

 #Plot the wavelet power spectrum
plt.figure(figsize=(10, 6))
plt.contourf(c2022.index, np.log2(period), np.log2(power), cmap='YlOrRd')
plt.colorbar()
plt.xlabel('Time')
plt.ylabel('Period (months)')
plt.title('CO2 Flux Wavelet Power Spectrum')
#plt.ylim(-2.5,0)
# Plot the global wavelet spectrum
plt.figure(figsize=(10, 6))
plt.plot(np.log2(period), np.log2(global_power), linewidth=2)
plt.xlabel('Period (months)')
plt.ylabel('Power')
plt.title('CO2 Flux Global Wavelet Spectrum')

plt.show()