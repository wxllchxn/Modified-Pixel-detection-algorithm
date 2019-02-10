#!/usr/bin/env python
# coding: utf-8

# In[50]:


# this is ye old image thingy
from PIL import Image
import requests
from io import BytesIO

response = requests.get('https://images.pexels.com/photos/248797/pexels-photo-248797.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
img = Image.open(BytesIO(response.content))

# show image

def compare(a,b):
        return (a>b) - (a<b)

def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]
    
    for count, colour in pixels:
#         print(colour)
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)

#     print(most_frequent_pixel)
    return most_frequent_pixel[1]

# img.show()
print(most_frequent_colour(img))


# In[ ]:




