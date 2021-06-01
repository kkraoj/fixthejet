# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 10:47:23 2018
@author: kkrao

Works in Python 3. only. 
Credits: Carreau
Code forked from https://github.com/Carreau/miscs/blob/master/Viridisify.ipynb
"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as colors
from matplotlib import cm
from scipy.spatial import cKDTree
# from ipywidgets import interact
import matplotlib.image as mpimg
from matplotlib.ticker import NullLocator
from PIL import Image
from argparse import ArgumentParser


def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--input',
            dest='input', help='content image',
            metavar='INPUT', required=True)
    parser.add_argument('--output',
            dest='output', help='output path',
            metavar='OUTPUT', required=True)
    parser.add_argument('--colormap', type=str,
            dest='cout', help='cout (default %(default)s)',
            metavar='COUT', default='viridis')
    return parser


def read_image(file_name):
    if file_name.rpartition('.')[-1]=='jpg':
        divide_by = 255.
    elif file_name.rpartition('.')[-1]=='jpeg':
        divide_by = 255.
    elif file_name.rpartition('.')[-1]=='png':
        divide_by = 1.
    else:
        raise IOError('%s file format not supported. Try .jpg/.png'%file_name.rpartition('.')[-1])
    img = mpimg.imread(file_name, format = file_name[-3:])[:,:,:3]/divide_by
    return img


#@interact(sub=(0, 500), d=(0,1,0.05))
def convert_image(img, cout, d=0.2,sub=256, cin='jet'):
    
    viridis = plt.get_cmap(cout)
    jet = plt.get_cmap(cin)
    jet256 = jet(range(sub))[:, :3]
    # jet256 = colors.makeMappingArray(sub, jet)[:, :3] #deprecated 3.2.1 onwards
    K = cKDTree(jet256)
    oshape = img.shape
    img_data = img.reshape((-1,3))
    res = K.query(img_data, distance_upper_bound=d)
    indices = res[1]
    l = len(jet256)
    indices = indices.reshape(oshape[:2])
    remapped = indices
    indices.max()
    mask = (indices == l)
    remapped = remapped / (l-1)
    mask = np.stack( [mask]*3, axis=-1)
    blend = np.where(mask, img, viridis(remapped)[:,:,:3])
    
    return img, blend

    
def save_image(blend, path):
    mpimg.imsave(path, blend)


def main():
    parser = build_parser()
    options = parser.parse_args()
    try:
        img = read_image(options.input)
    except:
        raise IOError('%s does not exist'%options.input)
    img, blend = convert_image(img = img, cout = options.cout,cin = 'jet')
    try:
        save_image(blend, options.output)
    except:
        raise IOError('%s is not writable or does not have a valid file \
                      extension for an image file'%options.output)


if __name__ == '__main__':
    main()
    