import frappe

def get_context(context):
    context.notices = get_notices()
    
@frappe.whitelist()
def get_notices():
    notices = frappe.get_all("Notice", fields=["title", "category", "tags"])
    return notices

