#تعريف كلاس حساب البنك بدون فائدة
class BankAccount:
    def __init__(self, account_number, account_holder):
        # رقم الحساب البنكي
        self.account_number = account_number
        # اسم صاحب الحساب
        self.account_holder = account_holder
        # الرصيد الافتراضي حسب نص الوظيفة
        self.balance = 0.0

        # تابع زيادة الرصيد بقيمة المبلغ المودع
    def deposit(self, amount):
        self.balance += amount
        # تابع خصم المبلغ المسحوب من الرصيد
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("حدث خطأ يرجى المحاولة لاحقاً")

    # تابع لمعرفة الرصيد
    def get_balance(self):
        return self.balance

#تعريف كلاس حساب البنك مع فائدة
    #الكلاس يرث الكلاس الابBankAccount
class SavingsAccount(BankAccount):
    #الانتقال الى التابع الباني للاب
    def __init__(self, account_number, account_holder, interest_rate):
        super().__init__(account_number, account_holder)
        self.interest_rate = interest_rate  # نسبة الفائدة

    # تابع لحساب المبلغ المستحق كفائدة بناءً على نسبة الفائدة
    def apply_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest  # زيادة الرصيد بقيمة المبلغ المستحق كفائدة
# override للتابع print
    def __str__(self):
        p="الرصيد الحالي: "+str(self.balance)+"نسبة الفائدة: "+str(self.interest_rate)
        return p


# اشتقاق غرض
bank = BankAccount("2971", "لين شناني")
# إيداع 1000 دولار
bank.deposit(1000)
print("الرصيد الحالي:", bank.get_balance())
# سحب 500 دولار
bank.withdraw(500)
print("الرصيد الحالي:", bank.get_balance())
savings= SavingsAccount("2222", "احمد محمد", 5)
# إيداع 10000 دولار
savings.deposit(10000)
print(savings)
# تطبيق الفائدة
savings.apply_interest()
print(savings)
