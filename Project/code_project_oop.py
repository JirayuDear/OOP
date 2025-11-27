class System:
    def __init__(self):
        self.__user_list = []
        self.__member_list = []
        self.__admin_list = []
        self.__court_list = []
        self.__court_booking_list = []
        self.__equipment_list = []
        self.__gift_list = []
        self.__coupon_list = []
        
    @property
    def get_member_list(self):
        return self.__member_list
    @property
    def get_court_list(self):
        return self.__court_list
    @property
    def get_coupon_list(self):
        return self.__coupon_list

    def search_court_by_sport():
        pass
    def search_court_by_court_name(self, court_name):
        for court in self.get_court_list:
            if court.get_court_name == court_name:
                return court
            else:
                return "Not Found"
    def search_coupon_by_coupon_id(self, coupon_id):
        for coupon in self.get_coupon_list:
            if coupon_id == coupon.get_coupon_id:   
                return coupon
            else:
                return "Not Found"
    def add_court_booking_list(self, court_booking):
        return self.__court_booking_list.append(court_booking)
    def add_court_list(self, court):
        return self.__court_list.append(court)
    def add_member_list(self, member):
        return self.__member_list.append(member)
    def available_date_time():
        pass
    def search_coupon_from_member():
        pass
    def search_account_by_id():
        pass
    def search_history_by_member():
        pass
    def search_profile_by_member():
        pass
    def search_court_booking_by_id():
        pass
    def payment_success():
        pass
    def add_member():
        pass
    def add_court():
        pass
    def booking_court():
        pass
    def get_user_info_by_account_id():
        pass
    def check_booking_status():
        pass
    def find_courtbooking_to_accept():
        pass
    def search_member_by_name():
        pass
    def search_member_by_account_id(self, account_id):
        for member in self.get_member_list:
            if member.get_account_id == account_id:
                return member
            

    def booking_confirmation(self, court_name):
        return court_name
                   
    def request_create_booking(self, court_name, date, time, receipt, account_id):
        member = self.search_member_by_account_id(account_id)
        court = self.search_court_by_court_name(court_name)
        court_booking = CourtBooking
        court_booking_temp = court_booking.create_booking(court, date, time, receipt, member)
        self.add_court_booking_list(court_booking)
        return self.booking_confirmation(court_name)

    def booking_form_data(self, court_name, date, time, total_price, coupon_id=None):
        if coupon_id != None:
            return [court_name, date, time, total_price, coupon_id]
        if coupon_id == None:
            return [court_name, date, time, total_price]
        
   
    def request_booking_form(self, court_name, date, time, member_id, coupon_id = None):
        court = self.search_court_by_court_name(court_name)
        price = court.get_court_price
        member = self.search_member_by_account_id(member_id)
        payment = Payment
        if coupon_id != None:
            coupon = self.search_coupon_by_coupon_id(coupon_id)
            coupon_discount = coupon.get_coupon_discount
            total_price = payment.calculate_price_with_coupon(price, coupon_discount)
            form = self.booking_form_data(court_name, date, time, total_price, coupon_id)
            return form
        else:
            total_price = payment.calculate_price(price)
            form = self.booking_form_data(court_name, date, time, total_price)
            return form
system = System()
# system.request_booking_form("สนามเทนนิสหญ้าแท้","23","120","0010")

    
            
class User:
    def __init__(self, name, surname, citizen_id,phone,birth_date,list_account):
        self.__name = name
        self.__surname = surname
        self.__citizen_id = citizen_id 
        self.__phone = phone
        self.__birth_date = birth_date
        self.__list_account = list_account
        
    def search_user_by_account_id():
        pass
    
    def get_user_info():
        pass

class Account(User):
    __account_id_counter = '00001'
    @classmethod
    def get_next_account_id(cls):
        return cls.__account_id_counter  

    @classmethod
    def increment_account_id(cls):
        next_id = str(int(cls.__account_id_counter) + 1).zfill(5)  # แปลงเป็น int + 1 แล้วแปลงกลับเป็น 5 หลัก
        cls.__account_id_counter = next_id 

    def __init__(self, name, surname, citizen_id, phone, birth_date, username, password,gmail):
        super().__init__(self, name, surname, citizen_id, phone, birth_date)
        self.__account_id = Account.get_next_account_id()
        self.__account_id = name
        self.__username = username
        self.__password = password
        self.__gmail = gmail

        Account.increment_account_id()

    @property
    def get_account_id(self):
        return self.__account_id
        
    def signup():
        pass
    
    def courtchecking():
        pass
    
    def login():
        pass
    
    def logout():
        pass
    
    def check_admin():
        pass

class Admin(Account):
    def __init__(self, name, surname, citizen_id, phone, birth_date, username, password, gmail, system):
        super().__init__(name, surname, citizen_id, phone, birth_date, username, password, gmail)
        self.__system = system
        
    def notification():
        pass
    def accept_reserve():
        pass
    def accept_cancel():
        pass
    def  book_court():
        pass
    def membership_management():
        pass
    def equipment_rental():
        pass
    def point_exchange():
        pass

class Member(Account):
    def __init__(self, account_id, name, surname, citizen_id, phone, birth_date, username, password, gmail, history, point, dmis_pay, coupon_list):
        super().__init__(account_id, name, surname, citizen_id, phone, birth_date, username, password, gmail)
        self.__history = history
        self.__point = point
        self.__dmis_pay = dmis_pay
        self.__coupon_list = coupon_list

    @property
    def get_account_id(self):
        return self.__account_id
    

    def book_court():
        pass
    def use_coupon():
        pass
    def cancel_booking():
        pass
    def view_profile():
        pass
    @property
    def view_history(self):
        return self.__history
    def use_points():
        pass
    def rent_equipments():
        pass
    def rental_payment():
        pass
    def add_member_points():
        pass
    def add_booking_history():
        pass
    def add_point():
        pass
    def get_coupon():
        pass

class CourtBooking:
    __court_booking_id_counter = 1
    @classmethod
    def get_next_booking_id(cls):
        return cls.__court_booking_id_counter  

    @classmethod
    def increment_booking_id(cls):
        cls.__court_booking_id_counter += 1 

    def __init__(self, court, date, time, member,receipt, status_booking_success=False):
        self.__booking_id = CourtBooking.get_next_booking_id()
        self.__court = court
        self.__date_of_booking = date
        self.__time = time
        self.__member = member
        self.__receipt = receipt

        CourtBooking.increment_booking_id()

    def select_time():
        pass
    def confirm_reserve():
        pass
    def confirm_cancel():
        pass
    def add_points():
        pass
    def change_status():
        pass
    def get_booking_status():
        pass
    def get_court_booking_id(self):
        return self.__booking_id
    def create_booking(court, date, time, receipt, member):
        court_booking = CourtBooking(court, date, time, receipt, member)
        return court_booking
        
class Court:    
    def __init__(self, court_name, court_id, court_sport_type,status,court_price, court_point):
        self.__court_name = court_name
        self.__court_id = court_id
        self.__court_sport_type = court_sport_type
        self.__status =  status
        self.__court_price = court_price
        self.__court_point = court_point

    @property
    def get_court_id(self):
        return self.__court_id
    @property
    def get_court_name(self):
        return self.__court_name
    @property
    def get_court_price(self):
        return self.__court_price

    def check_available():
        pass
    def change_status():
        pass
    def get_court_sport_type():
        pass
    def get_court_price_by_count_name():
        pass
    def get_court_info_by_court_name():
        pass


class Redeem:
    def __init__(self,name,point,amount ):
        self.__name = name
        self.__point = point
        self.__amount = amount

        
class Coupon:
    def __init__(self, coupon_id, list_of_code, coupon_discount, expire_date):
        self.__coupon_id = coupon_id
        self.__list_of_code = []
        self.__coupon_discount = coupon_discount
        self.__expire_date = expire_date

    @property
    def get_coupon_id(self):
        return self.__coupon_id
    @property
    def get_coupon_discount(self):
        return self.__coupon_discount

class Payment:
    def __init__(self, price):
        self.__payment_id = CourtBooking.get_next_booking_id()
        self.__total_price = price

    @staticmethod
    def calculate_price(court_price):
        return court_price
    @staticmethod
    def calculate_price_with_coupon(court_price, coupon_discount):
        discount = court_price * coupon_discount
        total_price = court_price - discount
        return total_price

class QRPayment(Payment):
    def __init__(self, total_price, reference_number):
        super().__init__(total_price)
        self.__reference_number = reference_number
        
    def check_reference_number():
        pass
    
class DMISPay(Payment):
    def __init__(self, total_price, reference_number, coin_balance, Member, pin):
        super().__init__(total_price)
        self.__reference_number = reference_number
        self.__coin_balance = coin_balance
        self.__member = Member
        self.__pin = pin 

class Equipment:
     def __init__(self,item_id, price,type,status):
        self.__item_id = item_id
        self.__price = price
        self.__type = type
        self.__status = status

     def change_status():
        pass

class EquipmentalRental:
    def __init__(self, list_of_equipment, date, time,member):
        self.__list_of_equipment = []
        self.__date = date
        self.__time = time
        self.__member = member
        
    def equip_availble():
        pass

class History:
    def __init__(self, CourtBooking, payment_type):
        self.__court_booking = CourtBooking
        self.__payment = payment_type
        
    def add_history():
        pass
    def cancle_reservation():
        pass
    
class Notification:
    def __init__(self, court, date,payment,sport_type,member):
        self.__court = court
        self.__date = date
        self.__payment = payment
        self.__member = member

system.add_court_list(Court('สนามเทนนิสหญ้าแท้',       101, "เทนนิส", True,     180, 50))

system.add_court_list(Court('สนามเทนนิสผิวตอนกรีต',  102, "เทนนิส", True,     180, 50))
system.add_court_list(Court('สนามเทนนิสมะตอย',     103,   "เทนนิส", True,   180, 50))
system.add_court_list(Court('สนามเทนนิสหญ้าเทียม',   104, "เทนนิส", True,     180, 50))

system.add_court_list(Court('สนามฟุตบอลหญ้าแท้',   201, "ฟุตบอล", True,     750 , 300))
system.add_court_list(Court('สนามฟุตบอลหญ้าเทียม',   202, "ฟุตบอล", True,     500, 200))

system.add_court_list(Court('โต๊ะ 1',   301, "ปิงปอง", True,     100, 30))
system.add_court_list(Court('โต๊ะ 2',   302, "ปิงปอง", True,     100, 30))
system.add_court_list(Court('โต๊ะ 3',   303, "ปิงปอง", True,     100, 30))
system.add_court_list(Court('โต๊ะ 4',   304, "ปิงปอง", True,     100, 30))

system.add_member_list(Member('Jirayu พุ่มศิริ', 'Dear' ))

# from fasthtml.common import *

# app, rt = fast_app()
# @rt("/")
# def get():
#     return Container(
#         # Navbar
#         Div(
#             H1("DMIS COURT"),
#             Div(
#                 A("HOME", href="/"),
#                 cls="navbar-links"
#             ),
#             cls="navbar"),
#         H1("Contact Form"),
#         Form(
#             Label("เลือกสนาม:", Select(
#                     Option("สนาม A", value="A"),
#                     Option("สนาม B", value="B"),
#                     Option("สนาม C", value="C"),
#                     id="choose_court_name")),
#             Label("เลือกวันที่:", Input(type="date", id="choose_date", value="2025-02-18")),
#             Label("เลือกเวลา:", Input(type="time", id="choose_time", value="12:00")),
           
            
#             Button("ต่อไป", type="submit"),
#             # method="post",
#             action="/submit"
        
#     )
#     # Footer
#         Div(
#             A("contact us", href="/contact"),
#             cls="footer"
#         ),
#     )

# serve(port=5002)

# @rt("/submit")
# def get():
#     return Container(
#         H1("ยืนยันการจอง"),
#         H4("สนามที่เลือก")


#     )
    