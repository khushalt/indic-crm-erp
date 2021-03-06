# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe.model.document import Document
from frappe.utils.jinja import validate_template

class TermsandConditions(Document):
	def validate(self):
		validate_template(self.terms)

@frappe.whitelist()
def get_terms_and_conditions(template_name, doc):
	if isinstance(doc, basestring):
		doc = json.loads(doc)

	terms_and_conditions = frappe.get_doc("Terms and Conditions", template_name)
	return frappe.render_template(terms_and_conditions.terms, doc)