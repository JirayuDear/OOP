from fasthtml.common import *
from fasthtml import *
from fastapi import Request
import datetime
import os
from datetime import timedelta
from datetime import date
from fastapi.responses import HTMLResponse

class System:
    def __init__(self):
        self.__user_list = []
        self.__member_list = []
        self.__admin_list = []
        self.__court_list = []
        self.__courtbooking_list = []
        self.__table_tennis_equipment = []
        self.__tennis_equipment = []
        self.__football_equipment = []
        self.__gift_list = []
        self.__coupon_list = []
        self.__equipment_rental = []
        self.__equipment_list = []
        self.__history = []
        self.__payment_list = []
        self.__request_cancel_list = []
        self.__choosing_list = []
        
    @property
    def get_payment_list(self):
        return self.__payment_list
    @property
    def get_court_booking_list(self):
        return self.__courtbooking_list
    @property
    def get_admin_list(self):
        return self.__admin_list
    @property
    def get_member_list(self):
        return self.__member_list
    @property
    def get_court_list(self):
        return self.__court_list
    @property
    def get_coupon_list(self):
        return self.__coupon_list
    @property
    def get_gift_list(self):
        return self.__gift_list
    @property
    def get_equipment_list(self):
        return self.__equipment_list
    @property
    def get_equipment_rental(self):
        return self.__equipment_rental
    
    def add_member_list(self, member):
        if isinstance(member, Member):
            self.__member_list.append(member)
            return "Success"
        return "Error: "
    
    def add_court_booking_list(self, courtbooking):
        if isinstance(courtbooking, CourtBooking):
            self.__courtbooking_list.append(courtbooking)
            return "Success"
        return "Error: "
    
    def add_court_list(self, court):
        if isinstance(court, Court):
            self.__court_list.append(court)
            return "Success"
        return "Error: "
    
    def add_history(self, history):
        if isinstance(history, History):
            self.__history.append(history)
            return "Success"
        return "Error: "
    
    def add_user_list(self, user): 
        return self.__user_list.append(user)
    
    def add_gift_list(self, redeem):
        return self.__gift_list.append(redeem)
    
    def add_payment_list(self, payment):
        return self.__payment_list.append(payment)
    
    def add_equipment_rental(self, equipment_rental):
        return self.__equipment_rental.append(equipment_rental)
    
    @property
    def _list_list(self):
        return self.__member_list
    
    def validate_data_signup(self, form_data):
        if len(form_data.get('username')) < 3:
            return "Username must be at least 3 characters long"
        for member in self.get_member_list:
            if member.get_username == form_data.get('username'):
                return "This Username is already in use."
        if len(form_data.get('password')) < 8:
            return "Password must be at least 8 characters long"
        if not form_data.get('password'):
            return "Password is required."
        if form_data.get('password') != form_data.get('confirm_password'):
            return "Passwords do not match."
        if not form_data.get('first_name'):
            return "First name is required."
        if not form_data.get('last_name'):
            return "Last name is required."
        if not form_data.get('citizen_id'):
            return "Citizen ID is required."
        elif not form_data['citizen_id'].isdigit():
            return "Citizen ID must contain only digits."
        if not form_data.get('phone'):
            return "Phone number is required."
        if len(form_data.get('phone')) < 10:
            return "Phone number must be exactly 10 digits long."
        elif not form_data['phone'].isdigit():
            return "Phone number must contain only digits."
        for member in self.get_member_list:
            if member.get_gmail == form_data.get('gmail'):
                return "This Gmail is already in use."
        # คุณสามารถเพิ่มการตรวจสอบเพิ่มเติมได้ เช่น การตรวจสอบรูปแบบอีเมล
        return True  # คืนค่า True ถ้าผ่านการตรวจสอบทั้งหมด
    
    def create_user_member(self, name, surname, citizen_id, phone, gender, birth_date, username, password, gmail):
        if name != None and surname != None and citizen_id != None and phone != None and gender != None and birth_date != None and username != None and password != None and gmail != None:
            user = User(name, surname, citizen_id, phone, gender, birth_date)
            self.add_user_list(user)
            member = Member(username, password, gmail, user)
            self.add_member_list(member)
            return "Success"
        else:
            return "Error"

    def check_login(self, username, password):
        for member in self.get_member_list:
            if member.get_username == username:
                if member.get_password == password:
                    return True
                return "Password not correct"  
        return "Username not found"  
    
    def check_admin_login(self, username, password):
        for admin in self.get_admin_list:
            if admin.get_username == username:
                if admin.get_password == password:
                    return True
                return "Password not correct"  
        return "Username not found"
    
    def get_unaccept_reserve(self):
        list_info = []
        for courtbooking_instance in self.__courtbooking_list:
            if courtbooking_instance.booking_status == "รอยืนยันการจอง":
                list_info.append([courtbooking_instance.booker.get_user.name, courtbooking_instance.court.court_name, courtbooking_instance.date_of_booking,
                                  courtbooking_instance.time, courtbooking_instance.receipt, courtbooking_instance.booking_status, courtbooking_instance.total_price])
        return list_info 
    
    
    def add_booking_history(self, name, history, point):
        for member_instance in self.__member_list:
            if member_instance.get_name == name:
                self.add_history(history)
                self.add_choosing_list(history)
                result1 = member_instance.add_booking_history(history)
                if result1 == "Success":
                    result2 = member_instance.add_point(point)
                    if result2 != "Success":
                        return result2
                else:
                    return result1
                return "Add point and history success"

    def find_courtbooking_to_accept(self, name, court_name, date, time):
        booking = None
        for courtbooking_instance in self.__courtbooking_list:
            if(courtbooking_instance.booker.get_user.name == name and courtbooking_instance.court.court_name == court_name and 
               courtbooking_instance.date_of_booking == date and courtbooking_instance.time == time):
                result = courtbooking_instance.change_status_cancel("จองสำเร็จ")
                if result == "Success":
                    booking = courtbooking_instance
                    break
                else:
                    return result
        if booking == None:
            return "Error: Booking not found"
        history = History(booking, booking.receipt)
        error = self.add_booking_history(name, history, booking.court.point)
        return error if error != "Add point and history success" else "Accept reserve complete!!"
    
    def find_courtbooking_to_cancel(self, name, court_name, date, time):
        for courtbooking_instance in self.__courtbooking_list:
            if(courtbooking_instance.booker.get_user.name == name and courtbooking_instance.court.court_name == court_name and 
               courtbooking_instance.date_of_booking == date and courtbooking_instance.time == time):
                self.__courtbooking_list.remove(courtbooking_instance)
                return "Remove Success!"
        return "Error: cannot found this booking"
    
    def avaliable_date_time(self, sport_type):
        from datetime import date, timedelta, datetime
        from collections import defaultdict

        time_range = ["10:00-11:00", "11:00-12:00", "12:00-13:00",
                      "13:00-14:00", "14:00-15:00", "15:00-16:00", "16:00-17:00",
                      "17:00-18:00", "18:00-19:00", "19:00-20:00", "20:00-21:00"]

        available_date_time = defaultdict(list)
        not_available_court = set()
        court_list = self.search_court_by_sport(sport_type)

        if not court_list:
            return "Error: No courts available for this sport!"

        current_time = datetime.now()

        for courtbooking_instance in self.__courtbooking_list:
            if courtbooking_instance.court in court_list:
                days_diff = date.fromisoformat(courtbooking_instance.date_of_booking) - date.today()
                if timedelta(days=0) <= days_diff <= timedelta(days=30):
                    not_available_court.add((courtbooking_instance.court.court_name, courtbooking_instance.date_of_booking, courtbooking_instance.time))

        for court_instance in court_list:
            for i in range(31):
                booking_date = (date.today() + timedelta(days=i)).isoformat()
                booked_times = {time for court, date_, time in not_available_court
                                if court == court_instance.court_name and date_ == booking_date}
                for times in time_range:
                    start_time_str, end_time_str = times.split("-")
                    start_time = datetime.strptime(booking_date + " " + start_time_str, "%Y-%m-%d %H:%M")
                    end_time = datetime.strptime(booking_date + " " + end_time_str, "%Y-%m-%d %H:%M")

                    if start_time > current_time and times not in booked_times:
                        available_date_time[court_instance.court_name].append((booking_date, times))

        return dict(available_date_time)
        
    def request_create_booking(self, court_id, date, time, account_id, payment_receipt, total_price, coupon_id):
        court = self.search_court_by_court_id(court_id)
        member = self.search_member_by_account_id(account_id)
        total_price = int(float(total_price))

        if payment_receipt == "dmis_pay":
            if coupon_id != "":
                member.remove_coupon_from_member_list(coupon_id)
                system.remove_coupon_by_id(coupon_id)
                member.deduct_dmis_coins(total_price)
                self.create_booking(court, date, time, member, total_price, payment_receipt)
                return "Success dmis co"
            else:
                self.create_booking(court, date, time, member, total_price, payment_receipt)
                member.deduct_dmis_coins(total_price)
                return "Success dmis"
        else:
            if coupon_id != "":
                member.remove_coupon_from_member_list(coupon_id)
                system.remove_coupon_by_id(coupon_id)
                self.create_booking(court, date, time, member, total_price, payment_receipt)
                return "Success qr cp"
            else:
                self.create_booking(court, date, time, member, total_price, payment_receipt)
                return "Success qr "

    def create_booking(self, court, date, time, member, total_price, payment_receipt):
        court_booking = CourtBooking(court, date, time, member, payment_receipt, total_price)
        self.add_court_booking_list(court_booking)
        return print("create")
    
    def remove_coupon_by_id(self, coupon_id):
        for coupon in self.get_coupon_list:  
            if coupon.get_coupon_id == coupon_id:
                self.get_coupon_list.remove(coupon)  # ลบออกจากลิสต์
                del coupon  # ลบ instance ออกจากหน่วยความจำ
                return f"Coupon {coupon_id} has been removed."
        return "Coupon not found."
        

    
    def add_equipment_by_sport(self, equipment):
        if equipment.get_item_type == "ปิงปอง":
            self.__table_tennis_equipment.append(equipment)
            self.__equipment_list.append(equipment)  # เพิ่มอุปกรณ์ใน __equipment_list
            return "เพิ่มอุปกรณ์ปิงปองเรียบร้อย"
        elif equipment.get_item_type == "เทนนิส":
            self.__tennis_equipment.append(equipment)
            self.__equipment_list.append(equipment)  # เพิ่มอุปกรณ์ใน __equipment_list
            return "เพิ่มอุปกรณ์เทนนิสเรียบร้อย"
        elif equipment.get_item_type == "ฟุตบอล":
            self.__football_equipment.append(equipment)
            self.__equipment_list.append(equipment)  # เพิ่มอุปกรณ์ใน __equipment_list
            return "เพิ่มอุปกรณ์ฟุตบอลเรียบร้อย"
        else:
            return "ไม่มีกีฬาที่ใช้อุปกรณ์นี้"
        
    def get_equipment_by_sport(self, sport):
        if sport == "ปิงปอง":
            return self.__table_tennis_equipment
        elif sport == "เทนนิส":
            return self.__tennis_equipment
        elif sport == "ฟุตบอล":
            return self.__football_equipment
        else:
            return None
        
    def calculate_total_equipment_price(self, equipment_ids):
        total = 0
        for item_id in equipment_ids:
            equipment = self.search_equipment_by_id(item_id)
            if equipment:
                total += equipment.get_item_price
        return total
    def search_court_booking_by_payment(self, category):
            for payment in self.get_payment_list:
                if payment.get_payment_category == category:
                    return payment
            return "Not Found"
    def search_equipment_by_id(self, item_id):
        all_equipment = self.__table_tennis_equipment + self.__tennis_equipment + self.__football_equipment
        for equipment in all_equipment:
            if equipment.get_item_id == item_id:
                return equipment
        return None  # ถ้าไม่พบอุปกรณ์
    def search_court_booking_by_id(self, booking_id):
        for court_booking in self.get_court_booking_list:
            if booking_id == court_booking.get_court_booking_id():   
                return court_booking
        return "Not Found"
        
    def search_member_by_username(self, username):
        for member in self.get_member_list:
            if member.get_username == username:
                return member
    def search_member_by_account_id(self, account_id): ##########################
        for member in self.get_member_list:
            if member.get_account_id == account_id:
                return member
    def search_court_by_sport(self, sport_type):
        return [court for court in self.__court_list if court.get_court_sport_type == sport_type] or []
    
    def search_court_by_court_name(self, court_name):
        for court in self.get_court_list:
            if court.court_name == court_name:
                return court
        return "Not Found"
    def search_court_by_court_id(self, court_id):
        for court in self.get_court_list:
            if court.get_court_id == court_id:
                return court
        return "Not Found"
    def search_coupon_by_coupon_id(self, coupon_id): 
        for coupon in self.get_coupon_list:
            if coupon_id == coupon.get_coupon_id:   
                return coupon
        return "Not Found"
    def search_coupon_by_coupon_code(self, coupon_code):
        for coupon in self.get_coupon_list:
            if coupon_code == coupon.get_coupon_code:   
                return coupon
        return "Not Found"
    def search_equipment_by_id(self, item_id):
        for equipment in self.get_equipment_list:
            if equipment.get_item_id == item_id:
                return equipment
            
    def search_equipment_by_id_for_rent(self, item_id):#
        all_equipment = self.__table_tennis_equipment + self.__tennis_equipment + self.__football_equipment
        for equipment in all_equipment:
            if equipment.get_item_id == item_id:
                return equipment
        return None  # ถ้าไม่พบอุปกรณ์
    
    def search_history_by_username(self, username):
        history = []
        for member in self.__member_list:
            if member.get_username == username:
                for booking in member.view_history:
                    if booking.get_status_booking_success:
                        history.append(booking)
            
    def get_info_for_create_table(self, sport_type, date):
        already_accept = []
        not_accept = []
        court_list = self.search_court_by_sport(sport_type)
        court_name = []
        for c in court_list:
            court_name.append(c.court_name)
        for history in self.__history:
            print(str(history))
            for court in court_list:
                print(history.get_date)
                print(date)
                print(history.get_court)
                print(court)
                if history.get_date == date and history.get_court == court:
                    already_accept.append([history.get_court_name, history.get_time])
        for booking in self.__courtbooking_list:
            for court in court_list:
                if booking.date_of_booking == date and booking.booking_status == False and booking.court == court:
                    not_accept.append([booking.court.court_name, booking.time])
        return court_name, already_accept, not_accept
    
    def add_coupon_list(self, coupon): #
        return self.__coupon_list.append(coupon)
    
    def search_gift_by_name(self, gift_name):
        for gift in self.__gift_list:
            if gift.get_gift_name == gift_name:
                return gift
        return None
    
    def time_expire_five_minute(self):
        expire_time = datetime.datetime.now() + timedelta(minutes=5)
        expire_str = expire_time.strftime("%H:%M:%S") 
        return expire_str
    def generate_js_countdown(self, expire_minutes=5):
        # สร้าง JavaScript สำหรับการนับถอยหลัง
        js = f"""
        var expireTime = new Date(new Date().getTime() + {expire_minutes} * 60000);  // เพิ่ม {expire_minutes} นาที
        var countdownElement = document.getElementById("countdown");

        function updateCountdown() {{
            var now = new Date();
            var timeLeft = expireTime - now;
            if (timeLeft <= 0) {{
                window.location.href = '/';  // รีไดเรกต์ไปที่หน้า '/'
            }} else {{
                var minutes = Math.floor(timeLeft / 60000);
                var seconds = Math.floor((timeLeft % 60000) / 1000);
                countdownElement.innerHTML = "เวลาที่เหลือ: " + minutes + " นาที " + seconds + " วินาที";
            }}
        }}

        setInterval(updateCountdown, 1000);  // อัปเดตทุกวินาที
        updateCountdown();  // เรียกฟังก์ชันครั้งแรกทันที
        """
        return js
    def progress_bar(self):
        js = """
            htmx.on('#upload_form', 'htmx:xhr:progress', function(evt) {
                htmx.find('#progress').setAttribute('value', evt.detail.loaded/evt.detail.total * 100);
            });

            htmx.on('#upload_form', 'htmx:afterSwap', function(evt) {
                document.getElementById('confirm_button').disabled = false;
            });
            """
        return js
    def merch_js_qr(self):
        merch = self.generate_js_countdown() + self.progress_bar()
        return merch
    # def back_home_after_delay(self, expire_time=30):  # 30 วินาที
    #     js = f"""
    #     setTimeout(function() {{
    #         window.location.href = '/home';  // รีไดเรกต์ไปที่หน้า '/'
    #     }}, {expire_time} * 1000);  // แปลงวินาทีเป็นมิลลิวินาที
    #     """
    #     return js

    def request_cancel(self,court_booking):
        self.add_request_cancel_list(court_booking)
        return court_booking
    def add_request_cancel_list(self,court_booking):
        self.__request_cancel_list.append(court_booking)
        return court_booking
    
    def remove_request(self,court_booking):
        self.remove_request_cancel_list(court_booking)
        return court_booking
    def remove_request_cancel_list(self, court_booking):
        if court_booking in self.__request_cancel_list:
            self.__request_cancel_list.remove(court_booking)
            return court_booking
        else:
            return "Booking not found"

    @property
    def get_request_cancel_list(self):
        return self.__request_cancel_list
    
    def accept_cancel(self,court_booking):
        self.remove_choosing_list(court_booking)
        return court_booking
    
    def remove_choosing_list(self, court_booking):
        if court_booking in self.__choosing_list:
            self.__choosing_list.remove(court_booking)
            return court_booking
        else:
            return "Booking not found"
    
    def add_choosing_list(self, history):
        if history.get_datetime > datetime.datetime.now():  # ตรวจสอบว่าไม่ใช่อดีต
            self.__choosing_list.append(history)
            return "Success"
    
    @property
    def get_choosing_list(self):
        return self.__choosing_list

system = System()

class User:
    def __init__(self, name, surname, citizen_id, phone, gender, birth_date):
        self.__name = name
        self.__surname = surname
        self.__citizen_id = citizen_id
        self.__phone = phone
        self.__gender = gender
        self.__birth_date = birth_date
        #self.__account = []

    # def add_account(self, account): #****************************
    #     self.__list_account.append(account)
    
    @property
    def name(self):
        return self.__name
    @property
    def surname(self):
        return self.__surname
    @property
    def birth_date(self):
        return self.__birth_date
    @property
    def phone(self):
        return self.__phone
    @property
    def gender(self):
        return self.__gender
    
    def set_name(self, new_name):
        if new_name == "" or new_name == None:
            return self.__name
        else:
            self.__name = new_name
            return self.__name
        
    def set_surname(self, new_surname):
        if new_surname == "" or new_surname == None:
            return self.__surname
        else:
            return self.__surname
        
    def set_birth_date(self, new_birth_date):
        self.__birth_date = new_birth_date
        return self.__birth_date
    
    def set_gender(self, new_gender):
        if new_gender == "ชาย" or new_gender == "หญิง":
            self.__gender = new_gender
            return self.__gender
        else:
            return self.__gender
        
    def set_phone(self, new_phone):
        if len(new_phone) != 10 or new_phone[0] != "0" or new_phone == "" or new_phone == None:
            return self.__phone
        else:
            self.__phone = new_phone
            return self.__phone
    

    # def add_account(self, account):
    #     if isinstance(account, Account):
    #         self.__account.append(account)
    #         return "Success"
    #     return "Error: "
    
class Account:
    __account_id_counter = '00001'
    
    @classmethod
    def get_next_account_id(cls):
        return cls.__account_id_counter
    
    @classmethod 
    def increment_account_id(cls):
        next_id = str(int(cls.__account_id_counter) + 1).zfill(5)  # แปลงเป็น int + 1 แล้วแปลงกลับเป็น 5 หลัก
        cls.__account_id_counter = next_id
        
    # def __init__(self, account_id, username, password, gmail, owner: User):
    #     self.__account_id = account_id
    #     self.__username = username
    #     self.__password = password
    #     self.__gmail = gmail
    #     self.__owner = owner
    
    def __init__(self, username, password, gmail, owner): ##########################
        self.__account_id = Account.get_next_account_id()
        self.__username = username
        self.__password = password
        self.__gmail = gmail
        self.__owner = owner

        Account.increment_account_id()

    @property
    def get_account_id(self):
        return self.__account_id

    @property
    def get_user(self):
        return self.__owner
    
    @property
    def get_name(self):
        return self.__owner.name
    
    @property
    def get_surname(self):
        return self.__owner.surname
    
    @property
    def get_birthdate(self):
        return self.__owner.birth_date
    
    @property
    def get_gender(self):
        return self.__owner.gender
    
    @property
    def get_phone(self):
        return self.__owner.phone
    
    @property
    def get_username(self):
        return self.__username
    
    @property
    def get_password(self):
        return self.__password
    
    @property
    def get_gmail(self):
        return self.__gmail
    
    def set_name(self, new_name):
        return self.__owner.set_name(new_name)
    
    def set_surname(self, new_surname):
        return self.__owner.set_surname(new_surname)
    
    def set_birth_date(self, new_birth_date):
        return self.__owner.set_birth_date(new_birth_date)
    
    def set_gender(self, new_gender):
        return self.__owner.set_gender(new_gender)
    
    def set_gmail(self, new_gmail):
        if new_gmail == "" or new_gmail == None:
            return self.__gmail
        else:
            self.__gmail = new_gmail
            return self.__gmail
        
    def set_phone(self, new_phone):
        return self.__owner.set_phone(new_phone)

class Admin(Account):
    def __init__(self, username, password, gmail, owner, system):
        super().__init__(username, password, gmail, owner)
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
    
    def __init__(self, username, password, gmail, owner, points = 0, dimis_coins = 0): ############################
        super().__init__(username, password, gmail, owner)
        self.__history = []
        self.__point = points
        self.__dmis_coins = dimis_coins
        self.__member_coupon_list = []
        self.__received_coupons = {}
        
    @property
    def get_account_id(self):
        return super().get_account_id
    
    @property
    def view_history(self):
        return self.__history
    
    @property
    def get_username(self):
        return super().get_username
    
    @property
    def get_point(self):
        return self.__point
    # Setter สำหรับกำหนดค่าคะแนนโดยตรง
    def add_member_coupon_list(self, coupon):
        return self.__member_coupon_list.append(coupon)
    def search_member_coupon_by_coupon_id(self, coupon_id):
        for coupon in self.get_member_coupon_list:
            if coupon.get_coupon_id == coupon_id:
                return coupon
        return "Not Found"
    def remove_coupon_from_member_list(self, coupon_id):
        for coupon in self.get_member_coupon_list:
            if coupon.get_coupon_id == coupon_id:
                self.get_member_coupon_list.remove(coupon)
                return
        return 
    def set_point(self, new_point):
        self.__point = new_point
    
    #setter ของ point
    def update_point(self, point_added):
        self.__point = self.__point + point_added
        return self.__point
    def deduct_point(self, item_point):
        self.__point = self.__point - item_point
        return self.__point
    
    @property
    def get_member_coupon_list(self):
        return self.__member_coupon_list
    
    def add_member_coupon_list(self, coupon):
        return self.__member_coupon_list.append(coupon)

    @property
    def get_dmis_coin(self):
        return self.__dmis_coins
    # Setter สำหรับกำหนดค่าเหรียญโดยตรง
    def set_dmis_coin(self, new_dmis_coins):
        self.__dmis_coins = new_dmis_coins
    #setter ของ dmis_coins
    def add_dmis_coins(self, amount):
        if amount > 0:
            self.__dmis_coins += amount
            return
        else:
            raise ValueError("Amount must be positive")
    def deduct_dmis_coins(self, amount):
        if 0 < amount <= self.__dmis_coins:
            self.__dmis_coins -= amount
            return
        else:
            raise ValueError("Insufficient balance or invalid amount")
        
    def add_booking_history(self, history: "History"):
        if isinstance(history, History):
            self.__history.append(history)
            return "Success"
        return "Error: history must be instance of History"
    
    def add_point(self, point):
        if isinstance(point, int):
            self.__point += point
            return "Success"
        return "Error: point must be instance of Integer"
    
    @property
    def get_coupon_list(self):
        return self.__member_coupon_list
    
    def check_item_point(self, item_point):
        if self.__point >= item_point:
            self.deduct_point(item_point)
            return True
        return False
    
    def claim_coupon(self, coupon):
        today = date.today()
        if coupon.get_coupon_id in self.__received_coupons and self.__received_coupons[coupon.get_coupon_id] == today:
            return "Already claimed today"
        
        self.__member_coupon_list.append(coupon)
        self.__received_coupons[coupon.get_coupon_id] = today
        return "Coupon claimed successfully"

    def has_claimed_today(self, coupon_id):
        today = date.today()
        return self.__received_coupons.get(coupon_id) == today
    

class History:
    def __init__(self, finish_booking: "CourtBooking", payment_type):
        self.__finish_booking = finish_booking
        self.__payment_type = payment_type

    def __str__(self):
        return f"{self.__finish_booking.booker.get_username}-{self.__finish_booking.court.court_name}-{self.__finish_booking.date_of_booking}-{self.__finish_booking.time}-{self.__finish_booking.receipt}"

    @property
    def get_date(self):
        return self.__finish_booking.date_of_booking
    
    @property
    def get_court_name(self):
        return self.__finish_booking.court.court_name
    
    @property
    def get_time(self):
        return self.__finish_booking.time
    
    @property
    def get_court(self):
        return self.__finish_booking.court
    
    @property
    def get_court_sport_type(self):
        return self.__finish_booking.get_court_sport_type
    
    @property
    def get_court_booking_status(self):
        return self.__finish_booking.booking_status
    
    @property
    def get_account_id(self):
        return self.__finish_booking.get_account_id
    
    @property
    def get_datetime(self):
        return self.__finish_booking.get_datetime
    
    @property
    def get_court_booking_id(self):
        return self.__finish_booking.get_court_booking_id
    
    def change_status_cancel(self, new_status):
        return self.__finish_booking.change_status_cancel(new_status)
    @property
    def get_username(self):
        return self.__finish_booking.get_username
    @property
    def get_receipt(self):
        return self.__finish_booking.receipt
    
    @property
    def get_total_price(self):
        return self.__finish_booking.total_price
    
class Court:
    def __init__(self, court_name, court_id, court_sport_type, status,  price, point):
        self.__court_name = court_name
        self.__court_id = court_id
        self.__court_sport_type = court_sport_type
        self.__price = price
        self.__point = point 
        self.__status = status

    @property
    def get_court_id(self):
        return self.__court_id
    
    @property
    def court_name(self):
        return self.__court_name
    
    @property
    def get_court_price(self):
        return self.__price
    
    @property
    def point(self):
        return self.__point
    
    @property
    def get_court_sport_type(self):
        return self.__court_sport_type


class CourtBooking:
    __court_booking_id_counter = '000001'
    @classmethod
    def get_next_booking_id(cls):
        return cls.__court_booking_id_counter

    @classmethod
    def increment_booking_id(cls):
        next_id = str(int(cls.__court_booking_id_counter)+1).zfill(6)
        cls.__court_booking_id_counter = next_id
        
    def __init__(self, court: Court, date_of_booking, time, booker : Member, receipt, total_price, status = "รอยืนยันการจอง"):
        self.__booking_id = CourtBooking.get_next_booking_id()
        self.__court = court
        self.__date_of_booking = date_of_booking
        self.__booker = booker
        self.__receipt = receipt
        self.__status = status
        self.__time = time
        self.__total_price = total_price

        if receipt == 'dmis_pay':
            self.__payment = Payment(self.__booking_id, total_price, 'dmis_pay')
        else:
            self.__payment = Payment(self.__booking_id, total_price, 'qr_code')

        system.add_payment_list(self.__payment)

        CourtBooking.increment_booking_id()

    @property
    def total_price(self):
        return self.__total_price
    
    @property
    def booking_status(self):
        return self.__status
    
    @property
    def booker(self):
        return self.__booker
    
    @property
    def court(self):
        return self.__court
    
    @property
    def receipt(self):
        return self.__receipt
    
    @property
    def date_of_booking(self):
        return self.__date_of_booking
    
    @property
    def time(self):
        return self.__time
    
    # @property
    # def change_status(self):
    #     if(self.__status == False):
    #         self.__status = True
    #         return "Success"
    #     return "Error: This booking is already acccept!"
    
    def change_status_cancel(self, new_status):
        """ เปลี่ยนสถานะการจอง """
        valid_statuses = ["จองสำเร็จ", "ยกเลิกสำเร็จ", "รอยืนยันการจอง", "รอยืนยันการยกเลิก"]

        if new_status in valid_statuses:
            self.__status = new_status
            return "Success"
        else:
            raise ValueError(f"สถานะต้องเป็นค่าต่อไปนี้เท่านั้น: {valid_statuses}")
    
    def get_court_booking_id(self):
        return self.__booking_id
    
    @property
    def get_court_sport_type(self):
        return self.__court.get_court_sport_type
    
    @property
    def get_username(self):
        return self.__booker.get_username
    
    @property
    def get_account_id(self):
        return self.__booker.get_account_id
    
    # @property
    # def get_datetime(self):
    #     """รวม date และ time เป็น datetime object"""
    #     return datetime.datetime.strptime(f"{self.__date_of_booking} {self.__time}", "%Y-%m-%d %H:%M-%H:%M")

    @property
    def get_datetime(self):
        """รวม date และ time เป็น datetime object โดยใช้เวลาเริ่มต้น"""
        start_time = self.__time.split("-")[0]  # แยก "10:00" จาก "10:00-11:00"
        return datetime.datetime.strptime(f"{self.__date_of_booking} {start_time}", "%Y-%m-%d %H:%M")
     
class Redeem:
    def __init__(self, name, point, amount, image_url):
        self.__name = name
        self.__point = point
        self.__amount = amount
        self.__image_url = image_url

    @property
    def get_gift_name(self):
        return self.__name
    @property
    def get_gift_point(self):
        return self.__point
    @property
    def get_gift_amount(self):
        return self.__amount
    @property
    def get_gift_url(self):
        return self.__image_url
    def deduct_amount(self, deleted_amount=1):
        self.__amount = self.__amount - deleted_amount
        return self.__amount
    
class Coupon:
    __coupon_id_counter = '000001'
    @classmethod
    def get_next_coupon_id(cls):
        return cls.__coupon_id_counter  

    @classmethod
    def increment_coupon_id(cls):
        next_id = str(int(cls.__coupon_id_counter) + 1).zfill(5)  # แปลงเป็น int + 1 แล้วแปลงกลับเป็น 5 หลัก
        cls.__coupon_id_counter = next_id 

    def __init__(self, coupon_code, coupon_discount, expire_date):
        self.__coupon_id = Coupon.get_next_coupon_id()
        self.__coupon_code = coupon_code
        self.__coupon_discount = coupon_discount
        self.__expire_date = expire_date

        Coupon.increment_coupon_id()

    @property
    def get_coupon_id(self):
        return self.__coupon_id
    @property
    def get_coupon_discount(self):
        return self.__coupon_discount
    @property
    def get_coupon_code(self):
        return self.__coupon_code
    @property
    def  get_expire_date(self):
        return self.__expire_date
    
class Payment:
    def __init__(self, booking_id, total_price, category):
        self.__payment_id = booking_id
        self.__total_price = total_price
        self.__category = category

    @staticmethod
    def calculate_price(court_price):
        return court_price
    @staticmethod
    def calculate_price_with_coupon(court_price, coupon_discount):
        discount = court_price * coupon_discount/100
        total_price = court_price - discount
        return total_price
    @staticmethod
    def calculate_price_dmis_coins(price, dmis_coins):
        if dmis_coins >= price:
            total_price = dmis_coins - price
            return f"{total_price} Coins"
        else:
            return "ยอด DMIS COINS คงเหลือของคุณไม่พอที่จะใช้บริการนี้"
    @staticmethod
    def check_coins_enough(dmis_coins, price):
        if dmis_coins > price:
            return False
        else: return True
    @property
    def get_payment_id(self):
        return self.__payment_id
    @property
    def get_payment_category(self):
        return self.__category
    

class Equipment:
    def __init__(self, item_id, name, price, type, image_url):
        self.__item_id = item_id
        self.__name = name
        self.__price = price
        self.__type = type
        self.__image_url = image_url

    @property
    def get_item_name(self):
        return self.__name
    @property
    def get_item_id(self):
        return self.__item_id
    @property
    def get_item_price(self):
        return self.__price
    @property
    def get_item_type(self):
        return self.__type
    @property
    def get_image_url(self):
        return self.__image_url
    # @property
    # def get_item_status(self):
    #     return self.__status
    # def change_status(self, new_status):
    #     self.__status = new_status
    #     return self.__status

class EquipmentRental:
    def __init__(self, equipment_list, date, time, renter):
        self.__equipment_list = equipment_list
        self.__date = date
        self.__time = time
        self.__renter = renter

    @property
    def get_renter(self):
        return self.__renter
        
    def equip_availble():
        pass
    
################################################################################################

tennisA = Court('สนามเทนนิสหญ้าแท้',       '101', "เทนนิส", True,     180, 50)
tennisB = Court('สนามเทนนิสผิวตอนกรีต',  '102', "เทนนิส", True,     180, 50)
tennisC = Court('สนามเทนนิสมะตอย',     '103',   "เทนนิส", True,   180, 50)
tennisD = Court('สนามเทนนิสหญ้าเทียม',   '104', "เทนนิส", True,     180, 50)

footballA = Court('สนามฟุตบอลหญ้าแท้',   '201', "ฟุตบอล", True,     750 , 300)
footballB = Court('สนามฟุตบอลหญ้าเทียม',   '202', "ฟุตบอล", True,     500, 200)

pA = Court('ปิงปองโต๊ะ 1',   '301', "ปิงปอง", True,     100, 30)
pB = Court('ปิงปองโต๊ะ 2',   '302', "ปิงปอง", True,     100, 30)
pC = Court('ปิงปองโต๊ะ 3',   '303', "ปิงปอง", True,     100, 30)
pD = Court('ปิงปองโต๊ะ 4',   '304', "ปิงปอง", True,     100, 30)


user_mock_1 = User('Jirayu', 'Phumsiri', '00000001', '0863521179', "ชาย", '2006-07-23')
system.add_user_list(user_mock_1)

user_mock_2 = User("John", "Doe", "12345678", "0812345678", "ชาย", "2000-01-01")
system.add_user_list(user_mock_2)

user_mock_3 = User("Jane", "Doe", "98765432", "0898765432", "หญิง", "1999-05-05")
system.add_user_list(user_mock_3)

userA = User("Sigma", "Lovely", "133264646464696", "0843486344", "ชาย", "2000-08-09")
system.add_user_list(userA)

userB = User("Cat", "San", "8888888888888", "0845444444", "หญิง", "2000-05-19")
system.add_user_list(userB)

memberdear = Member('Dear', '12345678', 'jirayuphumsiri@gmail.com', user_mock_1)
system.add_member_list(memberdear)
memberdear.add_dmis_coins(500)
system.add_member_list(Member("john_doe", "password123", "john@gmail.com", user_mock_2))
system.add_member_list(Member("jane_doe", "password456", "jane@gmail.com", user_mock_3))
memberA = Member("SigmaO_o", "1234", "fgdfgdaf@kiklsd.com", userA)
memberB = Member("Catt", "5555", "GG@kiklsd.com", userB)
system.add_member_list(memberA)
system.add_member_list(memberB)

# memberA = Member("123456789", "SigmaO_o", "1234", "fgdfgdaf@kiklsd.com", userA)
# memberB = Member("999999999", "Catt", "5555", "GG@kiklsd.com", userB)

# userA.add_account(memberA)
# userB.add_account(memberB)


system.add_coupon_list(Coupon('AAAA',5,datetime.datetime.now()+timedelta(days=10)))
system.add_coupon_list(Coupon('BBBB',10,datetime.datetime.now()+timedelta(days=7)))
system.add_coupon_list(Coupon('CCCC',15,datetime.datetime.now()+timedelta(days=5)))
system.add_coupon_list(Coupon('DDDD',20,datetime.datetime.now()+timedelta(days=3)))


#เพิ่มของแลก
system.add_gift_list(Redeem('น้ำดื่ม', 100, 150, 'https://www.evian.com/fileadmin/user_upload/gb/Products/Core_Range/Core_Range_-_EVIAN-500ML-BOTTLE.png'))
system.add_gift_list(Redeem('ผ้าเย็น', 200, 150,'https://bangpleestationery.com/wp-content/uploads/2019/11/6088002.png'))
system.add_gift_list(Redeem('แก้วเก็บความเย็น', 500, 150,'https://image.makewebcdn.com/makeweb/m_1920x0/YuMQ0nq3x/Products/Grey.jpg'))
system.add_gift_list(Redeem('เวย์โปรตีน', 1000, 150,'https://medias.watsons.co.th/publishing/WTCTH-BP_268327-front-zoom.jpg'))


jirayu = system.search_member_by_account_id('00001')
jirayu.add_member_coupon_list(system.search_coupon_by_coupon_code('AAAA'))
jirayu.add_member_coupon_list(system.search_coupon_by_coupon_code('AAAA'))
jirayu.add_member_coupon_list(system.search_coupon_by_coupon_code('BBBB'))
jirayu.add_member_coupon_list(system.search_coupon_by_coupon_code('CCCC'))
jirayu.add_member_coupon_list(system.search_coupon_by_coupon_code('DDDD'))


bookingA = CourtBooking( pA, "2025-03-11", "10:00-11:00", memberA, "receipt", 20)
bookingB = CourtBooking( tennisC, "2025-03-06", "15:00-16:00", memberB, "receipt", 30) 
bookingD = CourtBooking( tennisA, "2025-03-06", "15:00-16:00", memberB, "receipt", 40) 
bookingE = CourtBooking( tennisB, "2025-03-06", "15:00-16:00", memberB, "receipt", 50) 
bookingC = CourtBooking( footballB, "2025-04-15", "16:00-17:00", memberA, "receipt", 60)

system.add_court_booking_list(bookingA)
system.add_court_booking_list(bookingB)
system.add_court_booking_list(bookingC)
system.add_court_booking_list(bookingD)
system.add_court_booking_list(bookingE)
# system.add_member_list(memberA)
# system.add_member_list(memberB)
system.add_court_list(tennisA)
system.add_court_list(tennisB)
system.add_court_list(tennisC)
system.add_court_list(tennisD)
system.add_court_list(footballA)
system.add_court_list(footballB)
system.add_court_list(pA)
system.add_court_list(pB)
system.add_court_list(pC)
system.add_court_list(pD)

jirayu.add_booking_history(History(bookingA, "QRpayment"))
jirayu.add_booking_history(History(bookingB, "DMIS Coin"))

system.add_equipment_by_sport(Equipment('PP01','ไม้ปิงปอง(เดี่ยว)', 50, 'ปิงปอง', 'https://contents.mediadecathlon.com/p2542862/k$81ffcd7fb53f9142c70d9e5c72e6aaa8/%E0%B9%84%E0%B8%A1%E0%B9%89%E0%B8%9B%E0%B8%B4%E0%B8%87%E0%B8%9B%E0%B8%AD%E0%B8%87%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B9%80%E0%B8%A5%E0%B9%88%E0%B8%99%E0%B9%83%E0%B8%99%E0%B8%AA%E0%B9%82%E0%B8%A1%E0%B8%AA%E0%B8%A3%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%A5%E0%B9%88%E0%B8%99%E0%B8%97%E0%B8%B8%E0%B8%81%E0%B8%AA%E0%B9%84%E0%B8%95%E0%B8%A5%E0%B9%8C-8546887.jpg'))
system.add_equipment_by_sport(Equipment('PP02','ไม้ปิงปอง(คู่)', 100, 'ปิงปอง', 'https://contents.mediadecathlon.com/p1241056/k$c4e81c4254a7352cb84cd1e9b0dc0422/%E0%B8%8A%E0%B8%B8%E0%B8%94%E0%B8%95%E0%B8%B5%E0%B8%9B%E0%B8%B4%E0%B8%87%E0%B8%9B%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B8%E0%B9%88%E0%B8%99-%E0%B8%AA%E0%B8%B3%E0%B8%AB%E0%B8%A3%E0%B8%B1%E0%B8%9A%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%80%E0%B8%A5%E0%B9%88%E0%B8%99%E0%B8%9A%E0%B8%99%E0%B9%82%E0%B8%95%E0%B9%8A%E0%B8%B0%E0%B8%82%E0%B8%99%E0%B8%B2%E0%B8%94%E0%B9%80%E0%B8%A5%E0%B9%87%E0%B8%81%E0%B9%83%E0%B8%99%E0%B8%A3%E0%B9%88%E0%B8%A1-%E0%B8%9E%E0%B8%A3%E0%B9%89%E0%B8%AD%E0%B8%A1%E0%B9%84%E0%B8%A1%E0%B9%89-%E0%B8%AD%E0%B8%B1%E0%B8%99%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%A5%E0%B8%B9%E0%B8%81-%E0%B8%A5%E0%B8%B9%E0%B8%81-8500829.jpg?f=1920x0&format=auto'))

system.add_equipment_by_sport(Equipment('TB01','ไม้เทนนิส WILSON(เดี่ยว)', 50, 'เทนนิส', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRfFQhPORZJ7XMsxsKQXwS7N1fv0km10bR_g&s'))
system.add_equipment_by_sport(Equipment('TB02','ไม้เทนนิส WILSON(คู่)', 100, 'เทนนิส', 'https://raketka.ua/image/catalog/2024/08/04/Wilson%20Blade%20Pro%2098%2016x19%20V9%20WR150511%2014.jpg'))
system.add_equipment_by_sport(Equipment('TB03','ลูกเทนนิส(เดี่ยว)', 30, 'เทนนิส', 'https://media.istockphoto.com/id/137345149/th/%E0%B8%A3%E0%B8%B9%E0%B8%9B%E0%B8%96%E0%B9%88%E0%B8%B2%E0%B8%A2/%E0%B8%A5%E0%B8%B9%E0%B8%81%E0%B9%80%E0%B8%97%E0%B8%99%E0%B8%99%E0%B8%B4%E0%B8%AA.jpg?s=612x612&w=0&k=20&c=LPIiWTPRVcpu0L0AYOkj497cWeCJh0hNCDs-T4FCCYo='))
system.add_equipment_by_sport(Equipment('TB04','ลูกเทนนิส(แพ็ค 3)', 90, 'เทนนิส', 'https://image.makewebcdn.com/makeweb/m_1920x0/QCaGJLM49/1/AAC60B5A_8CF3_47AC_8C65_8D265FE38E5F.jpeg'))

system.add_equipment_by_sport(Equipment('FB01','ลูกฟุตบอล(ธรรมดา)', 60, 'ฟุตบอล', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcSJ-IbCSJAy9q-ZT3sd91dwVxtBZ7m9WAXw&s'))
system.add_equipment_by_sport(Equipment('FB02','ลูกฟุตบอล Molten', 100, 'ฟุตบอล', 'https://ik.imagekit.io/onenow/seven/1682571481.16sov4Z7eMV0jX0exuov9s4zUMej2m7J.jpeg?tr=f-auto,pr-true,ar-1-1,w-1200,fo-auto'))


################################################################################################

UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app, rt = fast_app(
    hdrs=(
        Style(""" 
                html, body {
                    height: 100%;
                    margin: 0;
                    padding: 0;
                    overflow: hidden;
                }
                
                .homepage {
                    min-height: 100vh;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                    background: url('https://scontent.fbkk6-2.fna.fbcdn.net/v/t39.30808-6/484033645_1288390358922966_3478436809208648281_n.jpg?_nc_cat=103&ccb=1-7&_nc_sid=127cfc&_nc_ohc=wvbBXcO9rbwQ7kNvgGRjRDw&_nc_oc=AdgnB2s56jiXPJSVRQPNcRU4UQjImLLSHNBjnXrrx_NcRCOudd8fdBKCCYNxbcK-7GM&_nc_zt=23&_nc_ht=scontent.fbkk6-2.fna&_nc_gid=AxmWnftVwNcysXoQZ8aW5xi&oh=00_AYFUijB8Osy6Evyl9wqwAgaOZpyfKtZwXhyic5vbsSLP3g&oe=67D4C03A') no-repeat center center fixed;
                    background-size: cover;
                    position: relative;
                }

                .admin {
                    min-height: 100vh;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                    background: url('https://images.unsplash.com/photo-1541744573515-478c959628a0?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center fixed;
                    background-size: cover;
                    position: relative;
                }
                
                /* Navbar */
                .navbar {
                    background-color: #000000;
                    background-color: rgba(0, 0, 0, 0.5); /* สีดำโปร่งใส 50% */
                    width: 100vw; /* ให้ Navbar เต็มจอ */
                    position: fixed;
                    top: 0;
                    left: 0;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 15px 40px;
                    color: white;
                    font-size: 18px;
                    z-index: 1000;
                }

                .navbar a {
                    color: white;
                    text-decoration: none;
                    margin-left: 20px;
                    font-weight: bold;
                }

                .navbar-links {
                    display: flex;
                }
                
                .navbar-item{
                    
                }
                
                .navbar-item:hover {
                    color: #ffffff;
                    font-weight: bold;
                    transform: scale(120%); /* ขยายขนาดขึ้น 5% */
                    transition: 0.3s ease-in-out;
                }


                /* Hero Section */
                .hero {
                    display: flex;
                    justify-content: space-between; /* แยก ซ้าย - ขวา */
                    align-items: center; /* จัดให้อยู่ตรงกลางแนวตั้ง */
                    padding: 100px 50px;
                }

                .hero-left {
                    flex: 1;
                    display: flex;
                    justify-content: flex-start; /* โลโก้ชิดซ้าย */
                }

                .hero-right {
                    flex: 1;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                }
                .hero h1 {
                    font-size: 50px;
                    font-weight: bold;
                    color: #6A31A5;
                }

                .hero p {
                    font-size: 18px;
                    color: #444;
                    max-width: 600px;
                    margin: auto;
                }

                .button {
                    background-color: #000000;
                    background-color: rgba(0, 0, 0, 0.7);
                    color: white;
                    border: none;
                    padding: 15px 30px;
                    margin-top: 20px;
                    font-size: 18px;
                    border-radius: 15px;
                    cursor: pointer;
                    margin-right: 10px; /* แก้ปุ่มติดกัน */
                }
                
                .button-side {
                    width: 100%;
                    background-color: #FFFFFF;
                    color: black;
                    border: none;
                    padding: 15px 30px;
                    margin-top: 20px;
                    font-size: 15px;
                    font-weight: bold;
                    border-radius: 15px;
                    cursor: pointer;
                    margin-right: 10px; /* แก้ปุ่มติดกัน */
                }

                .button:hover {
                    background-color: #00000;
                    background-color: rgba(0, 0, 0, 0.8);
                    font-weight: bold;
                    transform: scale(120%); /* ขยายขนาดขึ้น 5% */
                    transition: 0.3s ease-in-out;
                }

                /* Footer */
                .footer {
                    background-color: #000000;
                    background-color: rgba(0, 0, 0, 0.5); /* สีดำโปร่งใส 50% */
                    width: 100vw;
                    text-align: center;
                    padding: 15px 0;
                    position: fixed;
                    bottom: 0;
                    left: 0;
                }

                .footer a {
                    color: white;
                    text-decoration: none;
                    font-weight: bold;
                }
                
                .grid{
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: space-between;
                    gap: 20px; /* ระยะห่างระหว่างการ์ด */
                    padding-top: 40px;
                }
                .water {
                    width: 300px;
                    height: 400px;
                    border-radius: 20px;
                    background-color: #ffffff;
                }
                .data {
                    display: flex;
                    justify-content: space-between;
                    margin-left: 10px;
                    margin-right: 10px;
                }
                .points{
                    background-color: #C5A3FF;
                    padding: 10px 20px;
                    border-radius: 20px;
                    display: inline-block;
                    text-align: center;
                    margin-top: 100px;
                }
                .button_w {
                    background-color: #FFFFFF;
                    color: black;
                    border: none;
                    padding: 15px 30px;
                    margin-top: 20px;
                    font-size: 18px;
                    border-radius: 15px;
                    cursor: pointer;
                    margin-right: 10px; /* แก้ปุ่มติดกัน */
                    box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.2);
                    padding: 20px;
                    border-radius: 10px;
                    background-color: white;
                    font-weight: bold;
                }
                
                .button_w:hover {
                    background-color: #ffffff; /* เปลี่ยนสีเมื่อ hover */
                    color: black; /* เปลี่ยนสีตัวอักษร */
                    font-weight: bold;
                    transform: scale(120%); /* ขยายขนาดขึ้น 5% */
                    transition: 0.3s ease-in-out; /* ทำให้เอฟเฟกต์ดูสมูท */
                }
              
                .button_p {
                    background-color: #A56EFF;
                    color: #ffffff;
                    border: none;
                    padding: 15px 30px;
                    margin-top: 20px;
                    font-size: 18px;
                    border-radius: 15px;
                    cursor: pointer;
                    margin-right: 10px; /* แก้ปุ่มติดกัน */
                }
                
                .input {
                    border: 2px solid #a855f7;
                    border-radius: 8px;
                    padding: 8px;
                    width: 100%;
                }
                
                .side-button {
                    color: #A56EFF;
                    background-color: white;
                    border: none;
                    padding: 10px;
                    border-radius: 20px;
                    font-weight: bold;
                    cursor: pointer;
                    width: 200px;
                }
                .coupon-card {
                    background-color: #ffffff;
                    border-radius: 15px;
                    padding: 20px;
                    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                    margin: 10px;
                    text-align: left;
                }

                .coupon-grid {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 20px;
                }
                .acceptreserve {
                    min-height: 100vh;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                    background: url('https://images.unsplash.com/photo-1541744573515-478c959628a0?q=80&w=1935&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D') no-repeat center center fixed;
                    background-size: cover;
                    position: relative;
                }
                .button-container {
                    display: flex;
                    flex-direction: column; /* เรียงปุ่มเป็นแนวตั้ง */
                    gap: 10px; /* เพิ่มระยะห่างระหว่างปุ่ม */
                    margin-top: 20px;
                }
                .hero home{
                    display: flex;
                    justify-content: space-between;
                }
                .signup {
                    min-height: 100vh;
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    text-align: center;
                    background: url('https://media.discordapp.net/attachments/1334177447930892463/1349017358592643072/parsoa-khorsand-Br1xuldqYcM-unsplash.jpg?ex=67d191d1&is=67d04051&hm=7bd712deb771be6045e63e18e82fbc2e683b35ea6bc33d9670922e63691296ed&=&format=webp&width=1380&height=920') no-repeat center center fixed;
                    background-size: cover;
                    position: relative;
                }
        """),
        Script(src="https://unpkg.com/hyperscript.org@0.9.12")
    ))
#################################          หน้าหลัก Guest        ###############################################
# @rt("/Home")
# async def home(request):
#     account_id = request.session.get("account_id")  # ดึงค่า account_id จาก session
#     if account_id is None:
#         return Script("window.location.href = '/login';")  # ถ้าไม่มี account_id ให้กลับไปหน้า login

#     return Html(f"""
#         <h1>Welcome, your account ID is {account_id}</h1>
#     """)

@rt("/")  # main page
def get():
    return Container(
        Script("""
            document.addEventListener("DOMContentLoaded", function () {
                document.body.classList.add("homepage");
            });
        """),
        
        # Navbar
        Div(Div(
            H1("DMIS COURT"),
            Div(
                A("อัตราราคา", href="/booking-rates", cls = "navbar-item"),
                A("SIGN UP", href="/signup", cls = "navbar-item"),
                A("LOG IN", href="/login", cls = "navbar-item"),
                cls="navbar-links"
            ),
            cls="navbar"
        ),

        # Hero Section
        Div(
        Img(src="https://media.discordapp.net/attachments/1202220660613726248/1348657664065933384/IMG_6527.png?ex=67d042d3&is=67cef153&hm=53c2883354e1cbc5948074d8cfa58bc8d2c74e27639185a540336593f2664f7c&=&format=webp&quality=lossless&width=1050&height=1050", 
            style="height: 600px; width: 600px;"),
        Div(
            P("Hi, there. We are DMIS Court! Welcome to the best sport court booking service website of all time :D", style="color: #ffffff; font-weight: bold; font-size: 25px"),
            Div(
                Form(
                    Button("BOOK NOW!", style="font-weight: bold;", cls="button"),
                    method="get",
                    action="/login"
                ),

                Form(
                    Button("COURT CHECKING", style="font-weight: bold;", cls="button"),
                    method="get",
                    action="/court_checking"
                ),
                cls="button-container"
            ),
            style=""
        ),

        cls="hero home"
        ),


        # Footer
        Div(
            A("contact us", href="/contact"),
            cls="footer"
        ), cls="homepage")
    )
        

@rt("/contact")
def get():
    return "contact us" 

@rt("/booking-rates") #รูป
def get():
    return Container(
        Script("""
            document.addEventListener("DOMContentLoaded", function () {
                document.body.classList.add("signup");
            });
        """),
        
        Img(src="https://scontent.fbkk22-2.fna.fbcdn.net/v/t39.30808-6/482139884_1287852505643418_3237391886418985713_n.jpg?_nc_cat=105&ccb=1-7&_nc_sid=127cfc&_nc_ohc=2uKCDhbeAskQ7kNvgG_yjHF&_nc_oc=Adh79XOIB9mVl_I0AVM9Y1nZMFVjDIr7n-r_El1Q4B3nWGe2LfeUXLFKfmXh0OXdtIEUqmNeHF0vMISA4YVLkJ_5&_nc_zt=23&_nc_ht=scontent.fbkk22-2.fna&_nc_gid=A0VkDvTizanHsF4C3s82A6T&oh=00_AYGgPyjkNYlrxXfGx59TbOh4VsabdEiNK5yDECWavcjTvA&oe=67D3C180",
            alt="Court Rates per Hour", style = "width: 500px; height:auto; item-align: center"),
        A("X", href="/", style="color: #6A31A5; text-decoration: none; position: absolute; top: 10px; right: 10px;")
    )

@rt("/admin")
def get():
    return Container(
        Script("""
            document.addEventListener("DOMContentLoaded", function () {
                document.body.classList.add("admin");
            });
        """),
        Div(
            H1("DMIS COURT"),
            H3("ADMIN"),
            style="display: flex; justify-content: space-between; width: 100%;"
        ),
        Div(
            Form(
                Button("Accept Reserve", type="submit"),
                method="get",
                action="/accept_reserve"
            ),
            Form(
                Button("Rent Equipment", type="submit"),
                method="get",
                action="/equipment-rental"
            ),
            Form(
                Button("Accept Cancel", type="submit"),
                method="get",
                action="/accept_cancel"
            ),
            Form(
                Button("Court Checking", type="submit"),
                method="get",
                action="/court_checking"
            ),
            Form(
                Button("Booking", type="submit"),
                method="get",
                action="/booking"
            ),
            style="display: inline-block; white-space: nowrap;"
        )
    )


@rt("/accept_reserve")
def get_accept_reserve():
    data = system.get_unaccept_reserve()
    return Container(
        Div(
            H1("DMIS COURT"),
            A("HOME", href="/admin"),
            style="display: flex; justify-content: space-between; width: 100%;"
        ),
        Container(
            H3("ยืนยันการจอง", style='text-align: center'),
            Table(
                Thead(
                    Tr(
                        Th("ชื่อผู้จอง"),
                        Th("สนาม"),
                        Th("วันที่"),
                        Th("เวลา"),
                        Th("ราคาสุทธิ"),
                        Th("สลิป"),
                        Th("ยืนยัน"),
                        Th("ยกเลิก"),
                        Th("ดูสลิป")
                    )
                ),
                Tbody(
                    *[
                        Tr(
                            Td(name),
                            Td(court),
                            Td(date),
                            Td(time),
                            Td(total_price),
                            Td(
                                Img(src= slip, alt="Slip Image", style="width: 100px; height: auto;")),
                            Td(
                            Form(
                                Input(type="hidden", name="name", value=name),
                                Input(type="hidden", name="court", value=court),
                                Input(type="hidden", name="date", value=date),
                                Input(type="hidden", name="time", value=time),
                                Button("ยืนยัน", type="submit"),
                                method="post",
                                action="/confirm_booking")
                            ),
                            Td(
                            Form(
                                Input(type="hidden", name="name", value=name),
                                Input(type="hidden", name="court", value=court),
                                Input(type="hidden", name="date", value=date),
                                Input(type="hidden", name="time", value=time),
                                Button("ยกเลิก", type="submit"),
                                method="post",
                                action="/cancel_booking")
                            ),
                            Td(
                                Form(
                                    Input(type="hidden", name="slip", value=slip),
                                    Button("",type="radio"),
                                    method = "post",
                                    action="/seeslip"
                                )
                                
                            )
                        ) 
                        for oneData in data 
                        for name, court, date, time, slip, status, total_price in [oneData] 
                    ]
                )
            ), 
        ),  
    ) if data else Container(
        Div(
            H1("DMIS COURT"),
            A("HOME", href="/"),
            style="display: flex; justify-content: space-between; width: 100%;"
        ),
        Container(
            H3("ยืนยันการจอง", style='text-align: center'),
            Div(
                H2("ไม่มีรายการจองที่ยังไม่ได้รับการยืนยัน", style='text-align: center'),
                style="background-color: e6f3ff; padding: 20px;"
            ) 
        ),  
    )

@rt("/seeslip")
async def post(request):
    form_data = await request.form()
    slip = form_data.get("slip")
    return Container(
        Img(src= slip, alt="Slip Image", style="width: auto; height: auto;")
    )


@rt("/confirm_booking", methods=["POST"])
async def confirm_booking(request):
    form_data = await request.form()
    name = form_data.get("name")
    court = form_data.get("court")
    date = form_data.get("date")
    time = form_data.get("time")

    result = system.find_courtbooking_to_accept(name, court, date, time)

    return Container(
        H1("DMIS COURT"),
        H3("ยืนยันสำเร็จ", style="color: green; text-align: center;"),
        A("NEXT", href="/accept_reserve", style="display: block; text-align: center;")
    ) if result == "Accept reserve complete!!" else Container(
        H1("DMIS COURT"),
        H3("ยืนยันไม่สำเร็จ", style="color: green; text-align: center;"),
        H3(f"{result}", style="color: green; text-align: center;"),
        A("NEXT", href="/accept_reserve", style="display: block; text-align: center;")
    )

@rt("/cancel_booking", methods=["POST"])
async def confirm_booking(request): 
    form_data = await request.form()
    name = form_data.get("name")
    court = form_data.get("court")
    date = form_data.get("date")
    time = form_data.get("time")

    result = system.find_courtbooking_to_cancel(name, court, date, time)

    return Container(
        H1("DMIS COURT"),
        H3("ยกเลิกสำเร็จ", style="color: green; text-align: center;"),
        A("NEXT", href="/accept_reserve", style="display: block; text-align: center;")
    ) if result == "Remove Success!" else Container(
        H1("DMIS COURT"),
        H3("ยกเลิกไม่สำเร็จ", style="color: green; text-align: center;"),
        H3(f"{result}", style="color: green; text-align: center;"),
        A("NEXT", href="/accept_reserve", style="display: block; text-align: center;")
    )


@rt("/booking_tennis_court")
def get_available_selection_tennis(request, court: str = None, date: str = None, time: str = None):
    account_id = request.query_params.get("account_id") 
    bigdata = system.avaliable_date_time("เทนนิส")
    if not bigdata:
        return "No available courts"

    content = []

    if not court:
        court_options = [Option(c, value=c) for c in bigdata.keys()]
        content.append(Container(H1("ประเภทกีฬา: เทนนิส"),
            Form(
                Label("เลือกสนาม", 
                    Select(id="court", name="court", 
                         hx_get="/update_tennis", hx_target="#preview", 
                         hx_trigger="change, focusout", 
                         hx_vals=f"js:{{court: event.target.value, account_id: '{account_id}'}}"
                                     , *court_options))
        )))
    elif not date:
        available_dates = bigdata.get(court, [])
        unique_dates = sorted(set([d for d, _ in available_dates]))
        date_options = [Option(d, value=d) for d in unique_dates]
        content.append(Form(
            Label("เลือกวันที่", 
                  Select(id="date", name="date", 
                         hx_get="/update_tennis", hx_target="#preview", 
                         hx_trigger="change, focusout", 
                         hx_vals=f"js:{{court: '{court}', date: event.target.value, account_id: '{account_id}'}}"
                                    , *date_options))
        ))
    elif not time:
        available_dates = bigdata.get(court, [])
        time_options = [Option(t, value=t) for d, t in available_dates if d == date]
        content.append(Form(
            Label("เลือกเวลา", 
                  Select(id="time", name="time", 
                         hx_get="/update_tennis", hx_target="#preview", 
                         hx_trigger="change, focusout", 
                         hx_vals=f"js:{{court: '{court}', date: '{date}', time: event.target.value, account_id: '{account_id}'}}"
                                     , *time_options))
        ))
    else:
        content.append(Container(Div(f"ท่านกำลังจะจอง: {court} | {date} | {time}"),
                                 Form(
                                    Button(f"ดำเนินการต่อไป", type="submit"),
                                    Input(type="hidden", name="account_id", value=account_id),
                                    Input(type="hidden", name="court_name", value=court),
                                    Input(type="hidden", name="date", value=date),
                                    Input(type="hidden", name="time", value=time),
            
                                     method="get",
                                     action="/Submitnocoupon"
                                 )))
    content.append(Div(id="preview"))
    return Container(*content)

@rt("/booking_football_court")
def get_available_selection_football(request, court: str = None, date: str = None, time: str = None):
    account_id = request.query_params.get("account_id") 
    bigdata = system.avaliable_date_time("ฟุตบอล")
    if not bigdata:
        return "No available courts"

    content = []

    if not court:
        court_options = [Option(c, value=c) for c in bigdata.keys()]
        content.append(Container(H1("ประเภทกีฬา: ฟุตบอล"),
            Form(
                Label("เลือกสนาม", 
                    Select(id="court", name="court", 
                         hx_get="/update_football", hx_target="#preview", 
                         hx_trigger="change, focusout", 
                         hx_vals=f"js:{{court: event.target.value, account_id: '{account_id}'}}"
                                     , *court_options))
        )))
    elif not date:
        available_dates = bigdata.get(court, [])
        unique_dates = sorted(set([d for d, _ in available_dates]))
        date_options = [Option(d, value=d) for d in unique_dates]
        content.append(Form(
            Label("เลือกวันที่", 
                  Select(id="date", name="date", 
                         hx_get="/update_football", hx_target="#preview", 
                         hx_trigger="change, focusout", 
                         hx_vals=f"js:{{court: '{court}', date: event.target.value, account_id: '{account_id}'}}"
                                    , *date_options))
        ))
    elif not time:
        available_dates = bigdata.get(court, [])
        time_options = [Option(t, value=t) for d, t in available_dates if d == date]
        content.append(Form(
            Label("เลือกเวลา", 
                  Select(id="time", name="time", 
                         hx_get="/update_football", hx_target="#preview", 
                         hx_trigger="change, focusout", 
                         hx_vals=f"js:{{court: '{court}', date: '{date}', time: event.target.value, account_id: '{account_id}'}}"
                                     , *time_options))
        ))
    else:
        content.append(Container(Div(f"ท่านกำลังจะจอง: {court} | {date} | {time}"),
                                 Form(
                                     Button("ดำเนินการต่อไป", type="submit"),
                                     Input(type="hidden", name="account_id", value=account_id),
                                     Input(type="hidden", name="court_name", value=court),
                                     Input(type="hidden", name="date", value=date),
                                     Input(type="hidden", name="time", value=time),
                                     method="get",
                                     action="/Submitnocoupon"
                                 )))    
    content.append(Div(id="preview"))
    return Container(*content)

@rt("/booking_table_tennis_court")
def get_available_selection_table_tennis(request, court: str = None, date: str = None, time: str = None):
    account_id = request.query_params.get("account_id") 
    bigdata = system.avaliable_date_time("ปิงปอง")
    if not bigdata:
        return "No available courts"

    content = []

    if not court:
        court_options = [Option(c, value=c) for c in bigdata.keys()]
        content.append(Container(H1("ประเภทกีฬา: ปิงปอง"),
            Form(
                Label("เลือกสนาม", 
                    Select(id="court", name="court", 
                         hx_get="/update_table_tennis", hx_target="#preview", 
                         hx_trigger="change, focusout", 
                         hx_vals=f"js:{{court: event.target.value, account_id: '{account_id}'}}"
                                     , *court_options))
        )))
    elif not date:
        available_dates = bigdata.get(court, [])
        unique_dates = sorted(set([d for d, _ in available_dates]))
        date_options = [Option(d, value=d) for d in unique_dates]
        content.append(Form(
            Label("เลือกวันที่", 
                  Select(id="date", name="date", 
                         hx_get="/update_table_tennis", hx_target="#preview", 
                         hx_trigger="change, focusout", 
                         hx_vals=f"js:{{court: '{court}', date: event.target.value, account_id: '{account_id}'}}"
                                    , *date_options))
        ))
    elif not time:
        available_dates = bigdata.get(court, [])
        time_options = [Option(t, value=t) for d, t in available_dates if d == date]
        content.append(Form(
            Label("เลือกเวลา", 
                  Select(id="time", name="time", 
                         hx_get="/update_table_tennis", hx_target="#preview", 
                         hx_trigger="change, focusout", 
                         hx_vals=f"js:{{court: '{court}', date: '{date}', time: event.target.value, account_id: '{account_id}'}}"
                                     , *time_options))
        ))
    else:
        content.append(Container(Div(f"ท่านกำลังจะจอง: {court} | {date} | {time}"),
                                 Form(
                                     Button("ดำเนินการต่อไป", type="submit"),
                                     Input(type="hidden", name="account_id", value=account_id),
                                     Input(type="hidden", name="court_name", value=court),
                                     Input(type="hidden", name="date", value=date),
                                     Input(type="hidden", name="time", value=time),
                                     method="get",
                                     action="/Submitnocoupon"
                                 )))
    content.append(Div(id="preview"))
    return Container(*content)


@rt('/update_tennis')
async def get(request: Request):
    court = request.query_params.get("court")
    date = request.query_params.get("date")
    time = request.query_params.get("time")
    account_id = request.query_params.get("account_id")  # ✅ ดึงค่า account_id

    return get_available_selection_tennis(request, court, date, time)


@rt('/update_football')
async def get(request: Request):
    court = request.query_params.get("court")
    date = request.query_params.get("date")
    time = request.query_params.get("time")
    account_id = request.query_params.get("account_id")
    return get_available_selection_football(request, court, date, time)

@rt('/update_table_tennis')
async def get(request: Request):
    court = request.query_params.get("court")
    date = request.query_params.get("date")
    time = request.query_params.get("time")
    account_id = request.query_params.get("account_id")
    return get_available_selection_table_tennis(request, court, date, time)

@rt("/court_checking")
def index(sport_type: str = None, selected_date: str = None):
    from datetime import date as dt, timedelta

    sport_type_options = [
        Option("เทนนิส", value="เทนนิส"),
        Option("ฟุตบอล", value="ฟุตบอล"),
        Option("ปิงปอง", value="ปิงปอง")
    ]
    
    date_options = [
        Option((dt.today() + timedelta(days=i)).isoformat(),
               value=(dt.today() + timedelta(days=i)).isoformat())
        for i in range(31)
    ]
    
    content = []
    
    if not sport_type:
        content.append(Div(
            H1("DMIS COURT"),
            A("HOME", href="/"),
            style="display: flex; justify-content: space-between; width: 100%;"
        ))
        content.append(Form(
            Label("เลือกประเภทกีฬา"),
            Select(id="sport_type", name="sport_type",
                   hx_get="/update_table", hx_target="#preview",
                   hx_trigger="change, focusout",
                   hx_vals="js:{sport_type: event.target.value}",
                   *sport_type_options)
        ))
    elif not selected_date:
        content.append(Form(
            Label("เลือกวันที่"),
            Select(id="date", name="date",
                   hx_get="/update_table", hx_target="#preview",
                   hx_trigger="change, focusout",
                   hx_vals=f"js:{{sport_type: '{sport_type}', date: event.target.value}}",
                   *date_options)
        ))
    else:

        time_range = [
            "10:00-11:00", "11:00-12:00", "12:00-13:00",
            "13:00-14:00", "14:00-15:00", "15:00-16:00",
            "16:00-17:00", "17:00-18:00", "18:00-19:00",
            "19:00-20:00", "20:00-21:00"
        ]
        
        court_names, already_accepts, not_accepts = system.get_info_for_create_table(sport_type, selected_date)
        
        content.append(Container(
            H3(f"ตารางจองสนาม {sport_type} ณ วันที่ {selected_date}", style='text-align: center'),
            Table(
                Thead(
                    Tr(
                        Th("เวลา/สนาม"), 
                        *[Th(time) for time in time_range]  
                    )
                ),
                Tbody(
                    *[
                        Tr(
                            Td(court_name),
                            *[
                                Td(
                                    "จองได้" if court_name not in [i[0] for i in already_accepts + not_accepts] else
                                    "รอการยืนยัน" if [court_name, time] in not_accepts else
                                    "จองแล้ว" if [court_name, time] in already_accepts else
                                    "จองได้"
                                )
                                for time in time_range  
                            ]
                        )
                        for court_name in court_names
                    ]
                )
            )
        ))
    
    content.append(Div(id="preview"))
    return Container(*content)

@rt('/update_table')
async def get(request: Request):
    sport_type = request.query_params.get("sport_type")  
    selected_date = request.query_params.get("date")
    return index(sport_type, selected_date)

@rt("/home") 
def get_home(request):
    account_id = request.session.get("account_id")
    return Container(
       Div(
            H1("DMIS COURT"),
            Div(
                A("ACCOUNT", href=f"/account?account_id={account_id}"),
                cls="navbar-links"
            ),
            cls="navbar"
        ),
        
        Div(
            Form(
                Button("COUPON ส่วนลด", cls="button_w"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/claim-coupon"
            ),
            Form(
                Button("ใช้ POINT เพื่อแลกสินค้าต่าง ๆ", cls="button_w"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/redeem"
            ),
            style="display: flex; gap: 10px; justify-content: center;",
            cls="hero"
        ),
        
        Div(
            Form(
                Button("BOOK TENNIS COURT", cls="button_p"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/booking_tennis_court"
            ),
            Form(
                Button("BOOK TABLE TENNIS COURT", cls="button_p"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/booking_table_tennis_court"
            ),
            Form(
                Button("BOOK FOOTBALL COURT", cls="button_p"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/booking_football_court"
            ),
            style="display: flex; gap: 10px; justify-content: center;",
            cls="hero"
        ),

        Div(
            A("contact us", href=f"/contact?account_id={account_id}"),
            cls="footer"
        )
    )

@rt("/claim-coupon")
def get_coupons(request):
    account_id = request.session.get("account_id")
    if not account_id:
        return Script("window.location.href = '/login';")  

    member = system.search_member_by_account_id(account_id)
    coupons = system.get_coupon_list

    return Container(
        Div(H1("Claim Your Coupons"), cls="hero"),
        Div(
            *[
                Div(
                    H3(f"Coupon: {coupon.get_coupon_code} - Discount {coupon.get_coupon_discount}%"),
                    P(f"Expire Date: {coupon.get_expire_date}"),
                    Button(
                        "รับคูปอง" if not member.has_claimed_today(coupon.get_coupon_id) else "เก็บแล้ว",
                        type="submit",
                        disabled=member.has_claimed_today(coupon.get_coupon_id),
                        hx_post="/claim-coupon-action",
                        hx_vals=f"js:{{coupon_id: '{coupon.get_coupon_id}', account_id: '{account_id}'}}",
                        cls="button_p" if not member.has_claimed_today(coupon.get_coupon_id) else "button_w"
                    ),
                    cls="coupon-card"
                )
                for coupon in coupons
            ],
            cls="coupon-grid"
        )
    )

@rt("/claim-coupon-action", methods=["POST"])
async def claim_coupon_action(request):
    form_data = await request.form()
    account_id = form_data.get("account_id")
    coupon_id = form_data.get("coupon_id")

    member = system.search_member_by_account_id(account_id)
    coupon = system.search_coupon_by_coupon_id(coupon_id)

    if not member or not coupon:
        return "Invalid request"

    result = member.claim_coupon(coupon)
    
    return Script("window.location.reload();") if result == "Coupon claimed successfully" else result


@rt("/account")
def get(request):
    if request.method == "GET":
        # หากเป็น GET ให้ดึงข้อมูลจาก URL query parameters
        account_id = request.query_params.get("account_id", "ไม่ระบุ")

    member = system.search_member_by_account_id(account_id)
    username = member.get_username
    return Container(
        Div(
            H1("DMIS COURT"),
            Div(
                A("ACCOUNT", href="/account"),
                cls="navbar-links"
            ),
            cls="navbar"
        ),
        
        Div(
            Form(
                Button("COUPON ส่วนลด", cls="button_w"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/coupon"
            ),
            Form(
                Button("ใช้ POINT เพื่อแลกสินค้าต่าง ๆ", cls="button_w"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/redeem"
            ),
            style="display: flex; gap: 10px; justify-content: center;",
            cls="hero"
        ),
        
        Div(
            Form(
                Button("BOOK TENNIS COURT", cls="button_p"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/booking_tennis_court"
            ),
            Form(
                Button("BOOK TABLE TENNIS COURT", cls="button_p"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/booking_table_tennis_court"
            ),
            Form(
                Button("BOOK FOOTBALL COURT", cls="button_p"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/booking_football_court"
            ),
            style="display: flex; gap: 10px; justify-content: center;",
            cls="hero"
        ),

        # Footer
        Div(
            A("contact us", href="/contact"),
            cls="footer"
        ),
        # แถบด้านข้าง
        Div(
            A("X", href="/home", style="color: #6A31A5; text-decoration: none; position: absolute; top: 10px; right: 10px;"),
            H5(f"Hello, {username}", style="color: #6A31A5;"),
            
            Form(
                Button("MY PROFILE", cls = "button-side"),
                Input(type="hidden", name="account_id", value=account_id),
                method="get",
                action="/my-profile",
                style="width: 100%; display: flex; flex-direction: column; align-items: flex-start;",
            ),
            
            Div(
                Form(
                    Input(type="hidden", name="account_id", value=account_id),  # ใส่ account_id ที่ต้องส่ง
                    Button("ประวัติการจอง", cls="button-side"),
                    method="post",
                    action="/bookingHis"
                ),
                
                Button("เปลี่ยนรหัสผ่าน", cls="button-side"),
                Button("ลบบัญชี", cls="button-side"),
                style="display: flex; flex-direction: column; align-items: flex-start;",
            ),

            A("Log out", href="/", style="color: #6A31A5; text-decoration: none; display: block; margin-top: 10px;"),
            style="position: fixed; right: 0; top: 0; background-color: #e9d5ff; padding: 20px; width: 220px; height: 100vh; box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1); z-index: 9999;"
        )
    )

@rt("/my-profile")
def get(request):
    if request.method == "GET":
        # หากเป็น GET ให้ดึงข้อมูลจาก URL query parameters
        account_id = request.query_params.get("account_id", "ไม่ระบุ")
    member = system.search_member_by_account_id(account_id)
    username = member.get_username
    name = member.get_name
    surname = member.get_surname
    birthdate = member.get_birthdate
    gender = member.get_gender
    gmail = member.get_gmail
    phone = member.get_phone
    point = member.get_point
    coupon = member.get_coupon_list
    dmis_coin = member.get_dmis_coin

    return Container(
        # Navbar
        Div(
            H1("DMIS COURT"),
            Div(A("HOME", href="/home"), cls="navbar-links"),
            cls="navbar"
        ),
        # Main content
        Div(
            # Profile Section
            Div(
                Div(
                    Img(src="https://i.pinimg.com/736x/15/0f/a8/150fa8800b0a0d5633abc1d1c4db3d87.jpg", style="width: 80px; height: 80px; border-radius: 50%; background-color: #d8b4fe;"),
                    H5(username, style="text-align: center; font-weight: bold; padding-top: 10px;"),
                    style="display: flex; flex-direction: column; align-items: center;"
                ),
                
                Div(
                H4("ชื่อ: ", style="text-align: left; padding-left: 80px;"), 
                H4(name, style="text-align: left;"),
                H4("นามสกุล: ", style="text-align: left; padding-left: 80px;"), 
                H4(surname, style="text-align: left;"),
                H4("วันเกิด: ", style="text-align: left; padding-left: 80px;"), 
                H4(birthdate, style="text-align: left;"),
                H4("เพศ: ", style="text-align: left; padding-left: 80px;"), 
                H4(gender, style="text-align: left;"),
                H4("E-mail: ", style="text-align: left; padding-left: 80px;"), 
                H4(gmail, style="text-align: left;"),
                H4("เบอร์โทรศัพท์: ", style="text-align: left; padding-left: 80px;"),
                H4(phone, style="text-align: left;"),
                style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px;"
            ),

                
                style="background-color: white; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 6px rgba(0,0,0,0.1); width: 50%;"
            ),

            # Sidebar Menu
            Div(
                Button(f"POINT: {point}", cls="side-button"),
                Form(
                    Button("MY COUPON", type="submit", cls="side-button"),
                    Input(type="hidden", name="account_id", value=account_id),
                    method = "get",
                    action = "/my-coupon"
                    ),
                Button(f"DMIS COIN: {dmis_coin}", cls="side-button"),
                Form(
                    Button("แก้ไขข้อมูลส่วนตัว", type="submit", cls="side-button"),
                    Input(type="hidden", name="account_id", value=account_id),
                    method = "get",
                    action = "/edit-profile"
                    ),
                style="display: flex; flex-direction: column; gap: 40px;"
            ),
            style="display: flex; justify-content: space-between; padding: 20px; background-color: #E6D0FF; padding-top: 165px;"
        ),
        
        # Footer
        Div(
            A("contact us", href="/contact"),
            cls="footer"
        )
    )
    
@rt("/my-coupon")
def get(request):
    if request.method == "GET":
        # หากเป็น GET ให้ดึงข้อมูลจาก URL query parameters
        account_id = request.query_params.get("account_id", "ไม่ระบุ")
    coupons = system.search_member_by_account_id(account_id).get_coupon_list  # Assuming memberA is the logged-in member
    coupon_cards = [
        Card(
            H3(f"Coupon Code: {coupon.get_coupon_code}"),
            P(f"Discount: {coupon.get_coupon_discount}%"),
            P(f"Expire Date: {coupon.get_expire_date}"),
            cls="coupon-card"
        )
        for coupon in coupons
    ]
    
    return Container(
        # Navbar
        Div(
            H1("DMIS COURT"),
            Div(A("HOME", href=f"/home?account_id={account_id}"), cls="navbar-links"),
            cls="navbar"
        ),
        
        # Main content
        Div(
            Div(H2("My Coupons", style="color: #3e1a7d; text-align: center;"),
            Div(*coupon_cards, cls="coupon-grid"),
            style="padding: 20px; background-color: #E6D0FF; padding-top: 120px;"),
        ),
        
        # Footer
        Div(
            A("contact us", href="/contact"),
            cls="footer"
        )
    )


@rt("/edit-profile")
def get(request):
    if request.method == "GET":
        account_id = request.query_params.get("account_id", "ไม่ระบุ")
    member = system.search_member_by_account_id(account_id)
    username = member.get_username
    name = member.get_name
    surname = member.get_surname
    birthdate = member.get_birthdate
    gender = member.get_gender
    gmail = member.get_gmail
    phone = member.get_phone
    return Container(
        # Navbar
        Div(
            H1("DMIS COURT"),
            Div(A("HOME", href=f"/home?account_id={account_id}"), cls="navbar-links"),
            cls="navbar"
        ),

        # Main content
        Div(
            # Profile Section
            Div(
                Div(
                    Img(src="https://i.pinimg.com/736x/15/0f/a8/150fa8800b0a0d5633abc1d1c4db3d87.jpg", style="width: 80px; height: 80px; border-radius: 50%; background-color: #d8b4fe;"),
                    H5(username, style="text-align: center; font-weight: bold; padding-top: 10px;"),
                    style="display: flex; flex-direction: column; align-items: center;"
                ),
                
                Form(
                    Label("ชื่อ: ", style="color: #000000; text-align: left; padding-left: 30px;"), Input(name="name",placeholder=name, type="text", cls="input", style="height: 30px; background-color: #ffffff; color: #000000;"),
                    Label("นามสกุล", style="color: #000000; text-align: left; padding-left: 30px;"), Input(name="surname", placeholder=surname, type="text", cls="input", style="height: 30px; background-color: #ffffff; color: #000000;"),
                    Label("วันเกิด", style="color: #000000; text-align: left; padding-left: 30px;"), Input(name="birth_date",value=birthdate, type="date", cls="input", style="height: 30px; background-color: #ffffff; color: #000000;"),
                    Label("เพศ", style="color: #000000; text-align: left; padding-left: 30px;"), Input(name="gender", placeholder=gender,type="text", cls="input", style="height: 30px; background-color: #ffffff; color: #000000;"),
                    Label("E-mail", style="color: #000000; text-align: left; padding-left: 30px;"), Input(name="gmail", placeholder=gmail, type="email", cls="input", style="height: 30px; background-color: #ffffff; color: #000000;"),
                    Label("เบอร์โทรศัพท์", style="color: #000000; text-align: left; padding-left: 30px;"), Input(name="phone", placeholder=phone, type="text", cls="input", style="height: 30px; background-color: #ffffff; color: #000000;"),
                    
                    
                    Button("ยืนยันการแก้ไข", type="submit", style="font-weight: bold; cursor: pointer; width: 200px; background-color: #A56EFF;"),
                    Input(type="hidden", name="account_id", value=account_id),
                    method="post",
                    action="/edit-profile-data",
                    # style="display: flex; justify-content: flex-end; margin-top: 20px;" # ใช้ flex-end ดันไปขวา
                    style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px;",
                ),
                
                style="background-color: white; padding: 20px; border-radius: 15px; width: 50%;"
            ),

            # Sidebar Menu
            Div(
                Form(
                    Button("ยกเลิกการแก้ไข", type="submit", cls="side-button"),
                    method = "get",
                    action = "/my-profile"
                    ),
                style="display: flex; flex-direction: column; gap: 40px;"
            ),

            style="display: flex; justify-content: space-between; padding: 20px; background-color: #E6D0FF; padding-top: 120px; align-items: right;"
        ),

        # Footer
        Div(
            A("contact us", href="/contact"),
            cls="footer"
        )
    )
    

@rt("/edit-profile-data", methods=["POST"])
async def edit_profile(request):
        form_data = await request.form()
        # print("Received form data:", form_data)  # ตรวจสอบค่าที่ได้รับจากฟอร์ม
        account_id = form_data.get("account_id")
        new_name = form_data.get("name")
        new_surname = form_data.get("surname")
        new_birthdate = form_data.get("birth_date")
        new_gender = form_data.get("gender")
        new_gmail = form_data.get("gmail")
        new_phone = form_data.get("phone")

        member = system.search_member_by_account_id(account_id)

        print(f"New Name: {new_name}, New Surname: {new_surname}, New Birthdate: {new_birthdate}, New Gender: {new_gender}, New Gmail: {new_gmail}, New Phone: {new_phone}")

        # อัปเดตข้อมูล
        #ต้องเขียนเงื่อนไขว่าถ้าค่าที่ได้รับมาเป็นชื่อ ก็แก้แค่ชื่อ แต่ถ้าได้ none มาก็ไม่ต้องทำไร ต้องไปแก้ใน setter ว่าไม่ต้อง
        # ่ใช้ if == None return ชื่อเดิมมา
        member.set_name(new_name)
        member.set_surname(new_surname)
        member.set_birth_date(new_birthdate)
        member.set_gender(new_gender)
        member.set_gmail(new_gmail)
        member.set_phone(new_phone)

        # Redirect ไปหน้าโปรไฟล์หลังแก้ไขเสร็จ
        return Main(
                H1("แก้ไขข้อมูลสำเร็จ!", style="color: #A56EFF;"),
                A("กลับสู่หน้าหลัก", href=f"/home?account_id={account_id}", style="color: white; text-decoration: none; font-weight: bold;"),
                cls="success"
                )

#################################          หน้าแลกของ         ##############################################
@rt("/redeem")  # redeem page
def get(request):
    if request.method == "GET":
        # หากเป็น GET ให้ดึงข้อมูลจาก URL query parameters
        account_id = request.query_params.get("account_id", "ไม่ระบุ")

    points = system.search_member_by_account_id(account_id).get_point
    gift_list = system.get_gift_list
    
    return Container(
        # Navbar
        Div(
            H1("DMIS COURT"),
            Div(A("HOME", href=f"/home?account_id={account_id}"), cls="navbar-links"),
            cls="navbar"
        ),

        # แสดงแต้มที่มีอยู่
        Div(
            Div(H4(f"{points} points", style={"font-weight": "bold", "color": "#ffffff", "padding-top": "10px"}), cls="points"),
        ),
        
        # Hero Section - แสดงสินค้าทั้งหมด
        Grid(
            *[
                Card(
                    Img(src = gift.get_gift_url, height="100px", width="100px"),  # ใช้ URL ของแต่ละสินค้า
                    Div(H3(gift.get_gift_name), H3(f"{gift.get_gift_point}pt"), cls="data"),
                    Form(
                        Hidden(name="item_name", value = gift.get_gift_name),
                        Hidden(name="item_cost", value = gift.get_gift_point),
                        Input(type="hidden", name="account_id", value=account_id),
                        Button("แลกเลย!", type="submit"),
                        action="/redeem_item", method="post",
                        onsubmit="return confirmRedeem(this);"
                    ),
                    cls="water"
                )
                for gift in gift_list  # วนลูปสร้างการ์ด
            ],
            cls="grid"
        ),


        # Footer
        Div(A("contact us", href=f"/contact?account_id={account_id}"), cls="footer"),
        
        Script("""
        function confirmRedeem(form) {
            let confirmAction = confirm("คุณต้องการแลกสินค้านี้จริงหรือไม่?");
            if (confirmAction) {
                return true;  // ส่งฟอร์มไป /redeem_item
            } else {
                return false; // ยกเลิก
            }
        }
        """)
    )


@rt("/redeem_item", methods=["post"])
async def redeem_item(request):
    try:
        form_data = await request.form()
        account_id = form_data.get("account_id")
        member = system.search_member_by_account_id(account_id)
        item_name = form_data.get("item_name")
        item_cost = int(form_data.get("item_cost"))
        
        if member.check_item_point(item_cost):
            # ค้นหาของแลกใน backend
            gift = system.search_gift_by_name(item_name)
            if gift:
                gift.deduct_amount()  # ลบจำนวนของแลก
                # print(gift.get_gift_amount)
                return Main(
                    H3(f"แลก {item_name} สำเร็จ! Point คงเหลือ {member.get_point} points"),
                    A("กลับสู่หน้าหลัก", href=f"/home?account_id={account_id}"),
                    cls="success"
                )
            else:
                return Main(
                    H3("ไม่พบของแลกที่ต้องการ", style={"color": "red"}),
                    A("กลับไปเลือกใหม่", href=f"/redeem?account_id={account_id}"),
                    cls="error"
                )
        else:
            return Main(
                H3("Point ไม่พอTT", style={"color": "#ffffff"}),
                A("กลับไปเลือกใหม่", href=f"/redeem?account_id={account_id}"),
                cls="error"
            )
    except Exception as e:
        return Main(
            H3("เกิดข้อผิดพลาด: " + str(e), style={"color": "red"}),
            A("กลับไปเลือกใหม่", href=f"/redeem?account_id={account_id}"),
            cls="error"
        )

############################ เช่าอุปกรณ์ ########################################
@rt("/equipment-rental")
def get():
    return Container(
        # Navbar
        #Div(
        #     H1("DMIS COURT"),
        #     Div(A("HOME", href="/"), cls="navbar-links"),
        #     cls="navbar"
        # ),

        # search user
        Form(
            Input(placeholder="Search user", name="username"),
            Button("Search", type="submit"),
            method = "post",
        ),

        # Footer
        Div(A("contact us", href="/contact"), cls="footer")
    )

@rt("/equipment-rental", methods=["post"])
async def post(request):
    form_data = await request.form()
    username = form_data.get("username")
    member = system.search_member_by_username(username)
    if not member:
        return "User not found"
    else:
        history = system.get_choosing_list
        if not history:
            return Container(
                H1(f"No successful bookings found for user: {username}"),
                A("Back to search", href="/equipment-rental")
            )
        sports = set(booking.get_court_sport_type for booking in history)
        date_time_options = []
        for booking in history:
            date_time_options.append(Option(f"{booking.get_date} {booking.get_time}", value=f"{booking.get_date} {booking.get_time}"))

        return Container(
            H1(f"User: {member.get_username}"),
            Form(
                Hidden(name="username", value=username),
                Label("เลือกกีฬา:", Select(
                    *[Option(sport, value=sport) for sport in sports],
                    id="choose_sport", name="choose_sport"
                )),
                Label("เลือกวันที่และเวลา:", Select(
                    *date_time_options,
                    id="choose_date_time", name="choose_date_time"
                )),

                Button("ต่อไป", type="submit"),
                action="/select-equipment",  # ส่งไปที่ /select-equipment
                method="post"       # ใช้ POST
            )
        )
        
@rt("/select-equipment", methods=["post"])
async def post(request):
    form_data = await request.form()
    username = form_data.get("username")
    sport = form_data.get("choose_sport")
    date_time = form_data.get("choose_date_time")

    equipment_list = system.get_equipment_by_sport(sport)
    if equipment_list is None:
        return "ไม่มีนี้อุปกรณ์นี้ในระบบ"

    equipment_options = []
    for equipment in equipment_list:
        equipment_options.append(Div(
            Img(src=equipment.get_image_url, height="100px", width="100px"),
            Label(
                f"อุปกรณ์: {equipment.get_item_name} ราคา: {equipment.get_item_price} บาท/ชั่วโมง", 
                Input(type="checkbox", name="equipment", value=equipment.get_item_id), style="color: #3e1a7d"), style="display: flex; align-items: center; justify-content: space-between color: #3e1a7d" 
        ))

    return Container(
        H1(f"เลือกอุปกรณ์สำหรับกีฬา: {sport}"),
        Form(
            Hidden(name="username", value=username),
            Div(
                *equipment_options,
                id="choose_equipment", name="choose_equipment"
            ),
            Hidden(name="choose_date_time", value=date_time),
            Button("ยืนยันการเช่า", type="submit"),
            action="/SubmitEquipmentRental",
            method="post"
        )
    )
    
@rt("/SubmitEquipmentRental", methods=["post"]) 
async def post(request):
    form_data = await request.form()
    username = form_data.get("username")
    date_time = form_data.get("choose_date_time")
    equipment_ids = form_data.getlist("equipment")

    member = system.search_member_by_username(username)
    if not member:
        return "User not found"
    
    total_price = system.calculate_total_equipment_price(equipment_ids)
    date, time = date_time.split()
    equipment_list = [system.search_equipment_by_id_for_rent(equipment_id) for equipment_id in equipment_ids]
    system.add_equipment_rental(EquipmentRental(equipment_list, date, time, member))
    # print(system.get_equipment_rental)
    return Container(
        H1(f"User: {member.get_username}", style="color: #3e1a7d"),
        H2("อุปกรณ์ที่เช่า:", style="color: #3e1a7d"),
        Ul(*[Li(equipment.get_item_name, style="color: #3e1a7d") for equipment in equipment_list]),
        H2("วันที่และเวลา:", style="color: #3e1a7d"),
        P(f"{date} {time}", style="color: #3e1a7d"),
        H2("ยอดรวมทั้งหมด:", style="color: #3e1a7d"),
        P(f"{total_price} บาท", style="color: #3e1a7d"),
        A("กลับสู่หน้าหลัก", href="/", style="color: #3e1a7d"),
    )

@rt("/signup", methods=['post','get'])
async def post(request):
    if request.method == 'POST':
        form_data = await request.form()
        form_data = {
            'username': form_data.get('username'),
            'password': form_data.get('password'),
            'confirm_password': form_data.get('confirm_password'),
            'first_name': form_data.get('first_name'),
            'last_name': form_data.get('last_name'),
            'citizen_id': form_data.get('citizen_id'),
            'phone': form_data.get('phone'),
            'gmail': form_data.get('gmail'),
            'prefix': form_data.get('prefix'),
            'gender': form_data.get('gender', 'ไม่ระบุ'), 
            'birth_date': form_data.get('birth_date', '')
        }
        validation_result = system.validate_data_signup(form_data)
        
        # ถ้าผลลัพธ์ไม่ใช่ True (มีข้อผิดพลาด), ส่งข้อความผิดพลาดกลับไป
        if validation_result != True:
            return Container(
                H1("Sign Up", style="text-align: center; color: #007bff;"),
                Form(
                    Input(type="text", placeholder="Username", name="username", required=True),
                    Input(type="password", placeholder="Password", name="password", required=True),
                    Input(type="password", placeholder="Confirm Password", name="confirm_password", required=True),
                    Select(
                        Option("เพศ", value="", disabled=True, selected=True), 
                        Option("ชาย", value="ชาย"),
                        Option("หญิง", value="หญิง"),
                        Option("ไม่ระบุ", value="ไม่ระบุ"),
                        name="gender", required=True
                        ),
                    Input(type="text", placeholder="ชื่อจริง", name="first_name", required=True),
                    Input(type="text", placeholder="นามสกุล", name="last_name", required=True),
                    Input(type="date", name="birth_date", required=True),
                    Input(type="text", placeholder="เลขบัตรประชาชน", name="citizen_id", required=True),
                    Input(type="tel", placeholder="เบอร์", name="phone", required=True),
                    Input(type="email", placeholder="Gmail", name="gmail", required=True),
                    Button("Sign Up", type="submit", 
                        style="width:100%; background:#007bff; color:white; padding:12px; border:none; border-radius:5px; font-size:16px; box-shadow: 4px 4px 8px rgba(0,0,0,0.2); cursor:pointer; transition: all 0.3s;",
                        onmouseover="this.style.backgroundColor = '#90EE90';",
                        onmouseout="this.style.backgroundColor = '#007bff';"),

                    P(validation_result, style="color: red; text-align: center;"),
                      P("Already have an account? ", A("Log in", href="/login", style="color:#007bff; text-decoration:none;")),  # แสดงข้อผิดพลาด
                    action="/signup", method="post",  
                ),
                style="width: 350px; margin: auto; padding: 20px; background: white; border-radius: 15px; box-shadow: 0 20px 40px rgba(255, 255, 255, 0.1); text-align: center;"
            )
        request.session["signup_data"] = form_data
        return Redirect("/login")

    return Container(
        Script("""
            document.addEventListener("DOMContentLoaded", function () {
                document.body.classList.add("signup");
            });
        """),
        H1("Sign Up", style="text-align: center; color: #ffffff;"),
        Form(
            Input(type="text", placeholder="Username", name="username", required=True),
            Input(type="password", placeholder="Password", name="password", required=True),
            Input(type="password", placeholder="Confirm Password", name="confirm_password", required=True),
            Select(
                    Option("เพศ", value="", disabled=True, selected=True), 
                    Option("ชาย", value="ชาย"),
                    Option("หญิง", value="หญิง"),
                    Option("ไม่ระบุ", value="ไม่ระบุ"),
                    name="gender", required=True
                        ),
            Input(type="text", placeholder="ชื่อจริง", name="first_name", required=True),
            Input(type="text", placeholder="นามสกุล", name="last_name", required=True),
            Input(type="date", name="birth_date", required=True, id="birth_date"),
            Input(type="text", placeholder="เลขบัตรประชาชน", name="citizen_id", required=True),
            Input(type="tel", placeholder="เบอร์", name="phone", required=True),
            Input(type="email", placeholder="Gmail", name="gmail", required=True),
            Button("Sign Up", type="submit", 
                        style="width:100%; background:#007bff; color:white; padding:12px; border:none; border-radius:5px; font-size:16px; box-shadow: 4px 4px 8px rgba(0,0,0,0.2); cursor:pointer; transition: all 0.3s;",
                        onmouseover="this.style.backgroundColor = '#90EE90';",
                        onmouseout="this.style.backgroundColor = '#007bff';"),
            P("Already have an account? ", A("Log in", href="/login", style="color:#007bff; text-decoration:none;")),
            action="/signup", method="post",
        ),
        style="width: 450px; margin: auto; padding: 20px; background-color: #000000; background-color: rgba(0, 0, 0, 0.7); border-radius: 15px; box-shadow: 0 20px 40px text-align: center;"
    )

@rt("/login", methods=['POST', 'GET'])
async def get(request):
    if request.method == "POST":
        form_data = request.session.get("signup_data")

    # ดึงข้อมูลจาก form_data ที่มาจากการสมัครสมาชิก
        username = form_data.get('username')
        password = form_data.get('password')
        first_name = form_data.get('first_name')
        last_name = form_data.get('last_name')
        citizen_id = form_data.get('citizen_id')
        phone = form_data.get('phone')
        gmail = form_data.get('gmail')
        gender = form_data.get('gender')
        birth_date = form_data.get('birth_date')

    # สร้างผู้ใช้งานใหม่
        a = system.create_user_member(
            first_name, last_name, citizen_id, phone, gender, birth_date, username, password, gmail
        )
    # ส่งกลับฟอร์มล็อกอิน
    return Container(
        Div(
            H1("Login", style="text-align: center; color: #007bff;"),
            Form(
                Input(type="text", placeholder="Username", name="username", required=True),
                Input(type="password", placeholder="Password", name="password", required=True),

                Button("Log In", type="submit", 
                    style="width:100%; background:#007bff; color:white; padding:12px; border:none; border-radius:5px; font-size:16px; box-shadow: 4px 4px 8px rgba(0,0,0,0.2); cursor:pointer; transition: all 0.3s;",
                    onmouseover="this.style.backgroundColor = '#90EE90';",
                    onmouseout="this.style.backgroundColor = '#007bff';"),

                # การใช้ hx_post สำหรับการส่งข้อมูลแบบ AJAX
                hx_post="/check_login",  # ส่งข้อมูลไปที่ /check_login
                hx_trigger="submit",  # ทำเมื่อ submit ฟอร์ม
                hx_target="#login-message",  # เป้าหมายการแสดงข้อความ (error message)
                hx_swap="innerHTML",  # ใช้เพื่อแทนที่เนื้อหาของ #login-message ด้วยข้อความ

            ),
            P(id="login-message", style="color: red; text-align: center; font-weight: bold;"),  # แสดงข้อความ error ถ้ามี
            P("Don't have an account? ", 
                A("Sign Up", href="/signup", style="color:#007bff; text-decoration:none;")),

            style="width: 350px; margin: auto; padding: 20px; background: white; border-radius: 15px; box-shadow: 0 20px 40px rgba(255, 255, 255, 0.1); text-align: center; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);"
        )
    )


@rt("/check_login", methods=['post'])
async def check_login(request):
    form_data = await request.form()
    username = form_data.get("username")
    password = form_data.get("password")

    # เช็คก่อนว่าเป็นผู้ดูแลระบบ
    admin_login_result = system.check_admin_login(username, password)
    if admin_login_result is True:
        admin = system.search_admin_by_username(username)
        admin_id = admin.get_account_id
        request.session["account_id"] = admin_id  # หรือคุณจะตั้งค่าหมายเลขบัญชีเฉพาะสำหรับ admin
        return Script("window.location.href = '/AdminHome';")  # เปลี่ยนไปหน้า Admin Dashboard

    # ถ้าไม่ใช่ admin เช็คจากระบบสมาชิกปกติ
    login_result = system.check_login(username, password)
    if login_result is True:
        member = system.search_member_by_username(username)
        account_id = member.get_account_id
        request.session["account_id"] = account_id
        return Script("window.location.href = '/home';")  # ✅ Redirect เมื่อ login สำเร็จ
    
    # ถ้าล็อกอินไม่สำเร็จ จะส่งข้อความผิดพลาด
    return P(login_result, style="color: red; text-align: center; font-weight: bold;")  # ✅ แสดง error message


@rt("/Submitnocoupon", methods=["GET", "POST"])
async def post(request):
    if request.method == "POST":
        # หากเป็น POST ให้ดึงข้อมูลจาก form
        form_data = await request.form()
        account_id = form_data.get("account_id", "ไม่ระบุ")
        court_id = form_data.get("court_id", "ไม่ระบุ")
        date = form_data.get("date", "ไม่ระบุ")
        time = form_data.get("time", "ไม่ระบุ")
    elif request.method == "GET":
        # หากเป็น GET ให้ดึงข้อมูลจาก URL query parameters
        account_id = request.query_params.get("account_id", "ไม่ระบุ")
        court_name = request.query_params.get("court_name", "ไม่ระบุ")
        date = request.query_params.get("date", "ไม่ระบุ")  # เปลี่ยนจาก "date" เป็น "data" ตามพารามิเตอร์ที่ส่ง
        time = request.query_params.get("time", "ไม่ระบุ")
        court_instance = system.search_court_by_court_name(court_name)
        court_id = court_instance.get_court_id
    
    coupon_id = None

    court = system.search_court_by_court_id(court_id)
    
    return Container(
        Titled("ยืนยันการจอง"),
        H4(f"สนามที่เลือก: {court.court_name}"),
        H4(f"วันที่: {date}"),
        H4(f"เวลา: {time}"),
        H4("คูปองที่เลือก: "),
        
        # ฟอร์มไปเลือกคูปอง
        Div(
            Form(
                Button("เลือกคูปอง", type="submit", style="margin-right: 10px;"),
                Input(type="hidden", name="account_id", value=account_id),
                Input(type="hidden", name="court_id", value=court_id),
                Input(type="hidden", name="date", value=date),
                Input(type="hidden", name="time", value=time),
                action="/Coupon",
                method="post"
            ),
            Form(
                Button("ยกเลิกใช้คูปอง", type="submit", id="cancel_coupon", style="background-color: red; color: white; padding: 5px 10px; border: none; border-radius: 5px; cursor: pointer;"),
                Input(type="hidden", name="account_id", value=account_id),
                Input(type="hidden", name="court_id", value=court_id),
                Input(type="hidden", name="date", value=date),
                Input(type="hidden", name="time", value=time),
                action="/Submitnocoupon",
                method="post"
            ),
        ),

        H4(f"ราคาสุทธิ: {court.get_court_price}"),
        H4("ช่องทางการชำระเงิน"),
        
        Form(
            Input(type="hidden", name="court_id", value=court_id),
            Input(type="hidden", name="date", value=date),
            Input(type="hidden", name="time", value=time),
            Input(type="hidden", name="account_id", value=account_id),
            Input(type="hidden", name="total_price", value=court.get_court_price),
            Input(type="hidden", name="payment_method", value="QR_CODE"),
            Input(type="hidden", name="coupon_id", value=coupon_id),
            Button("ชําระเงินด้วย QRCODE", type="submit"),
            action="/QRCODE",
            method="post"
        ),

        Form(
            Input(type="hidden", name="court_id", value=court_id),
            Input(type="hidden", name="date", value=date),
            Input(type="hidden", name="time", value=time),
            Input(type="hidden", name="account_id", value=account_id),
            Input(type="hidden", name="total_price", value=court.get_court_price),
            Input(type="hidden", name="payment_method", value="DMIS_PAY"),
            Button("ชำระเงินด้วย DMIS COINS", type="submit"),
            action="/Dmis_pay",
            method="post"
        ),

        Br(),
        A("home", href=f"/home?account_id={account_id}"),
    )



@rt("/Coupon", methods=["POST"])
async def post(request):
    form_data = await request.form()
    account_id = form_data.get("account_id")
    court_id = form_data.get("court_id", "ไม่ระบุ")
    date = form_data.get("date", "ไม่ระบุ")
    time = form_data.get("time", "ไม่ระบุ")
    member = system.search_member_by_account_id(account_id)

    court = system.search_court_by_court_id(court_id)
    coupon_list = member.get_member_coupon_list  # ดึงรายการคูปองของสมาชิก

    return Container(
        Titled("เลือกคูปองเลย!"),
        H2("คูปองของคุณ"),
        Form(
            Grid(
                *[
                    Button(
                        H4(f"{coupon.get_coupon_discount}%", alignment="center", size="lg"),
                        type="submit",
                        name="coupon_id",  # ชื่อฟิลด์ที่จะส่งไป
                        value=coupon.get_coupon_id,  # ค่าของคูปองที่เลือก
                        style={
                            "background": "#F3E8FF",
                            "padding": "20px",
                            "border-radius": "10px",
                            "text-align": "center",
                            "border": "none"
                        }
                    )
                    for coupon in coupon_list
                ],
                columns=4,  # แสดง 4 คอลัมน์ต่อแถว
                gap="10px"
            ),
            Input(type="hidden", name="account_id", value=account_id),
            Input(type="hidden", name="court_id", value=court_id),
            Input(type="hidden", name="date", value=date),
            Input(type="hidden", name="time", value=time),

            action="/Submitwithcoupon",  # ฟอร์มจะส่งกลับไปที่ /Submit
            method="post"  # ส่งข้อมูลแบบ POST
        ),
        Button(
            "Back",
            onClick=f"window.location.href='Submitnocoupon?account_id={account_id}&court_name={court.court_name}&data={date}&time={time}';"
        ),
    )

@rt("/Submitwithcoupon", methods=["POST"])
async def post(request):
    form_data = await request.form()
    account_id = form_data.get("account_id", "ไม่ระบุ")
    court_id = form_data.get("court_id", "ไม่ระบุ")
    date = form_data.get("date", "ไม่ระบุ")
    time = form_data.get("time", "ไม่ระบุ")
    coupon_id = form_data.get("coupon_id", "ไม่ระบุ")  # รับ coupon_id จากหน้า Coupon

    member = system.search_member_by_account_id(account_id)
    court = system.search_court_by_court_id(court_id)
    coupon = member.search_member_coupon_by_coupon_id(coupon_id)

    total_price = Payment.calculate_price_with_coupon(court.get_court_price, coupon.get_coupon_discount)

    return Container(
        Titled("ยืนยันการจอง"),
        H4(f"สนามที่เลือก: {court.court_name}"),
        H4(f"วันที่: {date}"),
        H4(f"เวลา: {time}"),
        H4("คูปองที่เลือก: ", Span(f"{coupon.get_coupon_discount}%", id="coupon_info")),  # ใช้ Span เพื่อให้ JavaScript อัปเดตค่า

            Div(
                Form(
                    Button("เลือกคูปอง", type="submit", style="margin-right: 10px;"),
                    Input(type="hidden", name="account_id", value=account_id),
                    Input(type="hidden", name="court_id", value=court_id),
                    Input(type="hidden", name="date", value=date),
                    Input(type="hidden", name="time", value=time),
                    action="/Coupon",
                    method="post"
                ),
                Form(
                    Button("ยกเลิกใช้คูปอง", type="submit", id="cancel_coupon", style="background-color: red; color: white; padding: 5px 10px; border: none; border-radius: 5px; cursor: pointer;"),
                    Input(type="hidden", name="account_id", value=account_id),
                    Input(type="hidden", name="court_id", value=court_id),
                    Input(type="hidden", name="date", value=date),
                    Input(type="hidden", name="time", value=time),
                    action="/Submitnocoupon",
                    method="post"
                ),
        ),
        H4(f"ราคาสุทธิ: {total_price}", id="total_price"),  # ใช้ id เพื่ออัปเดต UI ผ่าน JavaScript
        H4("ช่องทางการชำระเงิน"),

        Form(
            Input(type="hidden", name="court_id", value=court_id),
            Input(type="hidden", name="date", value=date),
            Input(type="hidden", name="time", value=time),
            Input(type="hidden", name="account_id", value=account_id),
            Input(type="hidden", name="total_price", value=total_price),
            Input(type="hidden", name="coupon_id", value=coupon_id),
            Input(type="hidden", name="payment_method", value="QR_CODE"),
            Button("ชําระเงินด้วย QRCODE", type="submit"),
            action="/QRCODE",
            method="post"
        ),

        Form(
            Input(type="hidden", name="court_id", value=court_id),
            Input(type="hidden", name="date", value=date),
            Input(type="hidden", name="time", value=time),
            Input(type="hidden", name="account_id", value=account_id),
            Input(type="hidden", name="total_price", value=total_price),
            Input(type="hidden", name="coupon_id", value=coupon_id),
            Input(type="hidden", name="payment_method", value="DMIS_PAY"),
            Button("ชำระเงินด้วย DMIS COINS", type="submit"),
            action="/Dmis_pay",
            method="post"
        ),

        Br(),
        A("ย้อนกลับ", href="/"),

    )

@app.post("/upload")
async def upload(request: Request):
    form_data = await request.form()
    file = form_data.get("payment_receipt")  # รับไฟล์จากฟอร์ม

    if file:
        file_path = f"uploads/{file.filename}"  # กำหนดพาธไฟล์ที่จะบันทึก
        with open(file_path, "wb") as f:
            f.write(await file.read())  # บันทึกไฟล์ลงเซิร์ฟเวอร์
        
        # ส่งพาธไฟล์กลับไปอัปเดตในฟอร์มของหน้า QRCODE
        return HTMLResponse(content=f'<script>document.getElementById("payment_receipt_path").value="{file_path}";</script> File uploaded successfully!')
    
    return HTMLResponse(content="No file uploaded!")

@rt("/QRCODE", methods=["GET", "POST"])
async def post(request):
    form_data = await request.form()
    account_id = form_data.get("account_id", "ไม่ระบุ")
    court_id = form_data.get("court_id", "ไม่ระบุ")
    date = form_data.get("date", "ไม่ระบุ")
    time = form_data.get("time", "ไม่ระบุ")
    coupon_id = form_data.get("coupon_id")
    total_price = form_data.get("total_price")

    court = system.search_court_by_court_id(court_id)
    expire_time = system.time_expire_five_minute()  

    merch = system.merch_js_qr()

    return Container(
        Titled("คิวอาร์ชำระเงิน"),
        H4(f"สนามที่เลือก: {court.court_name}"),
        H4(f"วันที่: {date}"),
        H4(f"เวลา: {time}"),
        H4(f"ราคาสุทธิ: {total_price} บาท"),
        H4(f"กรุณาชำระเงินก่อน {expire_time}"),

        Div(id="countdown", style="font-size: 20px; font-weight: bold; color: red;"),
        # แสดง QR Code

        Div(
            Img(src="img/MyQRCODE.jpg", style="width: 502px; height: 731px; margin-top: 10px;"),
            style="display: flex; justify-content: center; align-items: center;"
        ),

        Br(),
        Form(
            hx_target="#output", 
            hx_post="/upload",  # ส่งไฟล์ไปที่ /upload
            id="upload_form", 
            enctype="multipart/form-data",
        )(
            Input(type="file", name="payment_receipt", accept=".jpg,.jpeg,.png", required=True),
            P("*ชนิดไฟล์ที่รองรับ: jpg, jpeg, png"),
            Button("Upload"),
            Progress(id="progress", value="0", max="100", style="margin-top:20px"),
            Div(id="output"),
        ),

        # ฟอร์มยืนยันการจอง (ส่งไฟล์ที่อัปโหลดไปหน้า /ConfirmReserve)
        Form(
            action="/ConfirmReserve",
            method="post",
        )(
            Input(type="hidden", name="court_id", value=court_id),
            Input(type="hidden", name="date", value=date),
            Input(type="hidden", name="time", value=time),
            Input(type="hidden", name="account_id", value=account_id),
            Input(type="hidden", name="total_price", value=total_price),
            Input(type="hidden", name="coupon_id", value=coupon_id),
            Input(type="hidden", id="payment_receipt_path", name="payment_receipt", value=""),  # เก็บพาธไฟล์ที่อัปโหลด
            Button("ยืนยันการจอง", type="submit", id="confirm_button", 
                   style="background-color: lightgreen; padding: 20px 20px; border: none; border-radius: 5px; font-size: 25px; cursor: pointer;",
                   disabled=True),  # ปิดปุ่มยืนยัน จนกว่าจะอัปโหลดไฟล์เสร็จ
            Br(),
        ),
        Button(
            "Back",
            onClick=f"window.location.href='Submitnocoupon?account_id={account_id}&court_name={court.court_name}&data={date}&time={time}';"
        ),

        # ใส่ JavaScript สำหรับอัปเดต hidden input และ countdown
        Script(merch)
    )

@rt("/Dmis_pay", methods=["GET", "POST"])
async def post(request):
    form_data = await request.form()
    account_id = form_data.get("account_id", "ไม่ระบุ")
    court_id = form_data.get("court_id", "ไม่ระบุ")
    date = form_data.get("date", "ไม่ระบุ")
    time = form_data.get("time", "ไม่ระบุ")
    coupon_id = form_data.get("coupon_id")
    total_price = form_data.get("total_price")

    total_price = int(float(total_price)) 

    member = system.search_member_by_account_id(account_id)
    court = system.search_court_by_court_id(court_id)
    expire_time = system.time_expire_five_minute()

    js = system.generate_js_countdown()

    dmiscoins_minus_price = Payment.calculate_price_dmis_coins(total_price, member.get_dmis_coin)
    check = Payment.check_coins_enough(member.get_dmis_coin, total_price)

    return Container(
        Titled("ชำระเงินด้วย DMIS COINS"),
        H2(f"คุณมี DMIS COINS: {member.get_dmis_coin} COINS"),
        P("1 DMIS COINS = 1 บาท"),
        H4(f"สนามที่เลือก: {court.court_name}"),
        H4(f"วันที่: {date}"),
        H4(f"เวลา: {time}"),
        H4(f"ราคาสุทธิ: {total_price} บาท"),
        H4(f"กรุณาชำระเงินก่อน {expire_time}"),

        Div(id="countdown", style="font-size: 20px; font-weight: bold; color: red;"),
        Br(),
        P(f"*หากคุณกดยืนยันการจองระบบจะทําการจองและ DMISCOINS คงเหลือของคุณจะเท่ากับ:  {dmiscoins_minus_price}*", style="font-weight: bold; color: #FF474C"),
        Form(
            action="/ConfirmReserve",
            method="post",
        )(
            Input(type="hidden", name="court_id", value=court_id),
            Input(type="hidden", name="date", value=date),
            Input(type="hidden", name="time", value=time),
            Input(type="hidden", name="account_id", value=account_id),
            Input(type="hidden", name="total_price", value=total_price),
            Input(type="hidden", name="coupon_id", value=coupon_id),
            Input(type="hidden", id="payment_receipt_path", name="payment_receipt", value="dmis_pay"),  # เก็บพาธไฟล์ที่อัปโหลด
            Button(
                "ยืนยันการจอง",
                type="submit",
                id="confirm_button",
                disabled=(check),  # ปิดปุ่มถ้าเหรียญไม่พอ
                style="background-color: lightgreen; padding: 20px 20px; border: none; border-radius: 5px; font-size: 25px; cursor: pointer;",
            ),

            Br(),
        ),
           Button(
            "Back",
            onClick=f"window.location.href='Submitnocoupon?account_id={account_id}&court_name={court.court_name}&data={date}&time={time}';"

        ),
        Script(js)
    )


@rt("/ConfirmReserve", methods=["POST"])
async def post(request):
    form_data = await request.form()
    court_id = form_data.get("court_id", "ไม่ระบุ")
    date = form_data.get("date", "ไม่ระบุ")
    time = form_data.get("time", "ไม่ระบุ")
    account_id = form_data.get("account_id", "ไม่ระบุ")
    coupon_id = form_data.get("coupon_id",None)
    total_price = form_data.get("total_price")
    payment_receipt = form_data.get("payment_receipt")
    

    court = system.search_court_by_court_id(court_id)
    member = system.search_member_by_account_id(account_id)

    print("DEBUG: coupon_id =", coupon_id, "type:", type(coupon_id))

    # js = system.back_home_after_delay()

    system.request_create_booking(court_id, date, time, account_id, payment_receipt, total_price,  coupon_id)
    # for i in system.get_court_booking_list:
    #     print(i.get_court_booking_id())
    print(system.search_court_booking_by_id('000001'))
    print(system.search_court_booking_by_payment('dmis_pay'))
    print(system.search_court_booking_by_payment('qr_code'))
    print(member.get_dmis_coin)

    return Container(
        H1(f'จองสนาม {court.court_name} สำเร็จ'),
        H4("ขอบคุณที่ใช้บริการกับเรา :D"),

        # ปุ่มกดกลับไปที่หน้าโฮม พร้อมพา account_id ไปด้วย
        Button(
            "Back",
            onClick=f"window.location.href='/home?account_id={account_id}';"
        ),

        # Script(js)  # ใช้ JavaScript ที่รีไดเรกอัตโนมัติหลัง 30 วิ
)


###############################################################################

@rt('/bookingHis')
async def post(request):
    booking_data = await request.form()
    account_id = booking_data.get("account_id")
    member = system.search_member_by_account_id(account_id)
    history = member.view_history
    # Return the history data dynamically rendered in the table
    return Titled(
        Div(
            H2("ประวัติการจองสนาม", style="text-align: left; flex-grow: 1;"),
            Form(Button("ยกเลิกการจอง", type="cancel", style="font-size: 14px; padding: 5px 10px; min-width: 120px;"), method="get", action="/choose_order"),
            style="display: flex; gap: 10px; justify-content: center;"
        ),
        Table(
            Tbody(*[
    Tr(*[Td(str(value)) for value in [
        #  str(booking)
         booking.get_court_name,
         booking.get_date,
         booking.get_time,
         booking.get_court_booking_status

        # booking.get_court_booking_id()
    ]])
    for booking in history
])

        )
    )

@rt('/choose_order')
def get():
    return Titled(
        "กรุณาเลือกรายการที่ต้องการยกเลิก",
        Table(
            Thead(Tr(Th(" "),Th("กีฬา"), Th("สนาม"), Th("วัน"), Th("เวลา"))),
            Tbody(
                Tr(
                    Td(Form(
                            Button("", type="radio", name="selected_booking", value=str(booking.get_court_booking_id), style="width: 20px; height: 20px;"),
                            method="post",
                            action="/cancel"
                        ), 
                        Td(booking.get_court_sport_type), 
                        Td(booking.get_court_name), 
                        Td(booking.get_date), 
                        Td(booking.get_time)
                    )
                )
                for booking in system.get_choosing_list
            )
        )
    )

@rt('/cancel', methods=["post"])
async def post(request):
    booking_data = await request.form()
    selected_booking_id = booking_data.get("selected_booking")

    # ค้นหาข้อมูลการจองที่ตรงกับ ID ที่เลือก
    selected_booking = next((booking for booking in system.get_choosing_list if str(booking.get_court_booking_id) == selected_booking_id), None)

    if selected_booking:
        sport_type = selected_booking.get_court_sport_type
        court_name = selected_booking.get_court_name
        date = selected_booking.get_date
        time = selected_booking.get_time
        
        return Container( 
            H2("คุณต้องการยกเลิกการจองสนามดังนี้ใช่หรือไม่", style="text-align: center;"),  # ใช้ H1 เพื่อให้หัวข้อใหญ่
            H6("กรุณาตรวจสอบให้ถี่ถ้วน เมื่อยกเลิกแล้วจะไม่สามารถกลับไปแก้ไขได้อีก", style="text-align: center;"),
            Card(
                P(f"{sport_type} - {court_name} - {date} - {time} "),
                style=""" 
                text-align: center;  /* จัดข้อความให้อยู่กลาง */
                border: 1px solid black;
                border-radius: 10px;
                border-width: 2px;
                """
            ),
            Div(  # ใช้ Div เพื่อจัดปุ่มให้อยู่บรรทัดเดียวกัน
                Form(Button("ยกเลิก", type="submit"), method="get", action="/choose_order"),
                Form(
                    Button("ยืนยัน", type="submit", name="selected_booking", value=str(selected_booking.get_court_booking_id)), method="post", action="/requestcanceldone"),
                style="display: flex; gap: 10px; justify-content: center;"
            )
        )
    else:
        return H2("การจองไม่พบหรือมีปัญหากับข้อมูลที่เลือก")

@rt('/requestcanceldone')
async def post(request):
    booking_data = await request.form()
    selected_booking_id = booking_data.get("selected_booking")

    selected_booking = next((booking for booking in system.get_choosing_list if str(booking.get_court_booking_id) == selected_booking_id), None)
    
    if selected_booking:
        court_booking_status = selected_booking.get_court_booking_status
        account_id = selected_booking.get_account_id
        member = system.search_member_by_account_id(account_id)

    system.accept_cancel(selected_booking)
    system.request_cancel(selected_booking)
    selected_booking.change_status_cancel("รอยืนยันการยกเลิก")
   
      
    # member.add_booking_history(selected_booking)
    #เหลือ total_price,payment_receipt,status_booking_success
    return Container(
             Card(
            H3("รอการยกเลิกการจองสนาม"),
            P(F"เมื่อยกเลิกสำเร็จจะส่งแจ้งเตือน หวังว่าเราจะได้ให้บริการคุณอีกในภายหลัง "),
            style="""
            text-align: center;"  # left, right, center, justify
            border: 1px solid black;  /* ขนาด สไตล์ สี ขอบ */
            border-radius: 10px;      /* ความโค้งขอบมน */
            border-width: 2px;        /* ความหนาขอบ */
            """
            
        )
    )

@rt("/accept_cancel")
def get():
    return Titled(
        "คำขอยกเลิกการจอง",
        Table(
            Thead(Tr(Th("ชื่อผู้จอง"), Th("กีฬา"), Th("สนาม"), Th("วันที่"), Th("เวลา"), Th("สลิป"), Th("ยืนยัน"))),
            Tbody(
                *[
                    Tr(
                        Td(booking.get_username), 
                        Td(booking.get_court_sport_type),
                        Td(booking.get_court_name),  
                        Td(booking.get_date),
                        Td(booking.get_time),
                        Td(booking.get_receipt),
                        Td(booking.get_court_booking_status),
                        Td(
                            Form(
                                Button("", type="submit", name="selected_booking", value=str(booking.get_court_booking_id), style="width: 20px; height: 20px;"),
                                method="post",
                                action="/confirmcancel"
                            )
                        )
                    )
                    for booking in system.get_request_cancel_list
                ]
            )
        )
    )

@rt('/confirmcancel', methods=["post"])
async def post(request):
    booking_data = await request.form()
    selected_booking_id = booking_data.get("selected_booking")

    selected_booking = next((booking for booking in system.get_request_cancel_list if str(booking.get_court_booking_id) == selected_booking_id), None)

    if selected_booking:
        sport_type = selected_booking.get_court_sport_type
        court_name = selected_booking.get_court_name
        date = selected_booking.get_date
        time = selected_booking.get_time
        account_id = selected_booking.get_account_id
        member = system.search_member_by_account_id(account_id)
        username = member.get_username
        return Container( 
            H2("คุณต้องการยกเลิกการจองสนามดังนี้ใช่หรือไม่", style="text-align: center;"),  # ใช้ H1 เพื่อให้หัวข้อใหญ่
            H6("กรุณาตรวจสอบให้ถี่ถ้วน เมื่อยกเลิกแล้วจะไม่สามารถกลับไปแก้ไขได้อีก", style="text-align: center;"),
            Card(
                P(f"{username} - {sport_type} - {court_name} วันที่ {date} เวลา {time} "),
                style=""" 
                text-align: center;  /* จัดข้อความให้อยู่กลาง */
                border: 1px solid black;
                border-radius: 10px;
                border-width: 2px;
                """
            ),
            Div( 
                Form(Button("ยกเลิก", type="submit"), method="get", action="/acceptcancel"),
                Form(
                    Button("ยืนยัน", type="submit", name="selected_booking", value=str(selected_booking.get_court_booking_id)), method="post", action="/acceptcanceldone"),
                style="display: flex; gap: 10px; justify-content: center;"
            )
        )
    else:
        return H2("การจองไม่พบหรือมีปัญหากับข้อมูลที่เลือก")

@rt("/acceptcanceldone")
async def post(request):
    booking_data = await request.form()
    selected_booking_id = booking_data.get("selected_booking")

    selected_booking = next((booking for booking in system.get_request_cancel_list if str(booking.get_court_booking_id) == selected_booking_id), None)
    if selected_booking:
        court_name = selected_booking.get_court_name
        account_id = selected_booking.get_account_id
        date = selected_booking.get_date
        time = selected_booking.get_time
        sport_type = selected_booking.get_court_sport_type
        member = system.search_member_by_account_id(account_id)
        system.remove_request(selected_booking)

        username = member.get_username
        selected_booking.change_status_cancel("ยกเลิกสำเร็จ")

        total_price = selected_booking.get_total_price
        refund = total_price*(0.8)
        member.add_dmis_coins(refund)
   
        # member.add_booking_history(selected_booking)  

    return Container(
        Card(
            H3("ยืนยันการยกเลิกการจอง"),
            P(f"{username} - {sport_type} - {court_name}-- วันที่ {date} เวลา {time}"),
            style="""
            text-align: center;"  # left, right, center, justify
            border: 1px solid black;  /* ขนาด สไตล์ สี ขอบ */
            border-radius: 10px;      /* ความโค้งขอบมน */
            border-width: 2px;        /* ความหนาขอบ */
            """
        )
    )



serve(host="127.0.0.1", port=5032)