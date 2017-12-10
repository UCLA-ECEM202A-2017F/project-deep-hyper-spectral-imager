# -*- coding: utf-8 -*-
#pylint: disable-msg=E0611, E1101, C0103, R0901, R0902, R0903, R0904, W0232
#------------------------------------------------------------------------------
# Copyright (c) 2007-2017, Acoular Development Team.
#------------------------------------------------------------------------------
"""

Loads the three sources test data set, analyzes them and generates a
map of the three sources.

"""
def format_coord(x, y):
     z = x+y
     return 'x=%1.4f, y=%1.4f, z=%1.4f'%(x, y, z)


from os import path
import acoular
from pylab import figure, plot, axis, imshow, colorbar, show
import matplotlib.pyplot as plt

micgeofile = path.join(path.split(acoular.__file__)[0],'xml','mic_geometry.xml')
datafile = '-35,75.h5'

mg = acoular.MicGeom( from_file=micgeofile )
ts = acoular.TimeSamples( name='-35,75.h5' )
ps = acoular.PowerSpectra( time_data=ts, block_size=128, window='Hanning' )
#ps = acoular.EigSpectra( time_data=ts, block_size=128, window='Hanning' )
rg = acoular.RectGrid( x_min=-.715, x_max=.715, y_min=-.44, y_max=.6, z=0.6, \
increment=0.001 )
bb = acoular.BeamformerBase( freq_data=ps, grid=rg, mpos=mg )
#bb = acoular.BeamformerCapon( freq_data=ps, grid=rg, mpos=mg,c=346.04 )
#bb = acoular.BeamformerMusic( freq_data=ps, grid=rg, mpos=mg,c=346.04,n=6 )


pm = bb.synthetic( 8000, 3 )
Lm = acoular.L_p( pm )
#imshow( Lm.T, origin='lower', vmin=Lm.max()-5, extent=rg.extend(), \
#interpolation='bicubic')
#colorbar()
plt.imsave('-35,75', Lm.T, origin='lower',vmin=Lm.max()-3,cmap=plt.cm.get_cmap('Blues', 6))
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow( Lm.T,origin='lower',vmin=Lm.max()-3,extent=rg.extend(),cmap=plt.cm.get_cmap('Blues', 6),interpolation='bicubic')

ax.format_coord = format_coord
plt.show()



figure(2)
plot(mg.mpos[0],mg.mpos[1],'o')
axis('equal')
show()
