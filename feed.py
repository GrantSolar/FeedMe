import feedparser
import pygame
import urllib

from PIL import Image
from io import BytesIO


#Returns the image at url as a pygame surface
def get_image(url):
    
    #Open image from url
    img_url = urllib.request.urlopen(url)
    img = BytesIO(img_url.read())
    img = Image.open(img)

    mode = img.mode
    size = img.size
    data = img.tostring()

    assert mode in "RGB", "RGBA"

    #Convert image url to pygame surface
    surface = pygame.image.fromstring(data, size, mode)
    return surface

#Retrieves thumbnail url from entry, returns surface via get_image
def get_thumb(entry, get_biggest=1):

    obj = entry['media_thumbnail']
    thumb = obj[get_biggest]['url']

    return get_image(thumb)

#Splits a string into maximum length substrings for wrapping
def split_text(text, rect, font):

    rect = pygame.Rect(rect)
    i = 1
    lines = []

    #Iterate the string. If it's over max width, split at most recent space. Repeat
    while text:
        
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        lines.append(text[:i])
        text = text[i:]

    return lines

#Calls split_text on a string then render as a surface
def render_text(text, rect, font):

    lines = split_text(text, rect, font)
    y=0
    spacing = 3
    font_height = font.size("Tg")[1]
    for line in lines:
        line = font.render(line, 1, colour)
        screen.blit(line, (rect[0], rect[1]+y))
        y += font_height + spacing

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


#for datum in data:
#    print(datum)

colour = (10,10,10)

font = pygame.font.SysFont("arial", 30)
title = font.render(data.entries[0]['title'], 1, colour)

font = pygame.font.SysFont("arial", 16)
summary = data.entries[0]['summary']
print(split_text(summary, (0,0, 100, 100), font))
#summary = font.render(summary, 1, colour)



title_pos = title.get_rect() #text height and width 298 29

img = get_thumb(data.entries[0])

#Update to screen. Move these to respective functions?
screen.blit(img, (0,0))
screen.blit(title, (150,0))
#screen.blit(summary, (150, 40))
render_text(summary, (150,40, 500,50), font)
pygame.display.flip()
