class User:
    count = 0
    
    def __init__(self, name, login, password, grade):
        if not isinstance(grade, int) or grade <= 0:
            raise ValueError("Grade должен быть положительным целым числом > 0")
        
        self._name = name
        self._login = login
        self._password = password
        self._grade = grade
        
        User.count += 1
    
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, value):
        print("Невозможно изменить логин!")
    
    
    @property
    def password(self):
        return "********"
    
    @password.setter
    def password(self, value):
        self._password = value
    
    
    @property
    def grade(self):
        return "Неизвестное свойство grade"
    
    @grade.setter
    def grade(self, value):
        print("Неизвестное свойство grade")
    
    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}")
    
    
    def __lt__(self, other):
        return self._grade < other._grade
    
    def __gt__(self, other):
        return self._grade > other._grade
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self._grade == other._grade


class SuperUser(User):
    count = 0
    
    def __init__(self, name, login, password, role, grade):
        super().__init__(name, login, password, grade)
        self._role = role
        SuperUser.count += 1
    
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        self._role = value
    
    def show_info(self):
        print(f"Name: {self.name}, Login: {self.login}, Role: {self.role}")




user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)

admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

print("=== show_info ===")
user1.show_info()
admin.show_info()

print("\n=== Счётчики ===")
users = User.count
admins = SuperUser.count
print(f"Всего обычных пользователей: {users}")
print(f"Всего супер-пользователей: {admins}")

print("\n=== Сравнения ===")
print(user1 < user2)
print(admin > user3)
print(user1 == user3)

print("\n=== Проверка доступа ===")
user3.name = 'Ringo Starr'
user1.password = 'Pa$$word'

print(user3.name)
print(user1.password)
print(user2.login)

user2.login = 'geo'           
print(user1.grade)
admin.grade = 10