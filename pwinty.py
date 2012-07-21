import requests
import json

class Pwinty(object):
	def __init__(self, url=None, apikey=None, merchantid=None):
		self.url = url
		self.apikey = apikey
		self.merchantid = merchantid

		print "Pwinty started"

	### /Orders operations
	def create_order(self):
		'''
		/Orders (POST)
		Create new order
		'''
		pass

	def update_order(self):
		'''
		/Orders (PUT)
		Update existing order information
		'''
		pass

	def view_order(self):
		'''
		/Orders (GET)
		View information about order
		'''
		pass

	def set_order_status(self):
		'''
		/Orders/Status (POST)
		Submit or cancel an order
		'''
		pass

	def view_order_status(self):
		'''
		/Orders/SubmissionStatus (GET)
		Check if order is ready for submission.  Show errors otherwise.
		'''
		pass

	### /Photos operations
	def view_photo(self):
		'''
		/Photos (GET)
		Retrieve information about a specific photo
		'''
		pass

	def add_photo(self):
		'''
		/Photos (POST)
		Add photo to order
		'''
		pass

	def delete_photo(self):
		'''
		/Photos (DELETE)
		Delete photo from order
		'''
		pass

	### /Documents operations
	def view_document(self):
		'''
		/Documents (GET)
		Get information about a specific document
		'''
		pass

	def add_document(self):
		'''
		/Documents (POST)
		Add document to existing order
		'''
		pass

	def delete_document(self):
		'''
		/Documents (DELETE)
		Delete document from order
		'''

	### /Stickers operations
	def view_sticker(self):
		'''
		/Stickers (GET)
		Get information about specific sticker
		'''
		pass

	def add_sticker(self):
		'''
		/Stickers (POST)
		Add sticker to order
		'''
		pass

	def delete_sticker(self):
		'''
		/Stickers (DELETE)
		Delete sticker from order
		'''
		pass
