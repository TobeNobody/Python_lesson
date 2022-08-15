
def questionnaire(name, surname, year, town, email, telephone):
    print(f"""Здравствуйте {name} {surname}!\nГод вашего рождения {year}\nВы проживаете в городе {town}
Электронная почта {email}\nНомер телефона {telephone}""")

questionnaire(input("Введите ваше имя: "), input("Введите вашу фамилию: "), input("Введите ваш год рождения: "),
               input("Введите ваш город: "), input("Введите ваш электронный адрес: "), input("Введите ваш телефон: "))
