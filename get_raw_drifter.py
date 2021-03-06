# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:32:36 2012

@author: huanxin

This use for plot track of drifter, use ctl file "getcodar_ctl.txt"
"""
#############################################################
#simple project for plotting drifter track
#It gets input value from control file "getcodar_bydrifter_ctl.txt" or  
# a python function "getcodar_ctl_file_py()"
# it could plot and save many pictures.
#Input values:datetime_wanted,filename
#output values:gbox,lat,lon
#function uses:getcodar_ctl_file,getdrift_raw_range_latlon,getdrift_raw
#############################################################
from matplotlib.dates import date2num, num2date
import datetime as dt
import pylab
import sys
import numpy as np
import matplotlib.pyplot as plt
pydir='../'
sys.path.append(pydir)
from drifter_functions import getcodar_ctl_file,getdrift_raw_range_latlon,getdrift_raw
from getcodar_bydrifter_ctl_py import getcodar_ctl_file_py


###############################################
#  read a control file that has user-specified inputs
inputfilename='./getdrifter_ctl.txt'
if inputfilename[-2:]=='py':
  (datetime_wanted,filename,driftnumber,url,model_option,num,interval_dtime,interval,step_size)=getcodar_ctl_file_py()
else:
  (datetime_wanted,filename,driftnumber,url,model_option,num,interval_dtime,interval,step_size)=getcodar_ctl_file(inputfilename)
drifter_id=int(driftnumber)  #change format

# get the geographic box (ie lat/lon ranges)
(maxlon,minlon,maxlat,minlat)=getdrift_raw_range_latlon(filename,drifter_id,interval,datetime_wanted,num,step_size)
for i in range(5):
    if maxlat-minlat<=0.1:
        maxlat=maxlat+0.01
        minlat=minlat-0.01
    if maxlon-minlon<=0.1:
        maxlon=maxlon+0.01
        minlon=minlon-0.01
gbox=[minlon-0.03,maxlon+0.03, minlat-0.03, maxlat+0.03]


for x in range(num): 
  (drifter_data)=getdrift_raw(filename,drifter_id,interval,datetime_wanted)
  lat=drifter_data['lat']
  lon=drifter_data['lon']   
  fig = plt.figure()
  ax = fig.add_subplot(111)   
  plt.title(str(num2date(datetime_wanted).strftime("%d-%b-%Y %H"))+'h')
  lat_wanted=lat[-1]
  lon_wanted=lon[-1]
  plt.plot(lon_wanted,lat_wanted,'.',markersize=30,color='r',label='end')
  
    #plt.plot(np.reshape(lon,np.size(lon)),np.reshape(lat,np.size(lat)))
  plt.plot(np.reshape(lon,np.size(lon)),np.reshape(lat,np.size(lat)),color='black')
    
  #basemap_usgs([minlat-1,maxlat+1],[minlon-1,maxlon+1],'True')
  plt.plot(lon[0],lat[0],'.',markersize=20,color='g',label='start')  # start time
  pylab.ylim([minlat-0.6,maxlat+0.1])
  pylab.xlim([minlon-0.1,maxlon+0.1])
  ax.patch.set_facecolor('lightblue')   #set background color

  plt.legend( numpoints=1,loc=2)  
  plt.savefig('./'+dt.datetime.now().strftime('%Y-%m-%d %H:%M') +'.png')
 
  datetime_wanted=date2num(num2date(datetime_wanted)+datetime.timedelta( 0,step_size*60*60 ))
  plt.show()
