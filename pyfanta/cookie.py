#!/usr/bin/env python
import cookielib
import urllib
import urllib2

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
resp = opener.open('http://www.fantagazzetta.com') # save a cookie

theurl = 'http://www.fantagazzetta.com' # an example url that sets a cookie, try different urls here and see the cookie collection you can make !
body={'usr':'greenman','pwd':'greenman'}
txdata = urllib.urlencode(body) # if we were making a POST type request, we could encode a dictionary of values here - using urllib.urlencode
txheaders = {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'} # fake a user agent, some websites (like google) don't like automated exploration
					  
					  
try:
    req = urllib2.Request(theurl, txdata, txheaders) # create a request object
    handle = opener.open(req) # and open it to return a handle on the url
    HTMLSource = handle.read()
    f = file('test.html', 'w')
    f.write(HTMLSource)
    f.close()
     
except IOError, e:
    print 'We failed to open "%s".' % theurl
    if hasattr(e, 'code'):
        print 'We failed with error code - %s.' % e.code
    elif hasattr(e, 'reason'):
        print "The error object has the following 'reason' attribute :", e.reason
        print "This usually means the server doesn't exist, is down, or we don't have an internet connection."
        sys.exit()
    else:
        print 'Here are the headers of the page :'
        print handle.info() # handle.read() returns the page, handle.geturl() returns the true url of the page fetched (in case urlopen has followed any redirects, which it sometimes does)
