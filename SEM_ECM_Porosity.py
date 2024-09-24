# -*- coding: utf-8 -*-
"""
@author: Alberto Martín-Asensio
"""

import os

import numpy as np

import matplotlib.pyplot as plt

from skimage import  io, filters
from matplotlib.font_manager import FontProperties

from matplotlib_scalebar.scalebar import ScaleBar

font = FontProperties()
font.set_family('serif')
font.set_name('Times New Roman')

os.chdir(r"XXXXXXXXXX") #Write the working directory

def porosity(image):
    
    #Read the image
    original = io.imread(image)
    
    #Show the image
    
    plt.imshow(original,cmap = "Greys")
    plt.show()
    plt.close()
    
    #filters.thresholding.try_all_threshold(original) #Use this code if you want to check wchich algorithm is best for your image.
    
    #Create mask
    img = original>filters.threshold_triangle(original)
    #Show mask
    plt.imshow(img,cmap = "Greys_r")
    plt.show()
    plt.close()
   
    #Initialize black pixels count
    n_b = 0
    #Initialize white pixels count
    n_w = 0
    #Count píxels
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] !=0:
                n_w +=1
            else:
                n_b+=1
    
    #Calculate the porosity
    p = n_b/(n_w+n_b)
    
    #Print the measured porosity
    print(f"Porosity = {p*100:0.2f} %")
    
    #Create subplots with the original image and the mask with scale bar
    
    value=3#Length of the scale bar
    
    fig, (ax1,ax2) = plt.subplots(1,2)
    
    ax1.imshow(original, cmap = "Greys")
    ax1.axis("Off")
    ax1.set_title("SEM image",fontproperties=font,fontsize = 18)
    scalebar = ScaleBar(11.16, "nm", length_fraction=0.4,location = "lower right",box_alpha = 0,width_fraction = 0.03,fixed_value = value,fixed_units = "um")
    ax1.add_artist(scalebar)
    ax2.imshow(img)
    ax2.axis("Off")
    ax2.set_title("Binarized image",fontproperties=font,fontsize = 18)
    scalebar = ScaleBar(11.16, "nm", length_fraction=0.4,location = "lower right",box_alpha = 0,width_fraction = 0.03,fixed_value = value,fixed_units = "um")
    ax2.add_artist(scalebar)
    
    savedir = r"XXXXXX" #Write the directory to save the images
    
    plt.savefig(savedir+image.strip(".tif")+"plot.jpg",bbox_inches = "tight")
    plt.show()
    plt.close()
    fig,ax = plt.subplots()
    plt.imshow(original, cmap = "Greys")
    scalebar = ScaleBar(11.16, "nm", length_fraction=0.4,location = "lower right",box_alpha = 0,width_fraction = 0.03,fixed_value = value,fixed_units = "um",label_formatter = lambda x, y:'')
    ax.add_artist(scalebar)
    plt.axis("Off")
    plt.savefig(savedir+image.strip(".tif")+"_original.jpg",bbox_inches = "tight")
    
    
    return p

def main():
    
    p = []
    for image in os.listdir("."):
        directory = image
        p.append(porosity(directory))
    
    p = np.array(p)*100
    
    #Calculate and print the average porosity
    print(f"Average porosity: p = {np.mean(p):0.2f} +- {np.std(p):0.2f}")

    return




main()
