// Copyright (c) 2023, Quantbit and contributors
// For license information, please see license.txt

frappe.ui.form.on('Cane Billing', {
	
	onload: function(frm) {

		frm.clear_table("farmer_table")
		frm.refresh_field('farmer_table')
		frm.call({
				method:'vivek',//function name defined in python
				doc: frm.doc, //current document
			});

	}
});

frappe.ui.form.on('Cane Billing', {
	select_all: function(frm) {
		frm.call({
			method: 'selectall',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});

frappe.ui.form.on('Cane Billing', {
	
	do_billing: function(frm) {
		frm.clear_table("calculation_table")
		frm.refresh_field('calculation_table')
		frm.call({
			method: 'billing',//function name defined in python
			doc: frm.doc, //current document
		});

	}
});

// frappe.ui.form.on('Cane Billing', {
//     onload: function(frm) {
//         frm.fields_dict['farmer_table'].grid.settings.limit =10;
//         frm.fields_dict['farmer_table'].grid.refresh();
//     }
// });
