import os
import numpy as np
import pandas as pd
import xarray as xr
from optparse import OptionParser

from estaverage import estimate_daily_average_across_years
from plotdailymean import *

__author__ = 'Eva Sinha'
__email__  = 'eva.sinha@pnnl.gov'

parser = OptionParser();

parser.add_option("--site", dest="site", default="", \
                  help="Site ID")
parser.add_option("--crop", dest="crop", default="", \
                  help="Modeled crop name")
parser.add_option("--rundir", dest="rundir", default="", \
                  help="Directory where ELM ensemble outputs are stored")
parser.add_option("--caseid", dest="caseid", default="", \
                  help="Case name")
parser.add_option("--yr_start", dest="yr_start", default=2000, \
                  help="Start year for reading ELM model outputs")
parser.add_option("--yr_end", dest="yr_end", default=2005, \
                  help="Last year for reading ELM model outputs")
parser.add_option("--obsdir", dest="obsdir", default="", \
                  help="Directory where netcdf file containing observed data is stored")
parser.add_option("--obsfname", dest="obsfname", default="", \
                  help="File name containing observation data")
parser.add_option("--fnamepre", dest="fnamepre", default="", \
                  help="file name prefix for saving comparison plots")

(options, args) = parser.parse_args()

#----------------------------------------------------------
def read_valid_model_data(rundir, caseid, yr_start, yr_end, varnames):
    """Read ELM validation model output for all ensemble members for specified case and year range and subset for variables
    :param: rundir:     path to the run directory
    
    :param: caseid:     case name
    
    :param: yr_start:   first year for reading data
    
    :param: yr_end:     last year for reading data
    
    :param: varnames:   list of variable names of interest

    :return:            single data array containing validation model results for select years and variables
    """

    # Read names of all NetCDF files within the given year range
    fnames = []
    for yr in range(int(yr_start), int(yr_end)+1):
        fnames.append(rundir + '/' + caseid + '.elm.h0.' + str(yr) + '-01-01-00000.nc')
        
    # Open a multiple netCDF data file and load the data into xarrays
    with xr.open_mfdataset(fnames, concat_dim='time') as ds:

        # Drop landgrid dimension
        ds = ds.isel(lndgrid=0)

        # Only keep select variables in the data array
        ds = ds[varnames]

    return (ds)
#----------------------------------------------------------

# List of variable names that we want to keep
varnames = ['GPP', 'ER', 'EFLX_LH_TOT', 'FSH']

# Read ELM validation model output for specified case and year range and subset for variables
ds_model = read_valid_model_data(options.rundir, options.caseid, options.yr_start, options.yr_end, varnames)

# Estimate average across years for each day of the year
ds_model = estimate_daily_average_across_years(ds_model)

# Open a netcdf containing observed data
ds_obs = xr.open_dataset('/home/ac.eva.sinha/ELM-Bioenergy/timeseries_plots/' + options.obsdir + options.obsfname)

# Read list of validation years for the site
valid_yrs = pd.read_csv('../info_obsdata/' + options.site + '_validation_years.csv', comment='#')
valid_yrs = valid_yrs['valid_yrs'].dropna().astype(int)

# Only keep observational data for validation years
ds_obs = ds_obs.sel(time = ds_obs.time.dt.year.isin(valid_yrs))

# Create array of ylabel for each plot
ylabel = ['GPP [$\mathregular{gC~m^{-2}~day^{-1}}$]', 'ER [$\mathregular{gC~m^{-2}~day^{-1}}$]', 'EFLX_LH_TOT [$\mathregular{W~m^{-2}}$]', 'FSH [$\mathregular{W~m^{-2}}$]']

# Title for plot
title = options.crop
site  = options.site

# Conversion constants
CONV_umolCO2_gC = 1.03775
CONV_SEC_DAY    = 1 / (24 * 60 * 60)

conv_fact_model = [CONV_SEC_DAY, CONV_SEC_DAY, 1, 1]
conv_fact_obs   = [CONV_umolCO2_gC, CONV_umolCO2_gC, 1, 1]

subplots_ts_valid_model_obs(ds_model, ds_obs, varnames, title, site, ylabel, conv_fact_model, conv_fact_obs, fname=options.fnamepre)

# ---------- LAI ----------
# Read ELM validation model output for specified case and year range and subset for variables
var      = 'TLAI'
ds_model = read_valid_model_data(options.rundir, options.caseid, options.yr_start, options.yr_end, varnames=[var])

fpath = '/home/ac.eva.sinha/ELM-Bioenergy/obsdata/UIUCEnergyFarm/'
fname = 'UIUC_LAI.csv'

# Site observations file path and file name
obs_data = pd.read_csv(fpath + fname)

# Only keep observational data for validation years
obs_data = obs_data[(obs_data.Year.isin(valid_yrs)) & (obs_data.Site == site)]
print(obs_data.groupby('Year').count())
print(obs_data.groupby('Site').count())

plot_col = 'LAI_avg'
ylabel = 'TLAI'

plot_ts_valid_lai(ds_model, var, obs_data, plot_col, ylabel, title, site, fname=options.fnamepre+ '_valid_lai.png')

# ---------- Canopy height ----------
# Read ELM validation model output for specified case and year range and subset for variables
var      = 'HTOP'
ds_model = read_valid_model_data(options.rundir, options.caseid, options.yr_start, options.yr_end, varnames=[var])

fname = 'UIUC_canopy_height.csv'

# Site observations file path and file name
obs_data = pd.read_csv(fpath + fname)

# Only keep observational data for validation years
obs_data = obs_data[(obs_data.Year.isin(valid_yrs)) & (obs_data.Site == site)]
print(obs_data.groupby('Year').count())
print(obs_data.groupby('Crop').count())

plot_col = 'canopy_height'
ylabel = 'Canopy height [m]'
plot_ts_valid_lai(ds_model, var, obs_data, plot_col, ylabel, title, site, fname=options.fnamepre+ '_valid_canopy_height.png')

# ---------- Harvest ----------
# Read ELM model output for specified case and year range and subset for variables
ds_model = read_valid_model_data(options.rundir, options.caseid, options.yr_start, options.yr_end, varnames=['DMYIELD'])

# Convert to pandas dataframe for writing csv file
df_model = ds_model.to_dataframe()

# Estimate maximum yield for each year
model_dmyield = df_model.groupby(df_model.index.year).max()

# Save to csv file
model_dmyield.to_csv(options.fnamepre + '_DMYIELD.csv', index_label='Year')

fname = 'UIUC_harvest.csv'

# Site observations file path and file name
obs_data = pd.read_csv(fpath + fname)

# Only keep observational data for validation years
obs_data = obs_data[(obs_data.Year.isin(valid_yrs)) & (obs_data.Site == site)]

plot_valid_DMYIELD(model_dmyield, obs_data, title, site, fname=options.fnamepre)
