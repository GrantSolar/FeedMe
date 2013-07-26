import feedparser
import pygame
import urllib

from PIL import Image
from io import BytesIO


#Returns the image at url as a pygame surface
def get_image(url):
    
    #Open image from url
    img_file = urllib.request.urlopen(url)
    img = BytesIO(img_file.read())
    img = Image.open(img)

    mode = img.mode
    size = img.size
    data = img.tostring()

    assert mode in "RGB", "RGBA"

    #Convert image url to pygame surface
    surface = pygame.image.fromstring(data, size, mode)
    return surface

#def get_thumb(
pygame.init()
pygame.display.set_caption('Feed Me')

w=640
h=480
size=(w,h)
screen = pygame.display.set_mode(size)

bg_colour = (255,255,255)
screen.fill(bg_colour)

url = "http://feeds.bbci.co.uk/news/rss.xml"

data = feedparser.parse(url)

#useful ones:
#media_thumbnail, title, link, published, summary
"""font = pygame.font.SysFont("comicsansms", 36)
#text = font.render(data.entries[0].title, 1, (10, 10, 10))
screen = screen.convert()
screen.fill((250,250,250))
text = font.render("Hello", 1, (10,10,10))
textpos = text.get_rect()

screen.blit(text, textpos)"""

#for datum in data:
#    print(datum)
#x = urllib.request.urlopen('http://www.google.com/images/srpr/logo4w.png')
#file = StringIO(x).read()


#img = get_image('http://i.imgur.com/CcjcXzj.jpg')
#screen.blit(img, (0,0))
font = pygame.font.SysFont("comicsansms", 36)
text = font.render(data.entries[0]['title'], 1, (10,10,10))
textpos = text.get_rect() #text height and width

thumb = data.entries[0]['media_thumbnail']
img = get_image(thumb[1]['url']) #1 gives bigger image. Could also use 0

screen.blit(img,textpos)

screen.blit(text, textpos)
pygame.display.flip()
