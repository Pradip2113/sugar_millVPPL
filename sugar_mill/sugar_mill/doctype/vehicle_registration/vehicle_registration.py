# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class VehicleRegistration(Document):
    # pass
	@frappe.whitelist()
	def vivo(self):
		doc = frappe.get_all('Vehicle Registration', filters={'h_and_t_contract': self.h_and_t_contract}, fields={"total_numbers_of_vehicle","name"})
		# frappe.msgprint(str(s))
		for s in doc:
			# frappe.msgprint(str(s.total_numbers_of_vehicle))
			frappe.db.set_value("H and T Contract", self.h_and_t_contract, "total_vehicle",self.total_numbers_of_vehicle)

