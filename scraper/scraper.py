import sqlite3
import urllib2
import lxml
import time

from lxml.cssselect import CSSSelector
# from lxml.etree import fromstring
import lxml.html

DB = 'content.db'

def get_conn():
    return sqlite3.connect(DB)

def init_tables():
    """docstring for init_tables"""
    conn = get_conn()
    c = conn.cursor()

    # Create table


def get_soup(uri):
    result = urllib2.urlopen(uri).read()
    # print result
    return lxml.html.fromstring(result)


def scrape(incr):
    """Scrape the page at increment incr and return a dict"""
    base_uri = "http://www.thecitizensfoundation.org/schoolpage.aspx?campusid=%s"
    results = []
    soup = get_soup(base_uri %incr)
    # print soup
    sel_schoolinfo = CSSSelector(".schoolInformation")
    scinfo = list(sel_schoolinfo(soup))
    for n in xrange(2):
        pane = scinfo[n].iterchildren()
        results += [(x.findall('td')[0].text_content(), x.findall('td')[1].text_content()) for x in pane]
    return dict(results)

def start():
    """docstring for start"""
    for i in xrange(1, 700):
        print "Page %s" %i
        print scrape(i)
        time.sleep(0.3)


if __name__ == '__main__':
    start()


