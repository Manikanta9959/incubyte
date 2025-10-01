import re

class StringCalc():
    
    def __init__(self, str_num : str):
        self.str_num = str_num
        
    
    def add(self):
        if not self.str_num:
            return 0
        
        delimiter = ","
        numbers_to_parse = self.str_num
        
            
        
        numbers_to_parse = numbers_to_parse.replace("\n", delimiter)
                
        
        number_strings = re.split(delimiter, numbers_to_parse)
        
        print(number_strings)
        
        parsed_numbers = []
        
        
        for num_str in number_strings:
            if num_str:
                num = int(num_str)
                parsed_numbers.append(num)
        
        
        return sum(parsed_numbers)
    

str_cal_obj = StringCalc("1\n1,2,3")
print(str_cal_obj.add())

        
    
    
    