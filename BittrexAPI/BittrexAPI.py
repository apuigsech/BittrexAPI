#!/usr/bin/env python

# BittrexAPI: Python Bittrex API implementation
#
# Copyright (c) 2014 - Albert Puigsech Galicia (albert@puigsech.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import random
import requests
from requests.auth import AuthBase
import hmac
import hashlib
import json
import urllib

API = {
  'public' : ['getmarkets', 'getcurrencies', 'getticker', 'getmarketsummaries', 'getorderbook','getmarkethistory'],
  'market' : ['getopenorders', 'cancel', 'sellmarket', 'selllimit', 'buymarket', 'buylimit'],
  'acount' : ['getbalances', 'getbalance', 'getdepositaddress', 'withdraw'],
}


class BittrexAPI:
  def __init__(self, key, secret, simulation=False, cached=False):
    self.url = 'https://bittrex.com/api/v1.1'
    self.key = key
    self.secret = secret
    self.simulation = simulation
    self.cached = cached
    self.cache = {}


  def request(self, method, args=None):
    if args == None:
      args = {}

    for api in API:
      if method in API[api]:
        break
    else:
      api = None

    if api == None:
        return None

    url = '{0}/{1}/{2}'.format(self.url, api, method)
    url += '?' + urllib.urlencode(args)

    res = requests.get(
      url
    )

    return json.loads(res.text)


  def getmarkets(self, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getmarkets'
    if cached == False or self.cached.has_key(keycache) == False:
      self.cache[keycache] = self.request('getmarkets')
    return self.cache[keycache]


  def getcurrencies(self, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getcurrencies'
    if cached == False or self.cached.has_key(keycache) == False:
      self.cache[keycache] = self.request('getcurrencies')
    return self.cache[keycache]


  def getticker(self, market, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getticker'+str(market)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'market': market
      }
      self.cache[keycache] = self.request('getticker', args)
    return self.cache[keycache]


  def getmarketsummaries(self, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getmarketsummaries'
    if cached == False or self.cached.has_key(keycache) == False:
      self.cache[keycache] = self.request('getmarketsummaries')
    return self.cache[keycache]


  def getmarketsummary(self, market, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getmarketsummary'+str(market)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'market': market
      }
      self.cache[keycache] = self.request('getmarketsummary', args)
    return self.cache[keycache]


  def getorderbook(self, market, type='both', depth=20, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getorderbook'+str(market)+str(type)+str(depth)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'market': market,
        'type': type,
        'depth': depth,
      }
      self.cache[keycache] = self.request('getorderbook', args)
    return self.cache[keycache]


  def getmarkethistory(self, market, count=20, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getmarkethistory'+str(market)+str(count)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'market': market,
        'count': count,
      }
      self.cache[keycache] = self.request('getmarkethistory', args)
    return self.cache[keycache]


  def buylimit(self, market, quantity, rate, simulated=None):
    if simulated == None:
      simulated = self.simulated

    if simulated == False:
      args = {
        'market': market,
        'quantity': quantity,
        'rate': rate
      }
      r = self.request('buylimit', args)
    else:
      r = None
    return r


def buymarket(self, market, quantity, rate=None, simulated=None):
    if simulated == None:
      simulated = self.simulated

    if simulated == False:
      args = {
        'market': market,
        'quantity': quantity,
        'rate': rate
      }
      r = self.request('buylimit', args)
    else:
      r = None
    return r


  def selllimit(self, market, quantity, rate, simulated=None):
    if simulated == None:
      simulated = self.simulated

    if simulated == False:
      args = {
        'market': market,
        'quantity': quantity,
        'rate': rate
      }
      r = self.request('selllimit', args)
    else:
      r = None
    return r


def sellmarket(self, market, quantity, rate=None, simulated=None):
    if simulated == None:
      simulated = self.simulated

    if simulated == False:
      args = {
        'market': market,
        'quantity': quantity,
        'rate': rate
      }
      r = self.request('selllimit', args)
    else:
      r = None
    return r


def cancel(self, uuid, simulated=None):
    if simulated == None:
      simulated = self.simulated

    if simulated == False:
      args = {
        'uuid': uuid
      }
      r = self.request('selllimit', args)
    else:
      r = None
    return r


  def getopenorders(self, market, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getopenorders'+str(market)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'market': market,
      }
      self.cache[keycache] = self.request('getopenorders', args)
    return self.cache[keycache]


  def getbalances(self, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getbalances'
    if cached == False or self.cached.has_key(keycache) == False:
      self.cache[keycache] = self.request('getbalances')
    return self.cache[keycache]


  def getbalance(self, currency, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getbalance'+str(currency)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'currency': currency,
      }
      self.cache[keycache] = self.request('getbalance', args)
    return self.cache[keycache]


  def getdepositaddress(self, currency, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getdepositaddress'+str(currency)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'currency': currency,
      }
      self.cache[keycache] = self.request('getdepositaddress', args)
    return self.cache[keycache]


def withdraw(self, currency, quantity, address, paymentid=None, simulated=None):
    if simulated == None:
      simulated = self.simulated

    if simulated == False:
      args = {
        'currency': currency,
        'quantity': quantity,
        'address': address,
        'paymentid': paymentid,
      }
      r = self.request('selllimit', args)
    else:
      r = None
    return r


def getorder(self, uuid, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getorder'+str(uuid)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'uuid': uuid,
      }
      self.cache[keycache] = self.request('getorder', args)
    return self.cache[keycache]


def getorderhistory(self, market=None, count=None, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getorderhistory'+str(market)+str(count)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'market': market,
        'count': count,
      }
      self.cache[keycache] = self.request('getorderhistory', args)
    return self.cache[keycache]


def getwithdrawalhistory(self, currency=None, count=None, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getwithdrawalhistory'+str(currency)+str(count)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'currency': currency,
        'count': count,
      }
      self.cache[keycache] = self.request('getwithdrawalhistory', args)
    return self.cache[keycache]


def getdeposithistory(self, currency=None, count=None, cached=None):
    if cached == None:
      cached = self.cached

    keycache = 'getdeposithistory'+str(currency)+str(count)
    if cached == False or self.cached.has_key(keycache) == False:
      args = {
        'currency': currency,
        'count': count,
      }
      self.cache[keycache] = self.request('getdeposithistory', args)
    return self.cache[keycache]