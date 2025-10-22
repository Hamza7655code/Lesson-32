class RomanConverter:
    def convert(self, num):
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        result = ""

        for i in range(len(numbers)):
            times = num // numbers[i]
            result += letters[i] * times
            num = num % numbers[i]

        return result

num = int(input("Enter a number: "))
converter = RomanConverter()
print("Roman numeral is:", converter.convert(num))