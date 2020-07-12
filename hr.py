#!/usr/bin/env python3
class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating payroll")
        print("=====================")
        for employee in employees:
            print(f"Payroll for {employee.id}-{employee.name}")
            print(f"-check Amount: {employee.calculate_payroll()}")
            print()



