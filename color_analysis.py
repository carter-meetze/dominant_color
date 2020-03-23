from PIL import Image
import urllib.request
from io import BytesIO
import statistics
from collections import Counter
import colorsys


def img2hex(path, **kwargs):

    if kwargs.get("hue"):
        hue_threshold = kwargs.get("hue")
    else:
        hue_threshold = .25

    try:
        img = Image.open(path)
    except:
        print('cannot parse image')

    colors = img.getcolors(maxcolors=10000000)
    top_colors = sorted(colors, key=lambda x: x[0], reverse=True)[:500]
    values = [x[1] for x in top_colors if statistics.mean(Counter(x[1]).values()) == 1]

    p = 0
    best_colors = []
    while p < len(values):
        hue = colorsys.rgb_to_hsv(values[p][0], values[p][1], values[p][2])[1]

        if hue < hue_threshold:
            p += 1
        else:

            best_colors.append(values[p])
            p += 1

    if best_colors:
        dominant_color = best_colors[0]
    else:
        dominant_color = colors[0][1]

    hex_code = '#%02x%02x%02x' % dominant_color

    return hex_code


def img2rgb(path, **kwargs):

    if kwargs.get("hue"):
        hue_threshold = kwargs.get("hue")
    else:
        hue_threshold = .25

    try:
        img = Image.open(path)
    except:
        print('cannot parse image')

    colors = img.getcolors(maxcolors=10000000)
    top_colors = sorted(colors, key=lambda x: x[0], reverse=True)[:500]
    values = [x[1] for x in top_colors if statistics.mean(Counter(x[1]).values()) == 1]

    p = 0
    best_colors = []
    while p < len(values):
        hue = colorsys.rgb_to_hsv(values[p][0], values[p][1], values[p][2])[1]

        if hue < hue_threshold:
            p += 1
        else:

            best_colors.append(values[p])
            p += 1

    if best_colors:
        dominant_color = best_colors[0]
    else:
        dominant_color = colors[0][1]

    return dominant_color


def img_url2hex(url, **kwargs):

    if kwargs.get("hue"):
        hue_threshold = kwargs.get("hue")
    else:
        hue_threshold = .25

    def get_img():
        file = BytesIO(urllib.request.urlopen(url).read())
        image = Image.open(file)

        return image
    
    try:
        img = get_img()
    except:
        print('cannot parse image')
        
    colors = img.getcolors(maxcolors=10000000)
    top_colors = sorted(colors, key=lambda x: x[0], reverse=True)[:500]
    values = [x[1] for x in top_colors if statistics.mean(Counter(x[1]).values()) == 1]

    p = 0
    best_colors = []
    while p < len(values):
        hue = colorsys.rgb_to_hsv(values[p][0], values[p][1], values[p][2])[1]

        if hue < hue_threshold:
            p += 1
        else:

            best_colors.append(values[p])
            p += 1

    if best_colors:
        dominant_color = best_colors[0]
    else:
        dominant_color = colors[0][1]

    hex_code = '#%02x%02x%02x' % dominant_color

    return hex_code


def img_url2rgb(url, **kwargs):

    if kwargs.get("hue"):
        hue_threshold = kwargs.get("hue")
    else:
        hue_threshold = .25

    def get_img():
        file = BytesIO(urllib.request.urlopen(url).read())
        image = Image.open(file)

        return image
    
    try:
        img = get_img()
    except:
        print('cannot parse image')

    colors = img.getcolors(maxcolors=10000000)
    top_colors = sorted(colors, key=lambda x: x[0], reverse=True)
    values = [x[1] for x in top_colors if statistics.mean(Counter(x[1]).values()) == 1]
    p = 0
    best_colors = []
    while p < len(values):
        hue = colorsys.rgb_to_hsv(values[p][0], values[p][1], values[p][2])[1]

        if hue < hue_threshold:
            p += 1
        else:
            best_colors.append(values[p])
            p += 1

    if best_colors:
        dominant_color = best_colors[0]
    else:
        dominant_color = colors[0][1]

    return dominant_color

