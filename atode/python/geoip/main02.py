#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint
pp = pprint.PrettyPrinter(indent=4)

import geoip2.database
#pip install geoip2

reader = geoip2.database.Reader('GeoLite2-City_20170704/GeoLite2-City.mmdb')

ip_addr = '172.217.27.83'
response = reader.city(ip_addr)

pp.pprint(response)

# wget http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
# tar zxvf GeoLite2-City.tar.gz
# http://dev.maxmind.com/geoip/geoip2/geolite2/
