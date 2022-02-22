# Copyright (c) 2022, Dexciss and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class StudentMarksheet(Document):

	def before_save(self):
#	 Calling method to calculate total obtained marks
		self.get_total_obtained_marks()
		

# Calculating total obtained marks and displaying in the field total obtained marks
	def get_total_obtained_marks(self):
		total_marks = []
		for i in self.marks_details:	
			total_marks.append(i.obtained_marks)
			final_marks = sum(total_marks)
			self.total_obtained_marks = final_marks


