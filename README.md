_your zenodo badge here_

# Sinha-etal\_2022_JAMES

**Modeling perennial bioenergy crops in the E3SM land model (ELMv2)**

Eva Sinha<sup>1\*</sup>, Katherine V. Calvin<sup>2</sup>, Ben Bond-Lamberty<sup>2</sup>, Beth A. Drewniak<sup>3</sup>, Daniel M. Ricciuto<sup>4</sup>, Khachik Sargsyan<sup>5</sup>, Yanyan Cheng<sup>1,6</sup>, Carl Bernacchi<sup>7,8</sup>, and Caitlin E. Moore<sup>8,9</sup>

<sup>1</sup>Pacific Northwest National Laboratory, Richland, WA, United States  
<sup>2</sup>Joint Global Change Research Institute, Pacific Northwest National Laboratory, College Park, MD, United States  
<sup>3</sup>Argonne National Laboratory, Lemont, IL, United StateA  
<sup>4</sup>Oak Ridge National Laboratory, Oak Ridge, TN, United States  
<sup>5</sup>Sandia National Laboratories, Livermore, CA, United States  
<sup>6</sup>Department of Industrial Systems Engineering and Management, National University of Singapore, Singapore  
<sup>7</sup>Global Change and Photosynthesis Research Unit, USDA-ARS, Urbana, IL, United States  
<sup>8</sup>University of Illinois at Urbana‐Champaign, Urbana, IL, United States  
<sup>9</sup>School of Agriculture and Environment, The University of Western Australia, Crawley, WA, Australia

\* corresponding author:  eva.sinha@pnnl.gov

## Abstract
Perennial bioenergy crops are increasingly important for the production of ethanol and other renewable fuels, and as part of an agricultural system that alters the climate through its impact on biogeophysical and biogeochemical properties of the terrestrial ecosystem. Few earth system models (ESMs) represent such crops, however. 
In this study, we expand the Energy Exascale Earth System Model (E3SM) Land Model (ELMv2) to include perennial bioenergy crops with a high potential for mitigating climate change. 
We focus on high-productivity miscanthus and switchgrass, estimating various parameters associated with their different growth stages and performing a global sensitivity analysis to identify and optimize these parameters. 
The sensitivity analysis identifies five parameters associated with phenology, carbon/nitrogen allocation, stomatal conductance, and maintenance respiration as the most sensitive parameters for carbon and energy fluxes.
We calibrated and validated the model against observations and found that the model closely captures the observed seasonality and the magnitude of carbon fluxes. 
The validated model represents the latent heat flux fairly well, but sensible heat flux for miscanthus is not well captured.
Finally, we validated the model against observed leaf area index (LAI) and harvest amount and found modeled LAI to be comparable to observations, although the model underestimates harvest amount.
This work provides a foundation for future ESM analyses of the interactions between perennial bioenergy crops and carbon, water, and energy dynamics in the larger earth system, and sets the stage for studying the impact of future biofuel expansion on climate and terrestrial systems.

## Journal reference
Sinha, E., Calvin, K.V., Bond-Lamberty B., Drewniak, B., Ricciuto, D., Sargsyan, K., Cheng, Y., Bernacchi, C., Moore, C., 2022. Modeling perennial bioenergy crops in the E3SM land model (ELMv2). (In review) Journal_JAMES, DOI: XXXX

## Code reference
Sinha, E., Calvin, K.V., Bond-Lamberty B., Drewniak, B., Ricciuto, D., Sargsyan, K., Cheng, Y., Bernacchi, C., Moore, C., 2022. Modeling perennial bioenergy crops in the E3SM land model (ELMv2). Supporting code for Sinha et al. 2022 - TBD [Code]. Zenodo. http://doi.org/some-doi-number/zenodo.7777777

## Data reference

### Input data
Reference for each minted data source for your input data.  For example:

Human, I.M. (2021). My input dataset name [Data set]. DataHub. https://doi.org/some-doi-number

### Output data
Sinha, E., Calvin, K.V., Bond-Lamberty B., Drewniak, B., Ricciuto, D., Sargsyan, K., Cheng, Y., Bernacchi, C., Moore, C., 2022. Modeling perennial bioenergy crops in the E3SM land model (ELMv2). Supporting data for Sinha et al. 2022 - TBD [Code]. Zenodo. http://doi.org/some-doi-number/zenodo.7777777

## Contributing modeling software
| Model | Version | Repository Link | DOI |
|-------|---------|-----------------|-----|
| E3SM | version | https://github.com/E3SM-Project/E3SM | link to DOI dataset |

## Reproduce my experiment
1. Clone and install [E3SM](https://github.com/E3SM-Project/E3SM).

## Reproduce my figures
Use the scripts found in the `workflow` directory to reproduce the figures used in this publication.

| Script Name | Description | How to Run |
| --- | --- | --- |
| `generate_figures.py` | Script to generate my figures | `python3 generate_figures.py -i /path/to/inputs -o /path/to/outuptdir` |
