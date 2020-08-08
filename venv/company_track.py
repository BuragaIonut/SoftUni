companies = {}

while True:
    employee = input().split(' -> ')
    if employee == 'End':
        break
    company = employee[0]
    companies[company] = id
print(companies)