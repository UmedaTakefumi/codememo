#!/usr/bin/env python

"""
./test_index.py -v
"""

import unittest
from index import *
import urllib.request

class TestHttpAccessUwsgi(unittest.TestCase):
    """
    """
    def test_http_access_uwsgi(self):
        
        url = 'http://localhost:4649'
        expected = b"Hello World\n"

        #ref: https://qiita.com/hoto17296/items/8fcf55cc6cd823a18217

        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as res:
          http_client_req_body = res.read()

        self.assertEqual(expected,http_client_req_body)

if __name__ == "__main__":
    unittest.main()

