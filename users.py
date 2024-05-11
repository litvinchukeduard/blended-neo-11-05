from datetime import datetime
# User (name, last_name, age)
# User('Ihor', 'Last name', '2000-01-01')

def calculate_age(date: str) -> int:
    today = datetime.today().date()
    birthday_date = datetime.strptime(date, '%Y-%m-%d').date()
    has_birthday_not_passed = (birthday_date.month, birthday_date.day) > (today.month, today.day)
    # if has_birthday_passed:
    #     return today.year - birthday_date.year 
    # else:
    #     return today.year - birthday_date.year - 1
    return today.year - birthday_date.year - int(has_birthday_not_passed)


class User:
    def __init__(self, name: str, last_name: str, birthday_date: str ) -> None:
        self.name = name
        self.last_name = last_name
        self.age = calculate_age(birthday_date)

    def print_info(self):
        print(f'{self.name} {self.last_name} {self.age}')

    # def __lt__(self, other):
    #     return self.age < other.age

    def __str__(self):
        return f'User: {self.name} {self.last_name} {self.age}'
    
    def __repr__(self):
        # return self.__str__()
        return str(self)

    
# print(calculate_age('2000-05-10'))

ihor = User('Ihor', 'LastName', '2000-05-10')
# print(ihor.age)
ihor.age = 25
# print(ihor.age)

john = User('John', 'Smith', '2013-04-05')
# print(john.age)
# print(ihor.age)
# print(john)

# john.print_info()
# User.print_info(john)

olga = User('Olga', 'Smith', '1994-05-18')

users = [ihor, john, olga]
print(users)

def get_user_age(user):
    return user.age

# print(sorted(users, key=lambda user: user.age))
# users.sort()
print(sorted(users, key=get_user_age))

