from PIL import Image
import numpy as np

pix = np.zeros((1080,1920, 3), dtype=np.uint8)

pix[:100,0:200] = [255,0,0]
pix[100:200,200:400] = [0,255,0]
pix[200:300,400:600] = [0,0,255]


img = Image.fromarray(pix, "RGB")
img.save("photo.png")

