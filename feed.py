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

#Retrieves thumbnail url from entry via get_image, blits image to screen
def render_thumb(entry, coords, get_biggest=1):

    #obj = entry['media_thumbnail']
    thumb = entry[get_biggest]['url']

    img = get_image(thumb)
    screen.blit(img, coords)

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

#Calls split_text on a string then render and blits
def render_text(text, rect, font):

    lines = split_text(text, rect, font)
    y = 0
    spacing = 3
    font_height = font.size("Tg")[1]

    #blit to screen one line at a time
    for line in lines:
        line = font.render(line, 1, colour)
        screen.blit(line, (rect[0], rect[1]+y))
        y += font_height + spacing

pygame.init()
pygame.display.set_caption('Feed Me')

WIDTH=640
HEIGHT=480
TEXT_LEFT = 150
MARGIN = 5

title_font = pygame.font.SysFont("arial", 30)
sum_font = pygame.font.SysFont("arial", 16)

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

colour = (10,10,10)
bg_colour = (255,255,255)
screen.fill(bg_colour)

url = "http://feeds.bbci.co.uk/news/rss.xml"

data = feedparser.parse(url)

#useful ones:
#media_thumbnail, title, link, published, summary

title = data.entries[0]['title']
summary = data.entries[0]['summary']
thumb = data.entries[0]['media_thumbnail']

#Update to screen
render_thumb(thumb, (0,0))
render_text(title, (TEXT_LEFT,0, WIDTH - TEXT_LEFT, HEIGHT), title_font)
render_text(summary, (150,40, 500,50), sum_font)
pygame.display.flip()
