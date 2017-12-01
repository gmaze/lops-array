
# coding: utf-8

# # Load NATL60 data on a dask cluster via xarray

# jupyter nbconvert --to script natl60_dask_demo.ipynb
# then uncomment matplotlib lines and make sure time indices are right in the main loop


#get_ipython().run_line_magic('matplotlib', 'inline')

import os
import xarray as xr
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from glob import glob

# from dask.dot import dot_graph
from dask.diagnostics import Profiler, ResourceProfiler, CacheProfiler
from dask.diagnostics import visualize

#from bokeh.io import output_notebook
#output_notebook()


# In[ ]:


from dask.distributed import Client
client = Client(scheduler_file=os.path.expanduser('~/dask/scheduler.json'))
print(client)
print(client._repr_html_())


# In[ ]:


dpath='/home/datawork-lops-osi/data/natl60/NATL60-CJM165/1d/3D/'
filenames = sorted(glob(dpath+'*_gridT.nc'))
print('Number of files available: %d' %len(filenames))

filenames = filenames[:10] # 10000 fails, 5000 passes
print('Number of files processed: %d' %len(filenames))
chunks={'deptht': 1}
chunks={'deptht': 1, 'x': 5422, 'y': 864}
chunks={'deptht': 1, 'x': 5422, 'y':10}

ds = xr.open_mfdataset(filenames, concat_dim='time_counter', chunks=chunks, compat='equals', autoclose=True, lock=True)
#ds = xr.open_mfdataset(filenames, engine='netcdf4', concat_dim='ensemble', chunks={'time': 50})
#mask = xr.open_mfdataset(filenames,concat_dim='time', compat='equals', autoclose=True, lock=False)['QA']


# In[ ]:


print('ds size in GB {:0.2f}\n'.format(ds.nbytes / 1e9))
ds.info()


# In[ ]:


for name, da in ds.data_vars.items():
    print(name, da.data)


# In[ ]:


# We can start by just working with one array, for this example,
# we'll can choose t_mean (average daily air temperature)
temp_surf = ds['votemper'].isel(deptht=0)
print(temp_surf)
dir(temp_surf)
print('temp_surf size in GB {:0.2f}\n'.format(temp_surf.nbytes / 1e9))
temp_mean = temp_surf.mean(dim='time_counter')  # calculates the long term mean along the time dimension

#spread = temp_mean.max(dim='ensemble') - temp_mean.min(dim='ensemble')  # calculates the intra-ensemble range of long term means
#spread


# In[ ]:


out = temp_mean.compute()
print('Mean temperature computed')
#%time out = spread.compute()


# In[ ]:


# a quick figure to prove to ourselves we actually did something
out.plot(robust=True, figsize=(10, 6))
#plt.title('Intra-ensemble range in mean annual temperature')
plt.savefig('t_mean.png')
