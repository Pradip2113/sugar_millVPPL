# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FarmerList(Document):
    
	
	def before_save(self):
		
		existing_supplier = frappe.get_all('Supplier', filters={'name': self.name})
		if len(existing_supplier)==0:
			m=frappe.new_doc('Supplier')
			m.supplier_type=self.supplier_type
			m.supplier_name=self.supplier_name
			m.supplier_group=self.supplier_group
			m.insert()
			doc = frappe.db.get_all("Supplier", fields=["name"], order_by="creation DESC", limit=1)
			frappe.db.set_value("Supplier", doc[0].name, "name", self.name)
	# ------------------------------------------------------------------------------------------------------------------------------------
			k=frappe.new_doc('Customer')
			k.customer_type=self.supplier_type
			k.customer_name=self.supplier_name
			k.customer_group=self.supplier_group
			k.territory="India"
			k.insert()
			moc = frappe.db.get_all("Customer", fields=["name"], order_by="creation DESC", limit=1)
			frappe.db.set_value("Customer", moc[0].name, "name", self.name)
	# ------------------------------------------------------------------------------------------------------------------------------------
			q=frappe.new_doc('Address')
			q.address_type="Billing"
			q.address_title=self.name 
			q.country="India"
			q.gst_category="Unregistered"
			q.pincode=self.pin_code
			q.address_line1 =self.village
			q.address_line2 =self.taluka
			q.city=self.circle_office
			q.state=self.state
			q.append(
							"links",
							{
								"link_doctype": "Supplier",
								"link_name": self.name,
								"link_title": "",
								
							},
						)
			q.append(
							"links",
							{
								"link_doctype": "Customer",
								"link_name": self.name,
								"link_title": "",
								
							},
						)
			q.insert()
	
			qoc=frappe.db.get_all("Address", fields=["name"], order_by="creation DESC", limit=1)
			frappe.db.set_value("Supplier", self.name, "supplier_primary_address", qoc[0].name)
			frappe.db.set_value("Supplier", self.name, "primary_address", f"{self.village}\n{self.taluka}\n{self.circle_office}\n{self.state}\n India")
			frappe.db.set_value("Customer",self.name, "customer_primary_address", qoc[0].name)
			frappe.db.set_value("Customer", self.name, "primary_address", f"{self.village}\n{self.taluka}\n{self.circle_office}\n{self.state}\n India") 
		else:
			frappe.db.set_value("Supplier", self.name, "supplier_type", self.supplier_type)
			frappe.db.set_value("Supplier", self.name, "supplier_name", self.supplier_name)
			frappe.db.set_value("Supplier", self.name, "supplier_group", self.supplier_group)
			frappe.db.set_value("Supplier", self.name, "primary_address", f"{self.village}\n{self.taluka}\n{self.circle_office}\n{self.state}\n India")
   
			frappe.db.set_value("Customer", self.name, "customer_name", self.supplier_name)
			frappe.db.set_value("Customer", self.name, "customer_group", self.supplier_group)
			frappe.db.set_value("Customer", self.name, "territory", "India")
			frappe.db.set_value("Customer", self.name, "primary_address", f"{self.village}\n{self.taluka}\n{self.circle_office}\n{self.state}\n India") 
   
			frappe.db.set_value("Address",self.name+"-Billing" , "address_line1", self.village)
			frappe.db.set_value("Address", self.name+"-Billing", "address_line2", self.taluka)
			frappe.db.set_value("Address", self.name+"-Billing", "city", self.circle_office)
			frappe.db.set_value("Address", self.name+"-Billing", "state", self.state)
			frappe.db.set_value("Address", self.name+"-Billing", "country", "India")
			frappe.db.set_value("Address", self.name+"-Billing", "pincode", self.pin_code)
			
		
	def on_trash(self):
		frappe.delete_doc("Supplier", self.name)
		frappe.delete_doc("Customer", self.name)
		# frappe.msgprint(doc[0].name)frappe.delete_doc("Crop Sampling", c.name)
		# frappe.msgprint(moc[0].name)
		# frappe.msgprint(qoc[0].name)




	# @frappe.whitelist()
	# def update_docs(self):
	# 	frappe.db.set_value("Supplier", self.name, "supplier_type", self.supplier_type)
	# 	frappe.db.set_value("Supplier", self.name, "supplier_name", self.supplier_name)
	# 	frappe.db.set_value("Supplier", self.name, "supplier_group", self.supplier_group)
	# 	frappe.db.set_value("Supplier", self.name, "address_line1", self.village)
	# 	frappe.db.set_value("Supplier", self.name, "address_line2", self.taluka)
	# 	frappe.db.set_value("Supplier", self.name, "city", self.circle_office)
	# 	frappe.db.set_value("Supplier", self.name, "state", self.state)
	# 	frappe.db.set_value("Supplier", self.name, "country", "India")
	# 	frappe.db.set_value("Supplier", self.name, "pincode", self.pin_code)

	# 	frappe.db.set_value("Customer", self.name, "customer_name", self.supplier_name)
	# 	frappe.db.set_value("Customer", self.name, "customer_group", self.supplier_group)
	# 	frappe.db.set_value("Customer", self.name, "territory", "India")
	# 	frappe.db.set_value("Customer", self.name, "address_line1", self.village)
	# 	frappe.db.set_value("Customer", self.name, "address_line2", self.taluka)
	# 	frappe.db.set_value("Customer", self.name, "city", self.circle_office)
	# 	frappe.db.set_value("Customer", self.name, "state", self.state)
	# 	frappe.db.set_value("Customer", self.name, "country", "India")
	# 	frappe.db.set_value("Customer", self.name, "pincode", self.pin_code)
		
		


		
		


	
