from astropy.io import fits

path_red = 'img/red.fits'
path_blue = 'img/blue.fits'
path_green = 'img/green.fits'

red_data = fits.open(path_red)

print red_data.info()
hdu = red_data[0]
print hdu.header
print hdu.header.keys()
print len(hdu.data)
print hdu.data.shape
print hdu.data[0]
