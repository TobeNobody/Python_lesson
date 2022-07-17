revenue = int(input('Ведите вашу выручку: '))
costs = int(input('Ведите ваши издержки: '))
profit = revenue - costs
lesion = costs - revenue

if revenue > costs:
    print('Ваше дело прибыльное! Прибыль составила ', profit )

elif revenue == costs:
    print('Вы работаете в 0!')

else:
    print('Вам нужно подыскать другое занятие, убыток составил ', lesion)

if revenue > costs:
    employees = int(input('Ведите колличество сотрудников: '))
    profit_employees = profit / employees
    print("Прибыль фирмы на одного сотрудника ", profit_employees)

else:
    print("Ваши сотрудники ничего не зарабатывают")

