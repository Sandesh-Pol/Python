import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active

num_rows = int(input("Enter the number of data rows: "))

data = []
a = 0
for _ in range(num_rows):
    a = a + 1
    srNo = a
    
    ID = input("Text case ID : ")
    
    pre = input("Enter Pre-Condition : ")
    
    steps = input("Enter Steps : ")
    
    inputData = input("Enter input data : ")
    
    expected = input("Enter Expected result : ")
    
    actual = input("Enter Actual result : ")
    
    result = input("Enter Pass/Fail result : ")
    
    
    data.append([srNo, ID, pre, steps, inputData, expected, actual, result ])

header = ["Name", "Age", "Country"]
sheet.append(header)

for row in data:
    sheet.append(row)

wb.save("data.xlsx")












