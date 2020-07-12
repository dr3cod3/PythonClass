#!/usr/bin/env python3
import sys
sys.path.append("./hr.py")
import hr
import employees

salary_employee = employees.SalaryEmployee(1, "John Smith", 1500) 
hourly_employee = employees.HourlyEmployee(2, "Jane Doe", 40, 15)
commission_employee = employees.CommissionEmployee(3, "Kevin Smith", 1000, 250)


payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
salary_employee,
hourly_employee,
commission_employee
])
