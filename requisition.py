import datetime

req_counter = 10000


class Requisition:
    def __init__(self, date, staff_id, staff_name):
        global req_counter
        req_counter = req_counter + 1

        self.requisition_id = str(req_counter)
        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.items = []
        self.total = 0.0
        self.status = "Pending"
        self.approval_reference = "Not available"

def add_requisition_items(self, items):
        for item_name, item_price in items:
            self.items.append((item_name, item_price))
            self.total = self.total + item_price
        return self.total

def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + self.requisition_id[-3:]
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"
        return self.status

def respond_requisition(self, decision):
        clean_decision = decision.strip().capitalize()
        if self.status == "Pending":
            if clean_decision == "Approved":
                self.status = "Approved"
                self.approval_reference = self.staff_id + self.requisition_id[-3:]
            elif clean_decision == "Not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"
            elif clean_decision == "Pending":
                self.status = "Pending"
                self.approval_reference = "Not available"
        return self.status