from PIL import Image
from PIL import EpsImagePlugin
from PIL import ImageOps
import random
EpsImagePlugin.gs_windows_binary = "Ghostscript/bin/gswin64c.exe" 

def randrgb():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

#input:




#process image, turn grayscale and invert
alpha = Image.open("resources/jerem.eps")
alpha.load(scale=16)
alpha = alpha.convert("L")
alpha = ImageOps.invert(alpha)

#create face rgba
fore = Image.new("RGB", alpha.size, (227, 211, 129))
fore.putalpha(alpha)

#create background rgba
back = Image.new("RGBA", alpha.size, (166, 68, 61))

#composite foreground and background
pfp = Image.alpha_composite(back,fore)

#save and display image
pfp.show()
pfp.save("output/jeremtest.png")
