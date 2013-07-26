import feedparser
import pygame
import urllib

from PIL import Image
from io import BytesIO

pygame.init()
pygame.display.set_caption('Feed Me')

w=640
h=480
size=(w,h)
screen = pygame.display.set_mode(size)


def get_image(url):
    
    #Image displaying
    img_file = urllib.request.urlopen(url)
    img = BytesIO(img_file.read())
    image = Image.open(img)

    mode = image.mode
    size = image.size
    data = image.tostring()

    assert mode in "RGB", "RGBA"

    #Convert image url to pygame surface
    surface = pygame.image.fromstring(data, size, mode)
    return surface



#url = "http://feeds.bbci.co.uk/news/rss.xml"

#data = feedparser.parse(url)


#for datum in data:
#    print(datum)
#x = urllib.request.urlopen('http://www.google.com/images/srpr/logo4w.png')
#file = StringIO(x).read()


img = get_image('http://i.imgur.com/CcjcXzj.jpg')
screen.blit(img, (0,0))
pygame.display.flip()
