

class Addition:
    

    def __init__(self):
        self.special_chars = ['[',']','(',')','"',"'"]
        pass

    def get_numbers(self,numbers):
        """tests to determine how numbers were passed into the calculator"""
        if ',' in numbers:
            return [number for number in numbers.split(',')]
        elif ' ' in numbers:
            return [number for number in numbers.split(' ')]
        else:
            return 1

    def add(self, numbers):
        numbers = self.get_numbers(numbers)
        val = 0
        for number in numbers:
            try:
                val = val + float(number)
            except TypeError:
                return -1
            except ValueError:                        
                number2 = self.remove_special_chars(number)
                val = val + float(number2)
        return val
    
    def remove_special_chars(self,number):
        for char in self.special_chars:
            if char in number:
                return number.replace(char,'')
        return -1