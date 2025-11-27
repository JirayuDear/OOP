class User:
    def __init__(self, citizen_id: str, name_surname: str):
        self.__citizen_id = citizen_id
        self.__name_surname = name_surname

    @property
    def citizen_id(self):
        return self.__citizen_id
    @property
    def name_surname(self):
        return self.__name_surname

class ATMCard:
    def __init__(self, card_number: str, pin_number: str, balance: int):
        self.__card_number = card_number
        self.__pin_number = pin_number
        self.__balance = balance

    @property
    def pin_number(self):
        return self.__pin_number
    @property
    def card_number(self):
        return self.__card_number
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        if isinstance(new_balance, int):
            self.__balance = new_balance

class Account:
    def __init__(self, account_number: str, user_owner: User):
        self.__account_number = account_number
        self.__user_owner = user_owner

        self.__atm_card = None
        self.__list_transaction = []
    
    def create_atm_card(self, atm_card):
        self.__atm_card = atm_card

    @property
    def atm_card(self):
        return self.__atm_card
    @property
    def account_number(self):
        return self.__account_number
    @property
    def user_owner(self):
        return self.__user_owner
    @property
    def list_transaction(self):
        return self.__list_transaction
    
    def add_transaction(self,transaction):
        if isinstance(transaction, Transaction):
            self.__list_transaction.append(transaction)


class ATMMachine:
    def __init__(self, machine_id: str, total_money: int, initial_amount: float = 1000000):
        self.__machine_id = machine_id
        self.__total_money = total_money
        self.__initial_amount = initial_amount

    @property
    def machine_id(self):
        return self.__machine_id
    @property
    def total_money(self):
        return self.__total_money

    def check_pin(self):
        pin = input("Enter your PIN: ")
        if pin != '1234':
            return "Invalid"
        else:
            return "success"

    def insert_atm_card(self, bank, atm_card):
        if isinstance(atm_card, ATMCard) and isinstance(bank, Bank):
            if self.check_pin() == 'success':  # เรียก check_pin ผ่าน self
                for account in bank.list_account:
                    if account.atm_card == atm_card:
                        return account
            else:
                print("Invalid PIN")
                return None

            
    def deposit(self, atm_machine, account, total: int):
        if isinstance(atm_machine, ATMMachine) and isinstance(account, Account) and total > 0:
            atm_card = account.atm_card
            atm_card.balance += total
            Transaction(account, 'D', total, atm_card.balance, atm_machine.machine_id)
            account.add_transaction(Transaction(account, 'D', total, atm_card.balance, atm_machine.machine_id))
            return "success"
        return "error"
    
    def withdraw(self, atm_machine, account, total: int):
        if isinstance(atm_machine, ATMMachine,) and isinstance(account, Account) and 0 < total:
            if atm_machine.total_money < total:
                return "Expected result: ATM has insufficient funds"
            atm_card = account.atm_card
            if total < atm_card.balance and total < 40000 :
                atm_card.balance -= total
                Transaction(account, 'W', total, atm_card.balance, atm_machine.machine_id)
                account.add_transaction(Transaction(account, 'W', total, atm_card.balance, atm_machine.machine_id))
                return "success"
            else:
                return "Exceeds daily withdrawal limit of 40,000 baht"
    

    def transfer(self, atm_machine, my_account, target_account, total: int):
        if isinstance(atm_machine, ATMMachine) and isinstance(my_account, Account) and isinstance(target_account, Account) and 0 < total:
            my_atm_card = my_account.atm_card
            target_atm_card = target_account.atm_card
            if total < my_atm_card.balance:
                my_atm_card.balance -= total
                target_atm_card.balance += total
                target_transaction = Transaction(target_account, 'TD', total, target_atm_card.balance, atm_machine.machine_id)
                my_transaction = Transaction(my_account, 'TW', total, my_atm_card.balance, atm_machine.machine_id)
                target_transaction.add_account_transfer(my_account)
                my_transaction.add_account_transfer(target_account)
                target_account.add_transaction(target_transaction)
                my_account.add_transaction(my_transaction)
                return "success"
        return "error"

class Bank:
    def __init__(self):
        self.__list_account = []
        self.__list_atm_card = []
        self.__list_atm_machine = []


    @property
    def list_account(self):
        return self.__list_account
    @property
    def list_atm_card(self):
        return self.__list_atm_card
    @property
    def list_atm_machine(self):
        return self.__list_atm_machine
    
    def get_atm(self, machine_id):  # เพิ่ม self
        for j in range(len(self.list_atm_machine)):
            if self.list_atm_machine[j].machine_id == machine_id:
                atm_machine_temp = self.list_atm_machine[j]
                return atm_machine_temp

    def add_list_account(self, account: Account):
        self.__list_account.append(account)
    def add_list_atm_card(self, atm_card: ATMCard):
        self.__list_atm_card.append(atm_card)
    def add_list_atm_machine(self, atm_machine: ATMMachine):
        self.__list_atm_machine.append(atm_machine)
        
    # def find_account(card_number):
    #     if atm.card_number

class Transaction:
    def __init__(self, account, category: str, total: float, after_total: float, machine_id: str):
        self.__account = account
        self.__category = category
        self.__total = total
        self.__after_total = after_total
        self.__machine_id = machine_id
        self.__account_transfer = None

    @property
    def account(self):
        return self.__account
    @property
    def category(self):
        return self.__category
    @property
    def total(self):
        return self.__total
    @property
    def after_total(self):
        return self.__after_total
    @property
    def machine_id(self):
        return self.__machine_id
        
    def add_account_transfer(self, account_transfer):
        self.__account_transfer = account_transfer

    # def __str__(self) ปริ้นตาม format นี้เวลาเรียนปริ้น instance
    #     return f"{history.category}-ATM:{history.machine_id}-{history.total}-{history.after_total}

    def transcation_history(account):
        history_list = []
        for i in range(len(account.list_transaction)):
            history = account.list_transaction[i]
            history_list.append(f"{history.category}-ATM:{history.machine_id}-{history.total}-{history.after_total}")
        return history_list
        


##################################################################################

# กำหนดให้ ชื่อคลาส (Class Name) ต้องเป็น Pascal case เช่น BankAccount
# กำหนดให้ ชื่อ instance และ variables ใดๆ ต้องเป็น snake case เช่น my_book
# กำหนดให้ เมื่อรับพารามิเตอร์เข้าใน method ต้องทำ validate data type และกรอบของค่า parameter ก่อนใช้เสมอ
# กำหนดให้ method ที่จัดการข้อมูลใด ต้องอยู่ในคลาสนั้น และพยายามอย่า access attribute นอกคลาส

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM , จำนวนเงิน]}
user ={'1-1101-12345-45-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-46-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}

list_key_user = [i for i in user.keys()]
list_key_atm = [i for i in atm.keys()]

# harry = User(list_key_user[0], user[list_key_user[0]][0])
# harry_atm_card = ATMCard(user[list_key_user[0]][2], '1234', user[list_key_user[0]][3])
# harr_account = Account(user[list_key_user[0]][1], User, ATMCard)

# hermione = User(list_key_user[10], user[list_key_user[1]][0])
# hermione_atm_card = ATMCard(user[list_key_user[1]][2], '1234', user[list_key_user[1]][3])
# hermione_account = Account(user[list_key_user[1]][1], User, ATMCard)
bank = Bank()
for i in range(len(list_key_user)):
    if isinstance(list_key_user[i], str) and isinstance(user[list_key_user[i]][0], str):
        user_temp = User(list_key_user[i], user[list_key_user[i]][0])
    if isinstance(user[list_key_user[i]][2], str) and isinstance(user[list_key_user[i]][3], int):
        atmcard_temp = ATMCard(user[list_key_user[i]][2], '1234', user[list_key_user[i]][3])
        bank.add_list_atm_card(atmcard_temp)
    if isinstance(user[list_key_user[i]][1], str):
        account_temp = Account(user[list_key_user[i]][1], user_temp)
        account_temp.create_atm_card(atmcard_temp)
        bank.add_list_account(account_temp)

        
for i in range(len(list_key_atm)):
    if isinstance(list_key_atm[i], str) and isinstance(atm[list_key_atm[i]], int):
        atmmachine_temp = ATMMachine(list_key_atm[i], atm[list_key_atm[i]])
        bank.add_list_atm_machine(atmmachine_temp)

# TODO 1 : จากข้อมูลใน user ให้สร้าง instance ของผู้ใช้ โดยมีข้อมูล
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง
# TODO :   ต้อง validate ข้อมุลทุกอย่าง ก่อนสร้าง instance ใดๆ


# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 2 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card
# TODO     return ถ้าบัตรถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM


# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 3 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 4 ตัว คือ 1) instance ของเครื่อง atm
# TODO     2) instance ของ account ตนเอง 3) instance ของ account ที่โอนไป 4) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่ม

# Test case #1 : ทดสอบ การ insert บัตร โดยค้นหาเครื่อง atm เครื่องที่ 1 และบัตร atm ของ harry
# และเรียกใช้ function หรือ method จากเครื่อง ATM
# ผลที่คาดหวัง : พิมพ์ หมายเลข account ของ harry อย่างถูกต้อง และ พิมพ์หมายเลขบัตร ATM อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print('---------------------------------------')
atm_machine_temp = bank.get_atm('1001')
for i in range(len(bank.list_atm_card)):
    atm_card_temp = bank.list_atm_card[i]
    if atm_card_temp.card_number == '12345':
        result = atm_machine_temp.insert_atm_card(bank, atm_card_temp)
        print(f"{result.atm_card.card_number}, {result.account_number}, Success")

print('---------------------------------------')

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
atm_machine_temp = bank.get_atm('1002')
for i in range(len(bank.list_atm_card)):
    atm_card_temp = bank.list_atm_card[i]
    if atm_card_temp.card_number == '12346':
        after_money = atm_card_temp.balance
        account_temp = atm_machine_temp.insert_atm_card(bank, atm_card_temp)
        result = atm_machine_temp.deposit(atm_machine_temp, account_temp, 1000)
if result == 'success':
    print(f"{account_temp.user_owner.name_surname} account before test : {after_money}")
    print(f"{account_temp.user_owner.name_surname} account after test : {atm_card_temp.balance}")          
else:
    print('error')

print('---------------------------------------')

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
atm_machine_temp = bank.get_atm('1002')
for i in range(len(bank.list_atm_card)):
    atm_card_temp = bank.list_atm_card[i]
    if atm_card_temp.card_number == '12346':
        after_money = atm_card_temp.balance
        account_temp = atm_machine_temp.insert_atm_card(bank, atm_card_temp)
        result = atm_machine_temp.deposit(atm_machine_temp, account_temp, -1)
if result == 'success':
    print(f"{account_temp.user_owner.name_surname} account before test : {after_money}")
    print(f"{account_temp.user_owner.name_surname} account after test : {atm_card_temp.balance}")          
else:
    print('Error')
    
print('---------------------------------------')

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
atm_machine_temp = bank.get_atm('1002')
for i in range(len(bank.list_atm_card)):
    atm_card_temp = bank.list_atm_card[i]
    if atm_card_temp.card_number == '12346':
        after_money = atm_card_temp.balance
        account_temp = atm_machine_temp.insert_atm_card(bank, atm_card_temp)
        result = atm_machine_temp.withdraw(atm_machine_temp, account_temp, 500)
if result == 'success':
    print(f"{account_temp.user_owner.name_surname} account before test : {after_money}")
    print(f"{account_temp.user_owner.name_surname} account after test : {atm_card_temp.balance}")          
else:
    print('Error')
    
print('---------------------------------------')

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
atm_machine_temp = bank.get_atm('1002')
for i in range(len(bank.list_atm_card)):
    atm_card_temp = bank.list_atm_card[i]
    if atm_card_temp.card_number == '12346':
        after_money = atm_card_temp.balance
        account_temp = atm_machine_temp.insert_atm_card(bank, atm_card_temp)
        result = atm_machine_temp.withdraw(atm_machine_temp, account_temp, 2000)
if result == 'success':
    print(f"{account_temp.user_owner.name_surname} account before test : {after_money}")
    print(f"{account_temp.user_owner.name_surname} account after test : {atm_card_temp.balance}")          
else:
    print('Error')
    
print('---------------------------------------')


# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
atm_machine_temp = bank.get_atm('1002')
for i in range(len(bank.list_account)):
    if bank.list_account[i].account_number == '0987654321':
        target_account_temp = bank.list_account[i]
        break
for i in range(len(bank.list_atm_card)):
    atm_card_temp = bank.list_atm_card[i]
    if atm_card_temp.card_number == '12345':
        my_atm_card_temp = atm_card_temp
        my_after_money = my_atm_card_temp.balance
        target_after_money = target_account_temp.atm_card.balance
        my_account_temp = atm_machine_temp.insert_atm_card(bank, my_atm_card_temp)
        result = atm_machine_temp.transfer(atm_machine_temp, my_account_temp,target_account_temp, 10000)
        break

if result == 'success':
    print(f"{my_account_temp.user_owner.name_surname} account before test : {my_after_money}")
    print(f"{my_account_temp.user_owner.name_surname} account after test : {my_atm_card_temp.balance}")     
    print(f"{target_account_temp.user_owner.name_surname} account before test : {target_after_money}")
    print(f"{target_account_temp.user_owner.name_surname} account after test : {target_account_temp.atm_card.balance}")      
else:
    print('Error')
    
print('---------------------------------------')


# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : TD-ATM:1002-10000-11500
for i in range(len(bank.list_atm_card)):
    atm_card_temp = bank.list_atm_card[i]
    if atm_card_temp.card_number == '12346':
        account_temp = atm_machine_temp.insert_atm_card(bank, atm_card_temp)
        result = Transaction.transcation_history(account_temp)
        for i in range(len(result)):
            print(result[i])
    
print('---------------------------------------')

# Test case #8 : ทดสอบการใส่ PIN ไม่ถูกต้อง 
# ให้เรียกใช้ method ที่ทำการ insert card และตรวจสอบ PIN
atm_machine = bank.get_atm('1001')
test_result = atm_machine.insert_atm_card(bank, atm_card_temp)  # ใส่ PIN ผิด
# ผลที่คาดหวัง
# Invalid PIN

print('---------------------------------------')

# Test case #9 : ทดสอบการถอนเงินเกินวงเงินต่อวัน (40,000 บาท)
atm_machine = bank.get_atm('1001')
for i in range(len(bank.list_atm_card)):
    atm_card_temp = bank.list_atm_card[i]
    if atm_card_temp.card_number == '12345':
        account = atm_machine.insert_atm_card(bank, atm_card_temp)  # PIN ถูกต้อง
        harry_balance_before = account.atm_card.balance


print(f"Harry account before test: {harry_balance_before}")
print("Attempting to withdraw 45,000 baht...")
result = atm_machine.withdraw(atm_machine, account, 45000)
print(f"Expected result: Exceeds daily withdrawal limit of 40,000 baht")
print(f"Actual result: {result}")
print(f"Harry account after test: {account.atm_card.balance}")
print("-------------------------")

# Test case #10 : ทดสอบการถอนเงินเมื่อเงินในตู้ ATM ไม่พอ
atm_machine = bank.get_atm('1002')  # สมมติว่าตู้ที่ 2 มีเงินเหลือ 200,000 บาท
account = atm_machine.insert_atm_card(bank, atm_card_temp)

print("Test case #10 : Test withdrawal when ATM has insufficient funds")
print(f"ATM machine balance before: {atm_machine.total_money}")
print("Attempting to withdraw 250,000 baht...")
result = atm_machine.withdraw(atm_machine, account, 250000)
print(f"Expected result: ATM has insufficient funds")
print(f"Actual result: {result}")
print(f"ATM machine balance after: {atm_machine.total_money}")
print("-------------------------")


