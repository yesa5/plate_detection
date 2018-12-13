from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
import httplib2
import requests
import cv2 
import numpy as np
import time
from PIL import Image
import pytesseract
import argparse
import os

def listt(request):
    return render(request, 'ml/main.html')#, {'fname': name})

def find(request):
	
	link = request.POST['url']
	page = requests.get(link).text
	page = page[page.find('<div class="gallery__container">'):]
	l = page.find('<a href="')
	r = page[l:].find('">')
	name = link[link.find('show/') + 5:]
	try:
	    h = httplib2.Http('.cache')
	    response, content = h.request(page[l + 9 :l + r])
	    out = open('data/' + name + '.jpg', 'wb')
	    out.write(content)
	    out.close()
	except:
	    print('Error')

	index = 0
	cnt = 0
	plateCascade = cv2.CascadeClassifier('data/haarcascade_russian_plate_number.xml')

	try:
	    frame = cv2.imread('data/' + name + '.jpg')
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    plaques = plateCascade.detectMultiScale(gray, 1.3, 5)
	    for i, (x, y, w, h) in enumerate(plaques):
	        roi_color = frame[y:y + h, x:x + w]
	        r = 400.0 / roi_color.shape[1]
	        dim = (400, int(roi_color.shape[0] * r))
	        resized = cv2.resize(roi_color, dim, interpolation = cv2.INTER_AREA)
	        w_resized=resized.shape[0]
	        h_resized=resized.shape[1]
	        cv2.imwrite('data/' + name + '.jpg', resized)
	        cnt += 1
	        frame[100:100+w_resized,100:100+h_resized] = resized     
	    cv2.destroyAllWindows()
	except:
		print('error')

	image = cv2.imread('data/'+name+'.jpg')
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.medianBlur(gray, 5)
	 
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)

	text = pytesseract.image_to_string(Image.open(filename), config='--psm 7')
	os.remove(filename)

	return redirect('listt')