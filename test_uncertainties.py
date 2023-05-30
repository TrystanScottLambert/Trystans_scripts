"""
Testing uncertainties
"""

import numpy as np


def k_val(number_counts_in_background, rms_background):
	return number_counts_in_background/(rms_background**2)

def uncertainty(number_counts_in_aperture, number_of_pixels_in_aperture, rms_background, k):
	return ((1./k)*(number_counts_in_aperture) + (number_of_pixels_in_aperture)*(rms_background**2))**(0.5)



#PIXELS_SOURCE = 513
#RMS_BACKGROUND = 0.07 
#COUNTS_SOURCE = 19.357948
#COUNTS_BACKGROUND = 0.6

PIXELS_SOURCE = 717
RMS_BACKGROUND = 1.39
COUNTS_BACKGROUND = 436
COUNT_TOTAL = 400564.69
MAG_ERR = 0.0001

counts_source = COUNT_TOTAL - (PIXELS_SOURCE*COUNTS_BACKGROUND)
snr_sextractor = (2.5/np.log(10))/MAG_ERR


k = k_val(COUNTS_BACKGROUND, RMS_BACKGROUND)
noise = uncertainty(counts_source, PIXELS_SOURCE, RMS_BACKGROUND, k)

print('Uncertainty is: ', noise)
print('SNR: ', counts_source/noise)
print('snr_sextractor', snr_sextractor)