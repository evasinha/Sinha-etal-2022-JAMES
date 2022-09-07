#!/bin/bash

for SITE in 'US-UiB' 'US-UiA'
do
   if [ $SITE == 'US-UiB' ]
   then
      export CROP='Miscanthus'
   else
      export CROP='Switchgrass'
   fi
   export FNAMEPRE=${SITE}_${CROP}_
   python plot_dm_surr.py --site ${SITE} --crop ${CROP}
   python plot_surr_rel_l2_rmse_rrmse.py --site ${SITE} --crop ${CROP}
   python subplots_sens.py --site ${SITE} --crop ${CROP}
   python subplots_shade.py -site ${SITE} -crop ${CROP} -x ${FNAMEPRE}xdata_all.txt -y ${FNAMEPRE}ytrain.dat -z ${FNAMEPRE}post_pred.dat -c 0 -ylb -0.1
done
