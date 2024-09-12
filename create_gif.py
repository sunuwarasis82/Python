import imageio.v3 as iio
filenames = ['aespa1.jfif', 'aespa2.jfif']
images = []

for filename in filenames:
    images.append(iio.imread(filename))
    
iio.imwrite('aespa.gif', images, duration = 500, loop =0)