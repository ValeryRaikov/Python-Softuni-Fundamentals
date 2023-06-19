company_dict = {}

command = input()
while command != "End":
    company_name, employee_id = command.split(" -> ")
    
    if company_name not in company_dict:
        company_dict[company_name] = []
        
    if employee_id not in company_dict[company_name]:
        company_dict[company_name].append(employee_id)
    
    command = input()
    
for company in company_dict:
        print(f"{company}")
        for employee in company_dict[company]:
            print(f"-- {employee}")