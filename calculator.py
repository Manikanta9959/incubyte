import re
from typing import List, Tuple


class StringCalculator:
    
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiters, numbers_to_parse = self._extract_delimiter_and_numbers(numbers)
        number_list = self._parse_numbers(numbers_to_parse, delimiters)
        self._validate_negatives(number_list)
        
        return sum(number_list)
    
    def _extract_delimiter_and_numbers(self, numbers: str) -> Tuple[List[str], str]:
        if numbers.startswith("//"):
            delimiter_end = numbers.index("\n")
            delimiter_section = numbers[2:delimiter_end]
            numbers_to_parse = numbers[delimiter_end + 1:]

            delimiters = re.findall(r"\[(.*?)\]", delimiter_section)
            if not delimiters:
                delimiters = [delimiter_section]
                
            return delimiters, numbers_to_parse
        
        return [",", "\n"], numbers
    
    def _parse_numbers(self, numbers_str: str, delimiters: List[str]) -> List[int]:
        number_strings = self._split_by_delimiter(numbers_str, delimiters)
        return self._convert_to_integers(number_strings)
    
    def _split_by_delimiter(self, numbers_str: str, delimiters: List[str]) -> List[str]:
        regex_pattern = "|".join(map(re.escape, delimiters))
        return re.split(regex_pattern, numbers_str)
    
    def _convert_to_integers(self, number_strings: List[str]) -> List[int]:
        return [int(num_str) for num_str in number_strings if num_str and int(num_str) <= 1000]
    
    def _validate_negatives(self, numbers: List[int]) -> None:
        negatives = [num for num in numbers if num < 0]
        if negatives:
            negative_str = ", ".join(map(str, negatives))
            raise ValueError(f"negative numbers not allowed: {negative_str}")


if __name__ == "__main__":
    calc = StringCalculator()
    
    print(calc.add(""))
    print(calc.add("1"))
    print(calc.add("1,5"))
    print(calc.add("1,2,3,4,5"))
    print(calc.add("1\n2,3"))
    print(calc.add("//;\n1;2"))
    print(calc.add("//|\n1|2|3"))
    
    try:
        calc.add("1,-2,3")
    except ValueError as e:
        print(e)
    
    try:
        calc.add("1,-2,-3,4,-5")
    except ValueError as e:
        print(e)