import urllib.request as request
import urllib
import re
import os

IMAGES = 'images'

try:
    import Image
except ImportError:
    from PIL import Image

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import requests

def search_google_image(search_term):

    url = 'https://www.googleapis.com/customsearch/v1'
    response = requests.get(url, params={'q': search_term, 'num': 1, 'start': 1, 'imgSize': "medium",
                                     'searchType': "image", 'key': 'AIzaSyCHiNZOR3jks2sguztp3xnLoH1plzURkow', 'cx' : '012763076801589293049:rxhgz0ebbac'})
    data = response.json()
    try:
        return save_image(search_term, data)

    except KeyError:
        print('No image found for {}'.format(search_term))
        return ('no_photo.jpg')

def save_image(search_term, data):

    img_link = data['items'][0]['link']
    img_name = search_term.strip().replace(" ", "")
    img_name = re.sub('[^A-Za-z0-9]+', '', img_name)[:10]

    if not os.path.exists(IMAGES):
        os.makedirs(IMAGES)

    img_path = "{}/{}.jpg".format(IMAGES, img_name)
    urllib.request.urlretrieve(img_link, img_path)

    return img_path




