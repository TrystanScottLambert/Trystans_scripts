"""Simple script to make a straigt line masking of all the weights files."""

import glob
from astropy.io import fits 

broken_chips = [2, 3, 4, 5, 6, 7, 8]
mask_upper_limits = [1000, 1000, 1000, 1000]

def mask_weight(infile: str):
    """cuts out the telescope part of the weights files."""
    hdu = fits.open(infile)
    hdu[0].data[:600] = 0
    hdu.writeto(infile, overwrite=True, output_verify='ignore')

if __name__ == '__main__':
    FOLDER = 'FLATS/'

    for broken_chip in broken_chips:
        files = glob.glob(FOLDER + f'*.fits')

    for file in files:
        mask_weight(file)

