from user import User

user_1 = User("Shantanu", "Laghate", 18)
user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.get_login_attempts()

user_1.increment_login_attempts()
user_1.get_login_attempts()

user_1.increment_login_attempts()
user_1.get_login_attempts()

user_1.increment_login_attempts()
user_1.get_login_attempts()

user_1.reset_login_attempts()
user_1.get_login_attempts()
