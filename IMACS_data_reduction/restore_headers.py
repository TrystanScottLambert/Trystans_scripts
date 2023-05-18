"""
Script to change theli headers into raw headers so that we can then use manaully determine the wcs information.
First use theli to perform the data reduction. Then run this script with the SCIENCE folder. Make sure to 
set Theli to not use its default naming convention. 
"""

import glob
import os
import numpy as np
from astropy.io import fits


raw_files = np.sort(glob.glob('SCIENCE/RAWDATA/*.fits'))
calibrated_files = np.sort(glob.glob('SCIENCE/*.fits'))

for i, old_file in enumerate(raw_files):
	print(f'Updating {calibrated_files[i]} with {old_file}')
	hdul_raw = fits.open(old_file)
	hdul_calibrated = fits.open(calibrated_files[i])

	hdul_calibrated[0].header = hdul_raw[0].header
	hdul_calibrated.writeto(old_file.split('/')[-1], overwrite=True)
	os.remove(calibrated_files[i])
