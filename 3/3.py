#assignment 3 code
from PIL import Image,ImageFilter
import requests
from StringIO import StringIO
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.cm
from skimage.color import rgb2gray


#3.1; import image from internet
imurl = requests.get("http://www.vancitymommyd.com/wp-content/uploads/2018/01/pokemon-clipart-pokemon-clip-art-clipart-wikiclipart-school-clipart.png")
name = 'pikachu'

#3.2; open image, print some properties
im = Image.open(StringIO(imurl.content))

c,d = im.size
print 'image width: '+str(c)+ '; image height: ' + str(d)
print 'image mode: '+str(im.mode)

#3.3; "effect we can achieve"
im_edges = im.filter(ImageFilter.FIND_EDGES)

#3.4; blur, convert to grayscale, and get brightnesses for crisper edges
im = im.filter(ImageFilter.GaussianBlur(radius=1.5))
im = im.convert('LA')
pxs = list(im.getdata())
px_val = [pxs[(n*c):((n+1)*c)] for n in range(d)]
brightness = [[sum(px) for px in row] for row in px_val]

#im_edges.show()
#im_edges.save(name+'_FIND_EDGES_demo.png','PNG')

#3.5; edge detect using gaussian gradient with different widths
for width in np.arange(0.1, 2,0.5):
     edge = ndimage.filters.gaussian_gradient_magnitude(brightness,width)
     #is using a builtin gaussian gradient ok?
     im_edge = Image.fromarray(edge.astype('uint8'))
     im_edge.save(name+'_width_'+str(width.round(decimals=1))+'.png','PNG')

#3.6
# Yes, we can probably use edge detection on captchas; as we can see from the watermarks in the "funny_sheep" images, edge detection will capture the shape of letters. If we have an extensive enough image bank of known letters, we could match shapes and figure out what the letters were. This is probably why most captchas have a lot of dots and stuff in the back; images with noise are harder to classify.

#3.7
#Edge detection seems really strong, although it probably needs to heavily process the image before doing the actual edge detection bit for best results in real life applications; in addition, it'd probably good to edge detect on several "types" of pixels, since differentiating using colors can double check the results from differentiating using brightness, or vice versa.
#I think this assignment could be longer/clearer. The question text didn't really explain very much for the hard parts, and it wasn't immediately obvious what resources could be used and what couldn't ('skim[ming] the wikipedia page' was allowed, but was reading the detailed implementations there ok?), and I was also unsure of what kind of built-in functions we could use (#4 says 'convolve your image with a blurring filter'; I used PIL's built in gaussian blur, was this ok? For the gaussian gradient magnitude, I also used a built in function.) 
#It was pretty cool to see the edges come out though. Fun assignment overall?
               

               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
