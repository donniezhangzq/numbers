# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render
from django.http import HttpResponse
from facai.models import Number 



def index(request):
	return render(request, "index.html")

def result(request):
	number_1 = request.POST.get('number_1', '')
	number_2 = request.POST.get('number_2', '')
	number_3 = request.POST.get('number_3', '')
	number_4 = request.POST.get('number_4', '')
	number_5 = request.POST.get('number_5', '')
	number_6 = request.POST.get('number_6', '')
	number_7 = request.POST.get('number_7', '')
	number_8 = request.POST.get('number_8', '')
	number_9 = request.POST.get('number_9', '')
	
	try:

		number_list = [int(number_1), int(number_2), int(number_3), int(number_4), int(number_5), 
				int(number_6), int(number_7), int(number_8), int(number_9)]
	except Exception:
		return HttpResponse("some number is not interger")
	
	rows = getdata(number_list)
	
	mapstr = ""
	t = 1
	for i in number_list:
		tmpstr = "%d->%d | " % (t, i)
		mapstr = mapstr + tmpstr
		t += 1

	data = {'rows': rows, "mapstr": mapstr}
	return render(request, "result.html", data)

def getdata(number_list):
	rows = []
	setlist = []
	i=1
	j=0
	k=0
	t=0
	l=0
	while i < 6:
		j = i+1
		while j < 7:
			k= j+1
			while k < 8:
				t = k+1
				while t < 9:
					l= t+1
					while l < 10:
						setlist.append([str(i), str(j), str(k), str(t), str(l)])
						l += 1
					t += 1
				k += 1
			j += 1
		i += 1
	
	for s in setlist:
		tmp = {}
		tmp['set'] = " ".join(s)
		tmp['result'] = number_list[int(s[0])-1] + number_list[int(s[1])-1] + number_list[int(s[2])-1] + number_list[int(s[3])-1] + number_list[int(s[4])-1]
		tmp['caculation'] = "%s%s%s%s%s" % (
				tostr(int(s[0]), number_list, True),
				tostr(int(s[1]), number_list, False),
				tostr(int(s[2]), number_list, False),
				tostr(int(s[3]), number_list, False),
				tostr(int(s[4]), number_list, False))
		rows.append(tmp)
	return rows

def tostr(number, number_list, is_first):
	tmp = number_list[int(number)-1] 
	if tmp >= 0:
		if is_first:
			result = str(tmp) 
		else:
			result = "+%d" % tmp
	else:
		result = str(tmp)

	return result
