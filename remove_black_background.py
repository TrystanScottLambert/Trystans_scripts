"""
Script for removing the black parts of the IMACS f/2 images.
Turns the vignitted part into nans
"""

import glob
import pylab as plt
import numpy as np
from astropy.stats import sigma_clipped_stats
from astropy.io import fits

def remove_modal(data: np.ndarray) -> np.ndarray:
    """
    Converts the modal value of the data to NANs.
    This works because the background black values are 
    all the same number.
    """
    values, counts = np.unique(np.concatenate(data), return_counts=True)
    modal_count = values[np.where(counts==np.max(counts))]
    data[np.where(data == modal_count)] = np.nan
    return data

def remove_carriage(data: np.ndarray) -> np.ndarray:
    """Determines a lower limit that is removed from the images."""
    _, median, std = sigma_clipped_stats(data, sigma=5)
    lower_limit = median  - (10 * std)
    data[np.where(data < lower_limit)] = np.nan
    return data

def correct_vignette(file_name: str) -> None:
    """Perform the two step process to remove the background and carriage from the images."""
    hdu = fits.open(file_name)
    no_back = remove_modal(hdu[0].data)
    no_carriage = remove_carriage(no_back)
    hdu[0].data = no_carriage
    hdu.writeto(file_name, overwrite=True)


if __name__ == '__main__':
    DIR = '/home/tlambert/Desktop/IMACS_analysis/IMACS_RAWDATA/ut211024_25/SCIENCE/'

    files = glob.glob(f'{DIR}*.fits')
    for file in files:
        print(f'correcting {file}')
        correct_vignette(file)
        
