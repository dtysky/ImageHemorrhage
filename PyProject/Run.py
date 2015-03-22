__author__ = 'Dai Tianyu (dtysky)'

from PIL import Image
import os,re,json
import ImageHemorrhage as IH

FileAll = []

Setting = json.load(open('Setting.json','r'))
border = Setting['border']
opcity = Setting['opcity']

for root,dirs,files in os.walk('./ImageSrc'):
    for f in files:
        if re.findall(r'jpg|bmp|png',f):
        	FileAll.append((root+'/',f))

for root,f in FileAll:
	im_src = Image.open(root+f)
	IH.hemorrhage(im_src,border,opcity).save('./ImageRes/'+f)