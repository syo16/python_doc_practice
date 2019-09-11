import io
import requests
from PIL import Image

url = 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'

r = requests.get(url)

img_io = io.BytesIO(r.content)
img = Image.open(img_io)

img.save('logo.png')
print(img_io.getvalue())
