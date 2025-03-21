from images import Image

def greyScale(image):
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r, g, b)=image.getPixel(x,y)
            r = int(r*0.299)
            g = int(g*0.587)
            b = int(b*0.114)
            lum = r+g+b
            image.setPixel(x, y, (lum, lum, lum))

def main():
    image=Image("cat.gif")
    image.draw()
    greyScale(image)
    image.draw()
    image.save("grey_cat")

if __name__ == "__main__":
    main()