---
layout: blog
category: Blog
title: How to use icons from `font-awesome` as markers in `matplotlib`
---
# How to use icons from `font-awesome` as markers in `matplotlib`
Font Awesome contains a lot of neat icons. Here is a way to use them as `markers` (really just annotated text) in matplotlib.

```
import random
from matplotlib import font_manager

# A path containing `font-awesome/FontAwesome.otf` should be in that list
# If not, consider installing using
# `apt-get install fonts-font-awesome` in terminal
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath
from fontTools.ttLib import TTFont


def get_fp():
    fapath = font_manager.findfont("FontAwesome")
    fp = FontProperties(fname=fapath)
    return fp, fapath
    
def make_fa_cmap_dict(verbose:bool = False):
    fp, fapath = get_fp()
    font = TTFont(fapath)
    cmap = font["cmap"].getcmap(3, 1).cmap

    # Create a list of characters available in the font
    cmap_dict = {name:chr(codepoint) for name, codepoint in zip(cmap.values(), cmap.keys())}
    if verbose: 
        for key in cmap_dict.keys():
            print(key)
    return cmap_dict, fp

def pick_random_fa_icon():
    cmap_dict, fp = make_fa_cmap_dict()

    # Randomly select a character from the available characters
    while True:
        rand_char = random.choice(list(cmap_dict.values()))
        # Check if the character can be rendered
        try:
            path = TextPath((0, 0), rand_char, prop=fp)
            break
        except ValueError:
            continue
    return rand_char, fp

def pick_named_fa_icon(name):
    cmap_dict, fp = make_fa_cmap_dict()
    return cmap_dict[name], fp

# cmap_dict = make_fa_cmap_dict(verbose=True)

num_points = 100

x = np.random.rand(num_points)
y = np.random.rand(num_points)

plt.figure(figsize=(8, 6))
for i in zip(range(num_points)):
    marker, fp = pick_random_fa_icon()
    plt.text(x[i], y[i], marker, fontproperties=fp, color="xkcd:purplish grey")

named_marker, fp = pick_named_fa_icon('cog')
plt.text(0.5, 0.5, named_marker, fontproperties=fp, color="xkcd:green teal")
plt.show()

```
<img src="/images/fontawesomescript/example.jpg">
