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

def display_requisition(self):
        print("Date:", self.date.strftime("%d/%m/%Y"))
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        if self.total == int(self.total):
            print("Total: $" + str(int(self.total)))
        else:
            print("Total: $" + str(self.total))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)
        print()

def requisition_statistics(self, requisitions):
        total_submitted = len(requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for r in requisitions:
            if r.status == "Approved":
                approved = approved + 1
            elif r.status == "Pending":
                pending = pending + 1
            elif r.status == "Not approved":
                not_approved = not_approved + 1

        print("Statistics:")
        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:", total_submitted)
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", not_approved)

        return total_submitted, approved, pending, not_approved