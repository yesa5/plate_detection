import httplib2
import requests

link = input()

page = requests.get(link).text
page = page[page.find('<div class="gallery__container">'):]
l = page.find('<a href="')
r = page[l:].find('">')
try:
    h = httplib2.Http('.cache')
    response, content = h.request(page[l + 9 :l + r])
    out = open('img.jpg', 'wb')
    out.write(content)
    out.close()
    cnt += 1
    print(cnt)
except:
    pass