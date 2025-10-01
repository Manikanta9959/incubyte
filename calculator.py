import re

class StringCalc():
    
    def __init__(self, str_num : str):
        self.str_num = str_num
        
    
    def add(self):
        if not self.str_num:
            return 0
        
        delimiter = ","
        numbers_to_parse = self.str_num
        
        if self.str_num.startswith("//"):
            delimiter_end = self.str_num.index("\n")
            delimiter = self.str_num[2:delimiter_end]
            numbers_to_parse = self.str_num[delimiter_end + 1:]
            
        
        numbers_to_parse = numbers_to_parse.replace("\n", delimiter)
        
        escaped_delimiter = re.escape(delimiter)
        
        number_strings = re.split(escaped_delimiter, numbers_to_parse)
        
        print(number_strings)
        
        parsed_numbers = []
        negative_numbers = []
        
        for num_str in number_strings:
            if num_str:
                num = int(num_str)
                parsed_numbers.append(num)
                if num < 0:
                    negative_numbers.append(num)
        
        if negative_numbers:
            negative_str = ", ".join(map(str, negative_numbers))
            raise ValueError(f"negative numbers not allowed: {negative_str}")
        
        return sum(parsed_numbers)
    

str_cal_obj = StringCalc("//;\n1;2")
print(str_cal_obj.add())

        
    
    
    