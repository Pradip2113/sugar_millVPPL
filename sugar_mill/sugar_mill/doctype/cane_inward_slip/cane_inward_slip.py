# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document



class CaneInwardSlip(Document):
		
	@frappe.whitelist()
	def cn(self):
		# eachdoc = frappe.get_doc("Vehicle Registration", self.transporter_code)
		doc = frappe.get_all('Vehicle Registration item', filters={'driver_name':self.transporter_code}, fields={"cart_no","name"})
		for d in doc:
			self.cartno=d.cart_no
			break
				

