from re import sub
import frappe


# Method to auto fill data in child table in doctype Student Marksheet
@frappe.whitelist()
def get_child(student):
    sub_name = frappe.db.get_value("Subject Wise Marks",{"student":student},"subject_name")
    obt_marks = frappe.db.get_value("Subject Wise Marks",{"student":student},"obtained_marks")
    tot_marks = frappe.db.get_value("Subject Wise Marks",{"student":student},"total_marks")
    
    return sub_name,obt_marks,tot_marks




        

   
    
