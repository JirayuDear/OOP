class BaseClass:
    num_base_class = 0
    
    def call_me(self):
        print("base")
        self.num_base_class += 1

class LeftSubClass(BaseClass):
    num_left_class = 0
    
    def call_me(self):
        super().call_me()
        print('left')
        self.num_left_class += 1

class RightSubClass(BaseClass):
    num_right_class = 0
    
    def call_me(self):
        super().call_me()
        print('right')
        self.num_right_class += 1

class SubClass(LeftSubClass, RightSubClass):
    num_sub_class = 0
    
    def call_me(self):
        super().call_me()
        print('sub')
        self.num_sub_class += 1

s = SubClass()
s.call_me()
print(s.num_sub_class, s.num_left_class, s.num_right_class, s.num_base_class)

print(SubClass.__mro__)
