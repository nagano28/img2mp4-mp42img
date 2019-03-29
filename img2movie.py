# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:04:22 2018

@author: Nagano Masatoshi
"""

import numpy as np
import matplotlib.pyplot as plt
import os
#import ffmpeg as fp

def classes_plot(savepath_png):
        table = np.loadtxt("./estimated_classes.txt")
        table_true = np.loadtxt("./true_classes.txt")
        
        x = np.arange(int(len(table)))
        for j in range(len(table)):
            save_impath = ("./%s/%d.png"%(savepath_png,j))
            #plt.xlim(-1.5, 1.0)
            plt.ylim(0, 8,1)
            plt.plot(x,table,label = "Estimated")
            plt.plot(x,table_true,label = "True")
    
            plt.plot(x[j],table[j],'o')
            
            plt.legend()
            plt.savefig(save_impath)
            plt.close()
            
def make_mp4(savepath_png, savepath_mp4):
    #st = fp.input("./image/%d.png")
    #st = fp.output(st, "./movie/output.mp4")
    #fp.run(st)
    
    #-r framerate -i input -r framerate output
    cmd = ("ffmpeg -r 5 -i ./image/%d.png -vcodec libx264 -pix_fmt yuv420p -r 5 ./movie/output.mp4")
    os.system(cmd)

def make_folder(path_img, path_movie):
    if not os.path.isdir(path_img):
        os.makedirs(path_img)
        
    if not os.path.isdir(path_movie):
        os.makedirs(path_movie)

def make_mp4_h264():
    cmd = ("ffmpeg -i ./movie/output.mp4 ./movie/output_h264.mp4 -vcodec libx264 -acodec libmp3lame")
    os.system(cmd)

def main():
    savepath_png = 'image'
    savepath_mp4 = 'movie'
    make_folder(savepath_png, savepath_mp4)
    classes_plot(savepath_png)
    make_mp4(savepath_png, savepath_mp4)
    make_mp4_h264()
    
if __name__ == '__main__':
    main()    