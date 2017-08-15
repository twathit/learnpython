# -*- coding: utf-8 -*-
__author__ = 'Edward'
import os;
def rename(path):
    filelist=os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join(path,files);#原来的文件路径

        if os.path.isfile(Olddir):
            #filename=os.path.split(files)[0];#文件名
            #filetype=os.path.splitext(files)[1];#文件扩展名
            Newdir=os.path.join(path,files+'.mp4');#新的文件路径
            os.rename(Olddir,Newdir);#重命名
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            rename(Olddir)

rename(r'D:\BaiduYunDownload\170424')