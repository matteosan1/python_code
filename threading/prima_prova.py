# $Id: dllib.py 909 2005-05-06 01:05:53Z Daniele $
__version__ = "$Revision: 909 $"[11:-2]

import os
import sys
import threading
from sets import Set
from urllib2 import urlopen

from util import get_logger

logger = get_logger("download")

class DownloadManager:
    """Download a set of url contents into local files."""
    MAX_THREADS = 10
    lock = threading.Lock()

    def __init__(self, urls):
        """Create a new `DownloadManager`

        :Parameters:
          * `urls` (`list` of 2-`tuples`): each couple (`url`, `file`) will
            become an asynchronous job and run.

        """
        self.urls = urls

        logger.info("%d files to download" % len(self.urls))

        for i in range(min(self.MAX_THREADS, len(self.urls))):
            url, filename = self.urls.pop()
            j = Job(url, filename, self.on_finish)
            j.start()

    def on_finish(self, job):
        self.lock.acquire()
        if self.urls:
            logger.info("%d files to go" % len(self.urls))
            url, filename = self.urls.pop()
            j = Job(url, filename, self.on_finish)
            j.start()

        self.lock.release()

class Job(threading.Thread):
    """The download of an url's contents.

    A failed download will be tried `TRYS` times before giving up.
    """
    TRYS = 3
    def __init__(self, url, filename, callback):
        """Create a new `Job`.
        :Parameters:
          * `url` (`str`): the url to be retrieved
          * `filename` (`str`): the file name to be stored
          * `callback` (callable): the function to be called when the job is
            finished. The callback signature is ``callback(job)`` where `job`
            is the caler `Job` instance.
        """
        threading.Thread.__init__(self)
        self.callback = callback
        self.url = url
        self.filename = filename

        logger.info("%s: job created" % url)

    def run(self):
        ok = False
        filename = self.filename
        url = self.url

        for itry in range(self.TRYS):
            try:
                fi = urlopen(url)
                logger.info("%s: url found" % url)
                try:
                    fo = open(filename, "wb")
                    try:
                        while 1:
                            buffer = fi.read(8192)
                            if not buffer:
                                break
                            fo.write(buffer)
                    finally:
                        fo.close()
                finally:
                    fi.close()

            except Exception, exc:
                logger.warning("%s: error opening: %s" % (url, exc))
                # Remove partially downloaded files
                if os.path.exists(filename):
                    os.remove(filename)

            else: # Downloaded: don't try further
                ok = True
                break

        if ok:
            logger.info("%s: download OK" % (url))
        else:
            logger.warning("%s: download FAILED" % (url))

        self.callback(self)

