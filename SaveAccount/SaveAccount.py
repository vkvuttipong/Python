class SavingAccount:
  def __init__(self, balance):
    self.balance = balance
  
  def withdraw(self, amount):
    self.balance -= amount
  
  def deposit(self, amount):
    self.balance += amount

acc = SavingAccount(500)
acc.deposit(100) # ฝากเพิ่ม 100

print(acc.balance) # 600