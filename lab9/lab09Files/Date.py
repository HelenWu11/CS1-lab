'''
Start to the Date class for Lab 9.  This code will not run in Python
until three methods are added:
    __init__,
    __str__
    same_day_in_year
'''

days_in_month = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
month_names = [ '', 'January', 'February', 'March', 'April', 'May', 'June', 'July',\
                    'August','September', 'October', 'November', 'December' ]

class Date(object):
    def __init__(self,year=1900,month=1,day=1):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        if int(self.month) < 10:
            self.month = str(self.month).rjust(2,'0')
        if int(self.day) < 10:
            self.day = str(self.day).rjust(2,'0')
        return str(self.year)+'/'+str(self.month)+'/'+str(self.day)
    
    def same_day_in_year(self,other):
        if self.month == other.month and\
           self.day == other.day:
            return True
        else:
            return False
    
    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0 and self.year % 400 != 0:
                return False
            else:
                return True
        else:
            return False
    
    def __lt__(self,other):
        if int(self.year) < int(other.year):
            return True
        elif int(self.year) > int(other.year):
            return False
        elif int(self.year) == int(other.year):
            if int(self.month) < int(other.month):
                return True
            elif int(self.month) == int(other.month):
                if int(self.day) < int(other.day):
                    return True
                else:
                    return False
            else:
                return False
        
if __name__ == "__main__":
    d1 = Date(1954, 10, 4)
    d2 = Date(1900, 7, 11)
    d3 = Date(1973, 7, 11)
    d4 = Date(1998, 4, 11)
    d5 = Date(1998, 5, 13)
    print("d1: " + str(d1))
    print("d2: " + str(d2))
    print("d3: " + str(d3))
    print("d1.same_day_in_year(d2)", d1.same_day_in_year(d2))
    print("d2.same_day_in_year(d3)", d2.same_day_in_year(d3)) 
    print ()
    print("d1.is_leap_year()",d1.is_leap_year())
    print("d2.is_leap_year()",d2.is_leap_year())
    print("d1 < d2",d1.__lt__(d2))
    print("d2 < d5",d2.__lt__(d5))
    print("d5 < d4",d5.__lt__(d4))