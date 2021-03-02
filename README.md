The Cumbria Singers website!
Repository now on GitHub for Cumbria Singers

With enormous gratitude to https://cameratamusica.com/ (Also http://colinbrislawn.github.io/CamerataMusica/)

This is built with [Pelican](http://docs.getpelican.com/) 

Currently it is _not_ deployed with Travis-CI 

---

Here's how to set up the build environment:
```
conda create --name pelican python=3.7 pelican ghp-import markdown
conda activate pelican
```

Here's how to test the site locally (Linux):
```
pelican -lr & sleep 2; open http://127.0.0.1:8000/
```
Then view your preview here: http://127.0.0.1:8000/

---

Here's how to make those big, beautiful background images:
- find high-def images that are wide, with artists in the center (because narrow screens crop the sides) 
- export low quality at `1950px` wide, with the name `name-large.jpg`
- crop to 4:3
- export high quality at `400px` wide, with the name `name400.jpg`
- add to page with this markdown (`Bannerposition` is `top` by default)
```
Status: hidden
Banner: ./images/choir-large.jpg
Bannerposition: center
```
