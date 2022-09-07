#!/bin/bash

# ----- Directory paths -----
export RUN_DIR_PATH=/lcrc/group/acme/ac.eva.sinha

export YR_START=2005
export YR_END=2014

for SITE in 'US-UiB' 'US-UiA'
do
   if [ $SITE == 'US-UiB' ]
   then
      export CROP='miscanthus'
   else
      export CROP='switchgrass'
   fi

   export CASE_PRE=20220120_${CROP}
   export CASEID=${CASE_PRE}_${SITE}_ICBELMCNCROP_trans
   export RUN_DIR=${RUN_DIR_PATH}/${CASEID}/run

   export OBSDIR=${SITE}_${CROP}/
   export OBSFNAME=${SITE}_${CROP}_select_var.nc
   export FNAMEPRE=${CASE_PRE}_${SITE}

   #------ Run plotmodobs -----
   python plot_valid_mod_obs.py --site ${SITE} --crop ${CROP^} --rundir ${RUN_DIR} --caseid ${CASEID} --yr_start ${YR_START} --yr_end ${YR_END} --obsdir ${OBSDIR} --obsfname ${OBSFNAME}  --fnamepre ${FNAMEPRE}

done
