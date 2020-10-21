from PIL import Image
#random jerem when?????
import random

#get input as string
bgi = input("Enter background rgb values seperated by commas: ")
fgi = input("Enter foreground rgb values seperated by commas: ")

#split string into list
rgbstrback = bgi.split(",")
rgbstrfore = fgi.split(",")

#declare lists to store actual int values
rgbback = []
rgbfore = []

#assign integers to lists
for i in rgbstrback:
    rgbback.append(int(i))
for i in rgbstrfore:
    rgbfore.append(int(i))


def jerempfp(rgbb, rgbf):
    foreground = Image.new("RGBA", (78,78), rgbf)
    alphaimage = Image.open("resources/jeremalpha.png")
    alpha = alphaimage.getchannel("A")
    foreground.putalpha(alpha)

    background = Image.new("RGBA", (78,78), rgbb)

    pfp = Image.alpha_composite(background,foreground)
    pfp.save("output/jerem.png")

jerempfp(tuple(rgbback), tuple(rgbfore))
