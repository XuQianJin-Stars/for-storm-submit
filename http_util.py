#!/usr/bin/env python
# -*- coding:utf-8 -*-
import urllib
import urllib2


# GET：
def get(URL):
    response = urllib2.urlopen(URL)
    return response.read()


# POST
def post(URL, values):
    data = urllib.urlencode(values)
    print data
    req = urllib2.Request(URL, data)
    response = urllib2.urlopen(req)
    return response.read()


# PUT
def put(URL, data):
    request = urllib2.Request(URL, data=data)
    request.add_header('Content-Type', 'your/contenttype')
    request.get_method = lambda: 'PUT'
    response = urllib2.urlopen(request)


# DELETE
def delete(URL):
    request = urllib2.Request(URL)
    request.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(request)
