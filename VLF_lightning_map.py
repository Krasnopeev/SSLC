# -*- coding: utf-8 -*-
"""
Created on Sun May 28 04:33:47 2023

@author: User
"""
import numpy as np
import sys
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.geoaxes import GeoAxes
from matplotlib.axes import Axes
GeoAxes._pcolormesh_patched = Axes.pcolormesh

import os
from datetime import datetime, timedelta
import matplotlib as mpl
#mpl.use('Agg')
#from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
#from windrose import WindroseAxes
from matplotlib import cm
from matplotlib import rc
import matplotlib.lines as lines

import time
mpl.rcParams['lines.color'] = 'k'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])

def draw_map(light_arr, prev_ind, current_ind):
    
    tor_lat = 51.81091944
    tor_lon = 103.07756667
    listv_lat = 51.84633889
    listv_lon = 104.892775
    irk_lat = 52.24820090 
    irk_lon = 104.26507171
    labelsize_1 = 30 
    
    fig_1 = plt.figure(figsize = (25,15))
    ax = fig_1.add_subplot(1,1,1)

    plt.rc('xtick', labelsize = labelsize_1)
    plt.rc('ytick', labelsize = labelsize_1)
    plt.rc('font', size = labelsize_1)          
    plt.rc('axes', titlesize = labelsize_1)     
    plt.rc('axes', labelsize = labelsize_1)

    ax.grid('both')
    ax.set_xlabel("LON")
    ax.set_ylabel('LAT')
    name = str(light_arr['date_light'][prev_ind])
    ax.set_title(name[:10]+" "+ str(light_arr['date_light'][prev_ind])[11:]+"-"+str(light_arr['date_light'][current_ind])[11:])
    ax.set_xlim(95, 115)
    ax.set_ylim(45, 65)
    #ax.set_xlim(80, 120)
    #ax.set_ylim(30, 70)
    
    ax.plot(light_arr['lon'][prev_ind:current_ind], light_arr['lat'][prev_ind:current_ind], 'bo', linewidth = '5.1')
    ax.plot(tor_lon, tor_lat, 'Dr', listv_lon, listv_lat, 'Db', irk_lon, irk_lat, 'Dk', markersize=10)
    fig_1.tight_layout()
    
    
    name = name.replace(':',".")
    plt.savefig('C:\\Users\\User\\Desktop\\test_time_VLF_prog\\png\\lightning_map\\'+name[:10]+"\\"+name+ ".png")
    plt.show()
    plt.clf()        
    plt.close()
    
def draw_true_map(light_arr, prev_ind, current_ind, proj, provinces, 
                  lat_lim_down, lat_lim_up, lon_lim_l, lon_lim_r):
    
    tor_lat = 51.81091944
    tor_lon = 103.07756667
    listv_lat = 51.84633889
    listv_lon = 104.892775
    irk_lat = 52.24820090 
    irk_lon = 104.26507171
    brt_lat = 56.315128
    brt_lon = 101.755536
    
    Lon_lim = [lon_lim_l, lon_lim_r]
    Lat_lim = [lat_lim_down, lat_lim_up] 
    
    fig = plt.figure(figsize = (20,10))
    ax = plt.axes(projection = proj)
    name = str(light_arr['date_light'][prev_ind])
    ax.set_title(name[:10]+" "+ str(light_arr['date_light'][prev_ind])[11:]+"-"+str(light_arr['date_light'][current_ind])[11:])
    ax.set_aspect('equal')
    #extent = [Lon_lim[0], Lon_lim[1], Lat_lim[0], Lat_lim[1]]
    #ax.set_extent([Lon_lim[0]+2, Lon_lim[1]-11, Lat_lim[0]+3, Lat_lim[1]-35])
    ax.set_extent([Lon_lim[0], Lon_lim[1], Lat_lim[0], Lat_lim[1]])
    
    ax.add_feature(provinces)
    
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.LAKES)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.RIVERS)
    ax.add_feature(cfeature.BORDERS)
    ax.gridlines()
    plt.plot(tor_lon, tor_lat, 'Dr', listv_lon, listv_lat, 'Dg', irk_lon, irk_lat, 'Dk', brt_lon, brt_lat, 'Dk', markersize=5, transform = ccrs.PlateCarree())
    plt.plot(light_arr['lon'][prev_ind:current_ind], light_arr['lat'][prev_ind:current_ind], 'bo', linewidth = '3.1',  transform = ccrs.PlateCarree())
            
    stamp = 'Number of pulses: '+str(len(light_arr['lon'][prev_ind:current_ind]))+'\n'
            
    plt.text(ax.get_xlim()[0], ax.get_ylim()[1], stamp, va='top', fontsize = 30)

    #plt.show() 
    fig.tight_layout() 
    name = name.replace(':',".")
    fig.savefig('.'+name[:10]+"\\"+name+ ".png", bbox_inches = 'tight') 
    plt.clf()
    plt.close()
        

### Segment for open .TXT files

# path_open = 'C:\\Users\\User\\Desktop\\test_time_VLF_prog\\tabl_coord_txt\\'
# list_file = os.listdir(path_open)

# for file in list_file[2:3]:
    
#     with open(path_open+str(file), 'r') as f:
#         lines = f.readlines()
#         f.close()
    
#     tabl_tp = np.dtype([('id_num','int32'),('date_light','datetime64[us]'),('lat', 'f4'),('lon','f4'),('Amp','int32'),('Note', 'str')])
#     tabl = np.array([],dtype=tabl_tp)
#     for line in lines[1:]:    
#         new_line = line.split(' ')
#         tabl = np.append(tabl,
#                          np.array((new_line[0], new_line[1], new_line[2], new_line[3], new_line[4], 'None'), 
#                                   dtype=tabl_tp))
#         print(new_line)
        
###

data = '2023-07-15'
window_t_interval = 3 # time for which lightning discharges accumulate (in minutes)
path_open = "data/"
list_file = os.listdir(path_open)

for line in list_file[:]:
    line_new = line.replace('.','-')
    if line_new[:10] == data:
        print("File exist. Success!")
        data_tabl = np.load(path_open+line)
        tabl = data_tabl['tabl']
        
    if line_new[15:-4] == data:
        print("File exist. Success!")
        data_tabl = np.load(path_open+line)
        tabl = data_tabl['tabl']
    else:
        print("File not found or not exist")

####################################
### Draw graph of Lighning point ###
####################################

provinces_50m = cfeature.NaturalEarthFeature('cultural',
                                             'admin_1_states_provinces_lines',
                                             '50m',
                                             facecolor = 'none')

proj = ccrs.LambertConformal(central_latitude = 40+(70-40)/2, 
                             central_longitude = 30+(160-30)/2,
                             standard_parallels = (2, 2))

prv_ind = 0
prv = 0

for i, num in enumerate(tabl):
    idx = (num['date_light'] - num['date_light'].astype('datetime64[D]').astype('datetime64[s]')).astype('i8')//(1e6*60*window_t_interval)
    if (idx - prv_ind) >= 1:
        #draw_true_map(tabl, prv, i, proj, provinces_50m, 50, 60, 95, 110) 
        draw_true_map(tabl, prv, i, proj, provinces_50m, 45, 65, 90, 120)
        #draw_map(tabl, prv, i)
    
        prv = i
        prv_ind = idx



        

    

         