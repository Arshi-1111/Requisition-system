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