import urllib.request as request
import simplejson
import urllib

try:
    import Image
except ImportError:
    from PIL import Image

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import json, requests

def search_google_image(search_term):

    url = 'https://www.googleapis.com/customsearch/v1'
    response = requests.get(url, params={'q': search_term, 'num': 1, 'start': 1, 'imgSize': "medium",
                                     'searchType': "image", 'key': 'AIzaSyCHiNZOR3jks2sguztp3xnLoH1plzURkow', 'cx' : '012763076801589293049:rxhgz0ebbac'})
    data = response.json()
    img_link = data['items'][0]['link']
    print(img_link)
    urllib.request.urlretrieve(img_link, "{}.jpg".format(search_term))

    return(img_link)



