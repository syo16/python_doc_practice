import functools
import time

import requests

@functools.lru_cache(maxsize=2048)
def get_page(i):
    r = requests.get('https://www.rfc-editor.org/rfc/rfc{}.txt'.format(i))
    return r.text

start = time.time()
for i in [1, 55, 33, 139, 55, 33, 22, 55, 22, 139, 55, 55, 55, 55, 55, 33, 22]:
    with open('{}.txt'.format(i), 'tw') as f:
        f.write(get_page(i))

print(time.time() - start)
