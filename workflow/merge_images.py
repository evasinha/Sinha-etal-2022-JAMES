"""
Python modules for making spatial plots of ELM outputs
"""
import os
import sys 
from PIL import Image
import matplotlib as mpl 
mpl.use('Agg')

__author__ = 'Eva Sinha'
__email__  = 'eva.sinha@pnnl.gov'


# -----------------------------------------------------------
def merge_2images_horiz(im1, im2):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1])
    im = Image.new('RGBA', (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))

    return im

# -----------------------------------------------------------
def merge_2images_vert(im1, im2):
    w = im1.size[0]
    h = im1.size[1] + im2.size[1]
    im = Image.new('RGBA', (w, h))

    im.paste(im1)
    im.paste(im2, ((im1.size[0] -  im2.size[0]), im1.size[1]))

    return im

# -----------------------------------------------------------
def merge_4images_vert(im1, im2, im3, im4):
    w = im1.size[0]
    h = im1.size[1] + im2.size[1] + im3.size[1] + im4.size[1]
    im = Image.new('RGBA', (w, h))

    im.paste(im1)
    im.paste(im2, (0, im1.size[1]))
    im.paste(im3, (0, im1.size[1] + im2.size[1]))
    im.paste(im4, (0, im1.size[1] + im2.size[1] + im3.size[1]))

    return im

# -----------------------------------------------------------
def merge_3images(im1, im2, im3):
    w = im1.size[0] + im2.size[0]
    h = max(im1.size[1], im2.size[1]) + im3.size[1] 
    im = Image.new('RGBA', (w, h))

    im.paste(im1)
    im.paste(im2, (im1.size[0], 0))
    im.paste(im3, (im1.size[0], max(im1.size[1], im2.size[1])))

    return im

# -----------------------------------------------------------

myDict_merge_2images_horiz = {'fig_model_obs.png':    {'im1':'20220111_miscanthus_US-UiB_model_obs.png',
                                                       'im2':'20220111_switchgrass_US-UiA_model_obs.png'},
                              'fig_surrogate_RMSE.png':  {'im1':'Miscanthus_rmse.png',
                                                          'im2':'Switchgrass_rmse.png'},
                              'fig_surrogate_RRMSE.png': {'im1':'Miscanthus_rrmse.png',
                                                          'im2':'Switchgrass_rrmse.png'},
                              'fig_SA.png':           {'im1':'US-UiB_Miscanthus_sens_main_all.png',
                                                       'im2':'US-UiA_Switchgrass_sens_main_all.png'},
                              'fig_calibration.png':  {'im1':'US-UiB_Miscanthus_fit_shade.png',
                                                       'im2':'US-UiA_Switchgrass_fit_shade.png'},
                              'fig_validation.png':   {'im1':'20220120_miscanthus_US-UiB_valid_model_obs.png',
                                                       'im2':'20220120_switchgrass_US-UiA_valid_model_obs.png'},
                              'fig_LAI.png':          {'im1':'20220120_miscanthus_US-UiB_valid_lai.png',
                                                       'im2':'20220120_switchgrass_US-UiA_valid_lai.png'},
                              'fig_harvest.png':      {'im1':'20220120_miscanthus_US-UiB_valid_harv.png',
                                                       'im2':'20220120_switchgrass_US-UiA_valid_harv.png'}}

myDict_merge_4images_vert = {'fig_ELM_surrogate_miscanthus.png': {'im1':'fit_US-UiB_Miscanthus_GPP.png',
                                                                  'im2':'fit_US-UiB_Miscanthus_ER.png',
                                                                  'im3':'fit_US-UiB_Miscanthus_LE.png',
                                                                  'im4':'fit_US-UiB_Miscanthus_H.png'},
                             'fig_ELM_surrogate_switchgrass.png': {'im1':'fit_US-UiA_Switchgrass_GPP.png',
                                                                   'im2':'fit_US-UiA_Switchgrass_ER.png',
                                                                   'im3':'fit_US-UiA_Switchgrass_LE.png',
                                                                   'im4':'fit_US-UiA_Switchgrass_H.png'}}

fpath = '../figures/'

#iterate through dictionary
for i, key in enumerate(myDict_merge_2images_horiz):

   # Read images
   im1 = Image.open(fpath + myDict_merge_2images_horiz[key]['im1'])
   im2 = Image.open(fpath + myDict_merge_2images_horiz[key]['im2'])

   new_image = merge_2images_horiz(im1, im2)
   new_image.save('../figures/'+key,'png')

#iterate through dictionary
for i, key in enumerate(myDict_merge_4images_vert):

   # Read images
   im1 = Image.open(fpath + myDict_merge_4images_vert[key]['im1'])
   im2 = Image.open(fpath + myDict_merge_4images_vert[key]['im2'])
   im3 = Image.open(fpath + myDict_merge_4images_vert[key]['im3'])
   im4 = Image.open(fpath + myDict_merge_4images_vert[key]['im4'])

   new_image = merge_4images_vert(im1, im2, im3, im4)
   new_image.save('../figures/'+key,'png')
