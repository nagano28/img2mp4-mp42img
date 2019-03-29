# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 15:04:22 2018

@author: Nagano Masatoshi
"""

import cv2
import os
#import ffmpeg as fp


def main():
    #動画を読み込む
    filename = './movie/output.mp4'
    video = cv2.VideoCapture(filename)
    
    path = 'movie2'
    if not os.path.exists(path):
        os.mkdir(path)
        
    savepath = 'image2'
    if not os.path.exists(savepath):
        os.mkdir(savepath)
    
    #フレーム数確認
    frames = int(video.get(7))
    print ('frame rate:',frames)
    
    for i in range(0,frames):
        _, frame = video.read()
        cv2.imwrite(savepath+"/%d.png"%i,frame)
    
if __name__ == '__main__':
    main()    