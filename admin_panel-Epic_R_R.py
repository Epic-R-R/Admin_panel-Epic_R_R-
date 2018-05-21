#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib2 import Request, urlopen, URLError, HTTPError

def Space(j):
	i = 0
	while i<=j:
		print " ",
		i+=1
def findAdmin():
	f = open("panel_link.txt","r");
	link = raw_input("Enter Site Name (ex : example.com or www.example.com): ")
	print "\n\nGood URL : \n"
	while True:
		sub_link = f.readline()
		if not sub_link:
			break
		req_link = "http://"+link+"/"+sub_link
		req = Request(req_link)
		try:
			response = urlopen(req)
		except HTTPError as e:
			continue
		except URLError as e:
			continue
		else:
			print "OK => ",req_link

def Credit():
	Space(9); print "######################################"
	Space(9); print "#     +++  Admin Panel Finder  +++   #"
	Space(9); print "#  Cod3d By The Commander/> Epic_R_R #"
	Space(9); print "#        Nothing Is Impossible       #"
	Space(9); print "#            /*Epic_R_R*/            #"
	Space(9); print "#####################################"

Credit()
findAdmin()
