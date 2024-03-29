# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HandTContract(Document):
	@frappe.whitelist()
	def on_submit(self):
		# moc = frappe.new_doc("Vehicle Registration")
		# moc.h_and_t_contract = self.name
		# moc.transporter_code = self.transporter_code
		# moc.contractor_name = self.h_and_t_group
		# moc.total_numbers_of_vehicle = self.total_vehicle
		# moc.season = self.season
		# count=1
		# for i in range(int(self.total_vehicle)):
		# 	moc.append(
		# 		"vehicle_details_tab",
		# 		{
		# 			# "cart_no":str(count),
		# 			"driver_name": self.transporter_code,
		# 			"vehicle_type":self.vehicle_type,
		# 			"capcity":self.total_vehicle,
		# 			"vehicle_number":self.vehicle_no,
			
		# 		},
		# 	)
		# 	count=count+1
		# moc.insert()
		# moc.save()
#   ----------------------------------------------------------------------------------------

		
		moc = frappe.new_doc("Vehicle Registration")
		moc.h_and_t_contract = self.name
		moc.transporter_code = self.transporter_code
		moc.contractor_name = self.h_and_t_group
		moc.total_numbers_of_vehicle = self.total_vehicle
		moc.season = self.season
		for i in range(int(self.total_vehicle)):
			vehicle_detail = moc.append("vehicle_details_tab", {})
			vehicle_detail.driver_name = self.transporter_code
			vehicle_detail.vehicle_type = self.vehicle_type
			vehicle_detail.capacity = self.total_vehicle
			vehicle_detail.vehicle_number = self.vehicle_no
		moc.save()

#  -------------------------------------------------------------------------------------------
	@frappe.whitelist()
	def on_update_after_submit(self):
		frappe.db.set_value("Vehicle Registration", str(self.season)+"-"+str(self.name), "contractor_name",self.h_and_t_group)
		frappe.db.set_value("Vehicle Registration",str(self.season)+"-"+str(self.name), "transporter_code",self.transporter_code)
    
    
    
	# @frappe.whitelist()
	# def before_save(self):
	# 	for i in range(1, self.total_vehicle + 1):
	# 		moc1 = frappe.new_doc("Cart No")
	# 		moc1.cart_no = f"{i}"
	# 		moc1.insert()
   
	# 	moc = frappe.new_doc("Vehicle Registration")
	# 	moc.contractor_name = self.h_and_t_group
	# 	moc.total_numbers_of_vehicle = self.total_vehicle
	# 	moc.season = self.season
	# 	count=1
	# 	for i in range(int(self.total_vehicle)):
	# 		for m in frappe.get_list("Cart No"):
	# 			moc.append(
	# 				"vehicle_details_tab",
	# 				{
	# 					"cart_no": m.name,
	# 					"driver_name": self.transporter_name,
	# 					"vehicle_type":self.vehicle_type,
	# 					"capcity":self.total_vehicle,
	# 					"vehicle_number":self.vehicle_no,
	# 					"h_and_t_contract":self.name
				
	# 				},
	# 			)
	# 		break
	# 		count=count+1
	# 	moc.insert()
	# 	moc.save()

    
			
			
				# 	moc = frappe.new_doc("Vehicle Registration")
				# 	moc.h_and_t_contract = self.name
				# 	moc.total_numbers_of_vehicle = self.total_vehicle
				# 	moc.season = self.season
				# 	for m in frappe.get_list("Cart No"):
				# 		if moc.h_and_t_contract == moc1.h_and_t_contract:
				# 			moc.append(
				# 				"vehicle_details_tab",
				# 				{
				# 					"cart_no": m.name,
				# 					"driver_name": self.transporter_name,
				# 					"vehicle_type":self.vehicle_type,
				# 					"capcity":self.total_vehicle,
				# 					"vehicle_number":self.vehicle_no,
				# 					"h_and_t_contract":self.name
							
				# 				},
				# 			)
				# 		break
				# 	moc.insert()
				# 	moc.save()
				# else:
				# 	frappe.msgprint("hiiiiii")
    
 


