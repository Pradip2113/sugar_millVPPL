// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Vehicle Registration item', {
	cart_no:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total1 = 0;
	frm.doc.vehicle_details_tab.forEach(function(d) { total1 = parseFloat(d.idx); });
	frm.set_value("total_numbers_of_vehicle", total1);
	refresh_field("total_numbers_of_vehicle");
  },
  vehicle_details_tab_remove:function(frm, cdt, cdn){
	var d = locals[cdt][cdn];
	var total1 = 0;
	frm.doc.vehicle_details_tab.forEach(function(d) { total1 = parseFloat(d.idx); });
	frm.set_value("total_numbers_of_vehicle", total1);
	refresh_field("total_numbers_of_vehicle");
   }
 });

 frappe.ui.form.on('Vehicle Registration', {
	after_save: function(frm) {
		frm.call({
			method:'vivo',//function name defined in python
			doc: frm.doc, //current document
		});
		
	}
});
