revenue = int(input('Ведите вашу выручку: '))
costs = int(input('Ведите вашу издержку: '))
profit = revenue - costs
employees = int(input('Ведите колличество сотрудников: '))
profit_employees = profit / employees
print("Прибыль фирмы на одного сотрудника ", profit_employees)