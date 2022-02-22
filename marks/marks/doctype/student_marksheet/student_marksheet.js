// Copyright (c) 2022, Dexciss and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Marksheet', {

	// Calling method from api.py to auto fill child table in Student Marksheet on change in student name
	student_name: function(frm){
		frappe.call({
						method : "marks.api.get_child",
						args: {
							student : frm.doc.student_name,
							
						},
						callback: function(r){
							if(r){
							console.log("r is ",r)
							
							cur_frm.add_child("marks_details", {
								subject_name : r.message[0],
								obtained_marks : r.message[1],
								total_marks: r.message[2]
								
								}),
							refresh_field("marks_details")}
							frm.doc.total_obtained_marks = r.message[1]
							refresh_field("total_obtained_marks")
							
						}})	
					},

// Applying filters and displaying only active students
	setup: function(frm){
		frm.set_query("student_name", function() {
							
			return {
				filters: [['is_active','=', '1']

					   				]};
							});
				
									 
					},	
	
	})
