"""
pwinty.py
~~~~~~~~~~~~~~~

This Python module wraps the photo printing API provided by Pwinty.com

Matt Gorecki
http://github.com/mattgorecki/pwinty
"""

import requests
import json

class Pwinty(object):
	def __init__(self, apikey=None, merchantid=None, sandbox=False):
		self.apikey = apikey
		self.merchantid = merchantid
		
		if sandbox:
			self.url = "https://sandbox.pwinty.com/"
		else:
			self.url = "https://api.pwinty.com/"

	def _headers(self):
		headers = {'X-Pwinty-MerchantId': self.merchantid, 'X-Pwinty-REST-API-Key': self.apikey}
		return headers

	def _rest_connect(self, resource, method, params=None, data=None, files=None):
		r = requests.request(method, self.url + resource, headers=self._headers(), params=params, data=data, files=files)

		if r.status_code == 200 or r.status_code == 201:
			if r.text:
				return json.loads(r.text)
			else:
				return r.content
		else:
			response = json.loads(r.content)
			raise PwintyError("Pwinty Error: " + r.text, r.status_code, response)

	### /Orders operations
	def create_order(self, **kwargs):
		'''
		/Orders (POST)
		Create new order
		'''
		return self._rest_connect('Orders', 'POST', data=kwargs)

	def modify_order(self, **kwargs):
		'''
		/Orders (PUT)
		Modify existing order information
		'''
		return self._rest_connect('Orders', 'PUT', data=kwargs)

	def view_order(self, **kwargs):
		'''
		/Orders (GET)
		View information about order.  Returns all orders if id not specified.
		'''
		return self._rest_connect('Orders', 'GET', params=kwargs)

	def delete_order(self, **kwargs):
		'''
		/Orders/Status (POST)
		Delete order
		'''
		kwargs['status'] == "Cancelled"
		return self._rest_connect('Orders/Status', 'POST', data=kwargs)

	def submit_order(self, **kwargs):
		'''
		/Orders/Status (POST)
		Submit order
		'''
		kwargs['status'] == "Submitted"
		return self._rest_connect('Orders/Status', 'POST', data=kwargs)

	def view_order_status(self, **kwargs):
		'''
		/Orders/SubmissionStatus (GET)
		Check if order is ready for submission.  Show errors otherwise.
		'''
		return self._rest_connect('Orders/SubmissionStatus', 'GET', params=kwargs)

	### /Photos operations
	def view_photo(self, **kwargs):
		'''
		/Photos (GET)
		Retrieve information about a specific photo
		'''
		return self._rest_connect('Photos', 'GET', params=kwargs)

	def add_photo(self, **kwargs):
		'''
		/Photos (POST)
		Add photo to order
		'''
		if "filename" in kwargs:
			files = {'file': open(kwargs['filename'], 'rb')}
			return self._rest_connect('Photos', 'POST', data=kwargs, files=files)
		elif "url" in kwargs:
			return self._rest_connect('Photos', 'POST', data=kwargs)
		else:
			raise Exception("Filename OR photo URL required")
			

	def delete_photo(self, **kwargs):
		'''
		/Photos (DELETE)
		Delete photo from order
		'''
		return self._rest_connect('Photos', 'DELETE', params=kwargs)

	### /Documents operations
	def view_document(self, **kwargs):
		'''
		/Documents (GET)
		Get information about a specific document
		'''
		return self._rest_connect('Documents', 'GET', params=kwargs)

	def add_document(self, **kwargs):
		'''
		/Documents (POST)
		Add document to existing order
		'''
		files = {'file': open(kwargs['filename'], 'rb')}
	
		return self._rest_connect('Documents', 'POST', data=kwargs, files=files)

	def delete_document(self, **kwargs):
		'''
		/Documents (DELETE)
		Delete document from order
		'''
		return self._rest_connect('Documents', 'DELETE', params=kwargs)

	### /Stickers operations
	def view_sticker(self, **kwargs):
		'''
		/Stickers (GET)
		Get information about specific sticker
		'''
		return self._rest_connect('Stickers', 'GET', params=kwargs)

	def add_sticker(self, **kwargs):
		'''
		/Stickers (POST)
		Add sticker to order
		'''
		filename = kwargs['filename']
		files = {'file': open(filename, 'rb')}

		return self._rest_connect('Stickers', 'POST', data=kwargs, files=files)

	def delete_sticker(self, **kwargs):
		'''
		/Stickers (DELETE)
		Delete sticker from order
		'''
		return self._rest_connect('Stickers', 'DELETE', params=kwargs)

#class PwintyError(Exception):
#	pass

class PwintyError(Exception):
	def __init__(self, message, status_code, response):
		self.message = message
		self.status_code = status_code
		self.error = response['error']

	def __str__(self):
		return repr(self.message)
