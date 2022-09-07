import os
import numpy as np
import pandas as pd
import xarray as xr
from optparse import OptionParser

from plotdailymean import subplots_ts_model_obs

__author__ = 'Eva Sinha'
__email__  = 'eva.sinha@pnnl.gov'

parser = OptionParser();

parser.add_option("--site", dest="site", default="", \
                  help="Site ID")
parser.add_option("--crop", dest="crop", default="", \
                  help="Modeled crop name")
parser.add_option("--moddir", dest="moddir", default="", \
                  help="Directory where netcdf file containing results for all ELM ensemble members is stored")
parser.add_option("--modfname", dest="modfname", default="", \
                  help="File name containing results for all ELM ensemble members")
parser.add_option("--obsdir", dest="obsdir", default="", \
                  help="Directory where netcdf file containing observed data is stored")
parser.add_option("--obsfname", dest="obsfname", default="", \
                  help="File name containing observation data")
parser.add_option("--fnamepre", dest="fnamepre", default="", \
                  help="file name prefix for saving comparison plots")

(options, args) = parser.parse_args()

#----------------------------------------------------------

# Open a netcdf containing results for all ensembles
ds_model = xr.open_dataset('/home/ac.eva.sinha/ELM-Bioenergy/timeseries_plots/' + options.moddir + options.modfname)

# Open a netcdf containing observed data
ds_obs = xr.open_dataset('/home/ac.eva.sinha/ELM-Bioenergy/timeseries_plots/' + options.obsdir + options.obsfname)

# Read list of validation years for the site
valid_yrs = pd.read_csv('../info_obsdata/' + options.site + '_validation_years.csv', comment='#')
if(options.crop == 'miscanthus' or options.crop == 'switchgrass'):
    valid_yrs = valid_yrs['valid_yrs'].dropna().astype(int)
else:
    valid_yrs = valid_yrs[options.crop].dropna().astype(int)

# Remove validation years
ds_obs = ds_obs.sel(time=~ds_obs.time.dt.year.isin(valid_yrs))

# List of variable names that we want to keep
varnames = ['GPP', 'ER', 'EFLX_LH_TOT', 'FSH']

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

subplots_ts_model_obs(ds_model, ds_obs, varnames, title, site, ylabel, conv_fact_model, conv_fact_obs, fname=options.fnamepre)
