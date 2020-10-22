from PIL import Image
from PIL import EpsImagePlugin
from PIL import ImageOps
import random
EpsImagePlugin.gs_windows_binary = "Ghostscript/bin/gswin64c.exe" 

def randrgb():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#process image, turn grayscale and invert
im = Image.open("resources/jerem.eps")
im.load(scale=2)
im = im.convert("L")
im = ImageOps.invert(im)

#create face rgba
fore = Image.new("RGB", im.size, (0,0,0))
fore.putalpha(im)

#create background rgba
back = Image.new("RGBA", im.size, (255,0,0))

#composite foreground and background
pfp = Image.alpha_composite(back,fore)

#save and display image
pfp.show()
pfp.save("output/jeremtest.png")
