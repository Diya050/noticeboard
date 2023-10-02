import frappe

def get_context(context):
    context.notices = get_notices()
    
@frappe.whitelist()
def get_notices():
    if not frappe.has_permission("Notice", "read"):
        raise frappe.PermissionError

    notices = frappe.get_all("Notice", fields=["title", "category", "body", "tags", "posted_on"])

    return notices
