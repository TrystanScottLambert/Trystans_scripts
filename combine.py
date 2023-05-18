#!/usr/bin/python3.10
""" Script to combine all images in the SCIENCE FOLDER """

import glob
from astropy.io import fits
from reproject.mosaicking import find_optimal_celestial_wcs
from reproject import reproject_interp
from reproject.mosaicking import reproject_and_coadd

if __name__ == '__main__':
	FOLDER = 'SCIENCE/'
	files = glob.glob(FOLDER + '*.fits')
	hdus = [fits.open(_file) for _file in files]
	wcs_out, shape_out = find_optimal_celestial_wcs(hdus)
	array, footprint = reproject_and_coadd(hdus,
                                       wcs_out, shape_out=shape_out,
                                       reproject_function=reproject_interp)

	fits.writeto('combined.fits', array, hdus[0][0].header, overwrite=True)

