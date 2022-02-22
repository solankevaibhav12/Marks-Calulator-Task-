// Copyright (c) 2022, Dexciss and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Details', {
	before_save: function(frm) {

//  Getting student's full name from first name and last name
	let first = frm.doc.student_first_name
	let last = frm.doc.student_last_name
	frm.doc.student_full_name = first + " " + last

	
	
}


	});
