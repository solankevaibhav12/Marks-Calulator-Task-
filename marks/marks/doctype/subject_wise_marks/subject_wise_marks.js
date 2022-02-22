// Copyright (c) 2022, Dexciss and contributors
// For license information, please see license.txt

frappe.ui.form.on('Subject Wise Marks', {


	// Applying filters and displaying only active students
	setup: function(frm){
			frm.set_query("student", function() {
				
				return {
					   filters: [['is_active','=', '1']
					   ]};
			});
						 
		},	
	
});
