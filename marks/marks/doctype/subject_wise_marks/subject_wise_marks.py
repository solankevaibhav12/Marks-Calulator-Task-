# Copyright (c) 2022, Dexciss and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SubjectWiseMarks(Document):
	def before_save(self):
		# calling method for creating automatic marksheet
		self.create_marksheet()
		
# Throwing validation error if obtained marks are greater than total marks
	def validate(self):
		if (self.obtained_marks > self.total_marks):
			frappe.throw("Obtained marks cannot be greater than total marks")
				

# Creating automatic marksheet after entering subject wise marks for students and appending details in child table
	def create_marksheet(self):
		list_of_marksheets = []

		marksheets = frappe.db.get_list("Student Marksheet",{"docstatus":0},["student_name"])
		for i in marksheets:
			list_of_marksheets.append(i.get("student_name"))

		if self.student in list_of_marksheets:
			soc = frappe.get_doc("Student Marksheet",{"student_name":self.student})
			soc.append("marks_details",{
				"subject_name":self.subject_name,
				"total_marks":self.total_marks,
				"obtained_marks":self.obtained_marks
			})
			soc.save()
		else:
			new_marksheet = frappe.new_doc('Student Marksheet')
			new_marksheet.student_name = self.student
				
			new_marksheet.append("marks_details",{
			"subject_name":self.subject_name,
			"total_marks":self.total_marks,
			"obtained_marks":self.obtained_marks

			})
			new_marksheet.save()

