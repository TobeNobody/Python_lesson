revenue = int(input('Ведите вашу выручку: '))
costs = int(input('Ведите вашу издержку: '))

if revenue > costs:
    print('Ваше дело прибыльное!')

elif revenue == costs:
    print('Вы работаете в 0!')

else:
    print('Вам нужно подыскать другое занятие')
