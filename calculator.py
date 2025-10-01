import re
from typing import List, Tuple


class StringCalculator:
    
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiter, numbers_to_parse = self._extract_delimiter_and_numbers(numbers)
        number_list = self._parse_numbers(numbers_to_parse, delimiter)
        self._validate_negatives(number_list)
        
        return sum(number_list)
    
    def _extract_delimiter_and_numbers(self, numbers: str) -> Tuple[str, str]:
        if numbers.startswith("//"):
            delimiter_end = numbers.index("\n")
            delimiter = numbers[2:delimiter_end]
            numbers_to_parse = numbers[delimiter_end + 1:]
            return delimiter, numbers_to_parse
        
        return ",", numbers
    
    def _parse_numbers(self, numbers_str: str, delimiter: str) -> List[int]:
        normalized_string = self._normalize_delimiters(numbers_str, delimiter)
        number_strings = self._split_by_delimiter(normalized_string, delimiter)
        return self._convert_to_integers(number_strings)
    
    def _normalize_delimiters(self, numbers_str: str, delimiter: str) -> str:
        return numbers_str.replace("\n", delimiter)
    
    def _split_by_delimiter(self, numbers_str: str, delimiter: str) -> List[str]:
        escaped_delimiter = re.escape(delimiter)
        return re.split(escaped_delimiter, numbers_str)
    
    def _convert_to_integers(self, number_strings: List[str]) -> List[int]:
        return [int(num_str) for num_str in number_strings if num_str and int(num_str) <= 1000]
    
    def _validate_negatives(self, numbers: List[int]) -> None:
        negatives = [num for num in numbers if num < 0]
        
        if negatives:
            self._raise_negative_exception(negatives)
    
    def _raise_negative_exception(self, negatives: List[int]) -> None:
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