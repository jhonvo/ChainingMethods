from users import User

Michael = User("Michael Jordan")
Benny = User("Benny Bob")
Chris = User("Chris Patt")

Michael.deposit(1000.00).deposit(500.00).withdraw(300.00).display_user_balance()

Benny.deposit(1000.00).deposit(500.00).withdraw(200.00).withdraw(200.00).display_user_balance()

Chris.deposit(1000.00).withdraw(500.00).withdraw(300.00).display_user_balance()

Michael.transfer(Chris,100.00)

