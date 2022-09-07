#!/bin/bash

for SITE in 'US-UiB' 'US-UiA'
do
   if [ $SITE == 'US-UiB' ]
   then
      export CROP='miscanthus'
   else
      export CROP='switchgrass'
   fi

   # ------ Options for running plotmodobs -----
   export CASE_PRE=20220111_${CROP}
   export MODDIR=${CASE_PRE}_${SITE}/
   export MODFNAME=${CASE_PRE}_${SITE}_ICBELMCNCROP_trans_mean_across_years.nc
   export OBSDIR=${SITE}_${CROP}/
   export OBSFNAME=${SITE}_${CROP}_select_var.nc
   export FNAMEPRE=${CASE_PRE}_${SITE}

   #------ Run plotmodobs -----
   python plotmodobs.py  --site ${SITE} --crop ${CROP} --moddir ${MODDIR} --modfname ${MODFNAME} --obsdir ${OBSDIR} --obsfname ${OBSFNAME}  --fnamepre ${FNAMEPRE}

done
