import datetime as dt  # Python standard library datetime  module
import numpy as np
from netCDF4 import Dataset  # http://code.google.com/p/netcdf4-python/
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy
import cartopy.feature as cfeature
from osgeo import gdal
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
gdal.SetConfigOption('GRIB_NORMALIZE_UNITS', 'NO')

nc_f = 'C:\\Users\\Public\\Documents\\hrrr.t12z.wrfsfcf00.nc'  # Your filename
nc_fid = Dataset(nc_f, 'r')  # Dataset is the class behavior to open the file
                             # and create an instance of the ncCDF4 class
                             
# Extract data from NetCDF file
lats = nc_fid.variables['gridlat_0'][:]  # extract/copy the data
lons = nc_fid.variables['gridlon_0'][:]
temp = nc_fid.variables['TMP_P0_L103_GLC0'][:]

fig = plt.figure(figsize=(20, 20))

latitude_south = 21.13812 
latitude_north = 47.84219 
longitude_west = -134.0955 
longitude_east = -60.91719

states_provinces = cfeature.NaturalEarthFeature(category='cultural', name='admin_1_states_provinces_lines',scale='50m', facecolor='none')


proj = ccrs.LambertConformal()
ax = plt.axes(projection=proj)
#ax.set_extent([longitude_west,longitude_east,latitude_south,latitude_north])

plt.pcolormesh(lons, lats, temp, transform=ccrs.PlateCarree(), cmap='RdYlBu_r',zorder=1)
ax.add_feature(cartopy.feature.BORDERS, linestyle=':', zorder=2)
ax.add_feature(states_provinces, edgecolor='black')
ax.coastlines()
ax.axes.autoscale(True)


plt.colorbar(orientation='horizontal')

plt.show()
