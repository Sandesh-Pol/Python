# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 20:25:26 2023

@author: STORMSOFT2
"""

import openpyxl

# Create a new Excel workbook and select the active sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Insert header into cells
header = ["Sr. No.", "Test Case ID", "Test Case Objective", "Pre-Condition",
          "Steps", "Input Data", "Expected Result", "Actual Result", "Pass / Fail"]
sheet.append(header)

# Test case data
test_cases = [
    [1, "TC_1", "To check Internet", "Check whether Internet is Available or Not",
     "Test Internet connection", "www.flipkart.com",
     "Site homepage should display on screen", "Home page displayed", "Pass"],
    # ... add more test cases as needed
]

# Insert test case data into cells
for row in test_cases:
    sheet.append(row)

# Save the workbook
wb.save("test_cases.xlsx")
