from PIL import Image,ImageFilter
import requests
from StringIO import StringIO
import numpy as np

imurl = requests.get("https://cdn.modernfarmer.com/wp-content/uploads/2017/12/Funny-Sheep-Facts.jpg")

im = Image.open(StringIO(imurl.content))

c,d = im.size
print 'image width: '+str(c)+ '; image height: ' + str(d)
print 'image mode: '+str(im.mode)
im.show()
im_edges = im.filter(ImageFilter.FIND_EDGES)
im_edges.show()

im_blur2 = im.filter(ImageFilter.GaussianBlur(radius=4))
im_blur2.show()
a = np.array(im_blur2)
h = a.shape[0]
w = a.shape[1]
dx = a[2:,1:w-1] - a[2:,0:w-2]
dy = a[1:h-1,2:] - a[0:h-2,2:]

#dx = np.diff(im_blur2, axis=0)
#dy = np.diff(im_blur2, axis=1)


im_dx = Image.fromarray(dx,'RGB')
im_dx.show()
im_dy = Image.fromarray(dy,'RGB')
im_dy.show()

d = np.sqrt(np.square(dx)+np.square(dy))
theta = np.arctan2(dy[:,:,0],dx[:,:,0])
theta = (np.round(theta * (5.0 / np.pi)) + 5) % 5
theta = (theta %4)
d1 = d.copy()


#print theta
im_d1 = Image.fromarray(d1,'RGB')
im_d1.show()
               

for r in range(h-3):
     for c in range(w-3):
          th = (theta[r,c])
         # print 'th'+str(th)
          if th==0:
               if np.any(d[r,c,:]<=d[r,c-1,:]) or np.any(d[r,c,:]<=d[r,c+1,:]):
                    d1[r,c,:]=0
          if th==1:
               if np.any(d[r,c,:]<=d[r-1,c+1,:]) or np.any(d[r,c,:]<=d[r+1,c-1,:]):
                    d1[r,c,:]=0
          if th==2:
               if np.any(d[r,c,:]<=d[r-1,c,:]) or np.any(d[r,c,:]<=d[r+1,c,:]):
                    d1[r,c,:]=0
          if th==3:
               if np.any(d[r,c,:]<=d[r-1,c-1,:]) or np.any(d[r,c,:]<=d[r+1,c+1,:]):
                    d1[r,c,:]=0

im_d1 = Image.fromarray(d1,'RGB')
im_d1.show()
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
