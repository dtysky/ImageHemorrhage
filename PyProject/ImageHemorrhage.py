__author__ = 'Dai Tianyu (dtysky)'

from PIL import Image
import os,re

def hemorrhage(im,border={'top':10,'bottom':10,'left':10,'right':10},opcity=0.5):
	opcity = int(opcity * 255)
	xsize,ysize = im.size
	im = im.convert('RGBA')
	res_xsize = xsize + border['left'] + border['right']
	res_ysize = ysize + border['top'] + border['bottom']
	hem_buffer = {}
	alpha = {'all':None,'tb':None,'lr':None}
	alpha['all'] = Image.new('L',(xsize,ysize),color=255)

	alpha['tb'] = Image.new('L',(xsize,1),color=opcity)
	hem_buffer['top'] = im.crop((0,0,xsize,1))
	hem_buffer['bottom'] = im.crop((0,ysize - 1,xsize,ysize))
	im_tmp = Image.new('RGBA',(xsize,res_ysize))
	im_tmp.paste(im,(0,border['top']),mask=alpha['all'])
	for i in range(border['top']):
		box = (0,i,xsize,i + 1)
		im_tmp.paste(hem_buffer['top'],box,mask=alpha['tb'])
	for i in range(border['bottom']):
		box = (0,ysize + i,xsize,ysize + i + 1)
		im_tmp.paste(hem_buffer['bottom'],box,mask=alpha['tb'])

	alpha['lr'] = Image.new('L',(1,res_ysize),color=opcity)
	hem_buffer['left'] = im_tmp.crop((0,0,1,res_ysize))
	hem_buffer['right'] = im_tmp.crop((xsize - 1,0,xsize,res_ysize))
	im_res = Image.new('RGBA',(res_xsize,res_ysize))
	im_res.paste(im_tmp,(border['left'],0))
	for i in range(border['left']):
		box = (i,0,i + 1,res_ysize)
		im_res.paste(hem_buffer['left'],box,mask=alpha['lr'])
	for i in range(border['right']):
		box = (xsize + i,0,xsize + i + 1,res_ysize)
		im_res.paste(hem_buffer['right'],box,mask=alpha['lr'])

	return im_res