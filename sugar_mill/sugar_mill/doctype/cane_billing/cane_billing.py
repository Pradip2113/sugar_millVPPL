# Copyright (c) 2023, Quantbit and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class CaneBilling(Document):
    
    @frappe.whitelist()
    def vivek(self):
        doc = frappe.db.get_list(
				"Farmer List",
				fields=[
					"name",
					"supplier_name",
					"supplier_group",
				],
			)
        for d in doc:
            self.append(
						"farmer_table",
						{
							"farmer_id": d.name,	
							"farmer_name": d.supplier_name,
							"village": d.supplier_group,
						},
					)
            
    @frappe.whitelist()
    def selectall(self):
        # pass
        children = self.get("farmer_table")
        if not children:
            return
        all_selected = all([child.check for child in children])
        value = 0 if all_selected else 1
        for child in children:
            child.check = value
            
            
            
        
    @frappe.whitelist()
    def billing(self):
        total_weight=0
        cane_rate=4.5
        Total_collection_amount=0
        total_deduction=0
        for FAR in self.get("farmer_table"):
            if FAR.check:
                doc = frappe.get_all('Cane Weight', filters={'farmer_code': FAR.farmer_id}, fields={"actual_weight","farmer_code"})
                # frappe.msgprint(str(doc))
                for d in doc:
                    total_weight += int(d.actual_weight)
                    
                Total_collection_amount = total_weight * cane_rate
                # frappe.msgprint(str(total_weight))
                # frappe.msgprint(str(Total_collection_amount))
                
                
                deduction_doc = frappe.get_all('Sales Invoice', filters={'customer': FAR.farmer_id ,'status':"Unpaid"}, fields={"outstanding_amount","customer"})
                for d_d in deduction_doc:
                    total_deduction += int(d_d.outstanding_amount)
                # frappe.msgprint(str(total_deduction))
                
                
                self.append(
                    "calculation_table",
                    {
                        "farmer_name": FAR.farmer_name,
                        "farmer_id": FAR.farmer_id,
                        "village": FAR.village,
                        "total_collection_amount":Total_collection_amount ,
                        "total_deduction": total_deduction ,
                        "total_payable_amount": int(Total_collection_amount) - int(total_deduction),
                    },
                )
