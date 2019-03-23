# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render
from django.http import HttpResponse
from facai.models import Number 



def index(request):
	return render(request, "index.html")

def version2(request):
	return render(request, "version2.html")

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

def result_version2(request):
	numbers = [0 for i in range(55)]
	numbers_map = {}
	i = 1
	j = 0
	k = 0
	while i < 11:
		j = i+1
		while j < 12:
			numbers[k] = "%d_%d" % (i, j)
			k += 1
			j += 1
		i = i+1
	
	i = 0
	try:
		while i < 55:
			key = "number_" + str(numbers[i])
			numbers_map[numbers[i]] = int(request.POST.get(key, ""))
			i += 1
	except Exception:
		return HttpResponse("some number is not interger")

	rows = getdata_version2(numbers_map)
	if len(rows) == 0:
		return HttpResponse("something is error")

	mapstr = ""
	for i in numbers:
		mapstr += "%s->%d | " % (i, numbers_map[i])

	data = {'rows': rows, "mapstr": mapstr}

	return render(request, "result_version2.html", data)


def getdata(number_list):
	rows = []
	selist = get_setlist()

	for s in setlist:
		tmp = {}
		tmp['set'] = ""
		for i in s:
			tmp['set'] += str(i) + " "

		tmp['result'] = number_list[s[0]-1] + number_list[s[1]-1] + number_list[s[2]-1] + number_list[s[3]-1] + number_list[s[4]-1]
		tmp['caculation'] = "%s%s%s%s%s" % (
				tostr(number_list[s[0]-1], True),
				tostr(number_list[s[1]-1], False),
				tostr(number_list[s[2]-1], False),
				tostr(number_list[s[3]-1], False),
				tostr(number_list[s[4]-1], False))
		rows.append(tmp)
	return rows

def getdata_version2(numbers_map):
	rows = []
	setlist = get_setlist()

	for s in setlist:
		tmp = {}
		tmp['set'] = ""
		for i in s:
			tmp['set'] += str(i) + " "

		c_list = c52_version3(s)
		tmp['subset'] = " ".join(c_list)

		if len(c_list) == 0:
			return []

		tmp['result'] = 0
		tmp['caculation'] = ""
		for i in c_list:
			tmp['result'] += numbers_map[i]
			if i == 0:
				tmp['caculation'] += tostr(numbers_map[i], True)
			else:
				tmp['caculation'] += tostr(numbers_map[i], False)
		rows.append(tmp)

	return rows


def c52(l):
	result = [0 for i in range(10)]

	if len(l) != 5:
		return []
	
	l.sort()
	i = 0
	j = 0
	t = 0
	while i < 4:
		j = i+1
		while j < 5:
			result[t] = "%d_%d" % (l[i], l[j])
			t += 1
			j += 1
		i += 1
	
	if len(result) != 10:
		return []

	return result

def c52_version3(l):
	result = [0 for i in range(4)]
	
	if len(l) != 5:
		return []

	l.sort()
	result[0] = "%d_%d" % (l[0], l[1])
	result[1] = "%d_%d" % (l[0], l[2])
	result[2] = "%d_%d" % (l[0], l[3])
	result[3] = "%d_%d" % (l[0], l[4])

	return result
	

def	get_setlist():
	setlist = []
	i=1
	j=0
	k=0
	t=0
	l=0
	while i < 8:
		j = i+1
		while j < 9:
			k= j+1
			while k < 10:
				t = k+1
				while t < 11:
					l= t+1
					while l < 12:
						setlist.append([i, j, k, t, l])
						l += 1
					t += 1
				k += 1
			j += 1
		i += 1
	return setlist

def tostr(tmp, is_first):
	if tmp >= 0:
		if is_first:
			result = str(tmp) 
		else:
			result = "+%d" % tmp
	else:
		result = str(tmp)

	return result
