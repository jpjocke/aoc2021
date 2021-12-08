from typing import List


class Serie:
    numbers: List[str]
    result: List[str]

    def __init__(self, numbers: List[str], result: List[str]):
        self.numbers = numbers
        self.result = result

    def count_problem_one(self) -> int:
        total = 0
        for s in self.result:
            length = len(s)
            if length == 2 or length == 3 or length == 4 or length == 7:
                total += 1
        return total

    def parse_result(self) -> int:
        num_to_letter = self.__parse_all_numbers()

        letter_to_num = {}
        for key in num_to_letter:
            letter_to_num[num_to_letter[key]] = key

        return self.__extract_result(letter_to_num)

    def __parse_all_numbers(self) -> {}:
        num_to_letter = {}
        num_to_letter[1] = self.__find_by_length(2)
        num_to_letter[4] = self.__find_by_length(4)
        num_to_letter[7] = self.__find_by_length(3)
        num_to_letter[8] = self.__find_by_length(7)
        num_to_letter[3] = self.__find_three(num_to_letter[7])
        num_to_letter[9] = self.__find_nine(num_to_letter[3], num_to_letter[4])
        lower_left = self.__find_lower_left(num_to_letter[8], num_to_letter[9])
        num_to_letter[2] = self.__find_two(lower_left)
        num_to_letter[5] = self.__find_five(num_to_letter[2], num_to_letter[3])
        num_to_letter[6] = self.__find_six(num_to_letter[5], lower_left)
        num_to_letter[0] = self.__find_zero(num_to_letter[6], num_to_letter[9])
        return num_to_letter

    def __extract_result(self, letter_to_num):
        result = ''
        for number in self.result:
            for key in letter_to_num:
                # result letters are scrambled
                if self.__same_letter(number, key):
                    result += str(letter_to_num[key])
                    break
        return int(result)

    def __find_by_length(self, length: int) -> str:
        for i in self.numbers:
            if len(i) == length:
                return i

    def __find_zero(self, six: str, nine: str) -> str:
        for i in self.numbers:
            if len(i) == 6:
                if six != i and nine != i:
                    return i

    def __find_two(self, lower_left: str) -> str:
        for i in self.numbers:
            if len(i) == 5:
                if lower_left in i:
                    return i

    def __find_three(self, seven: str) -> str:
        for i in self.numbers:
            if len(i) == 5:
                if self.__letter1_in_letter2(seven, i):
                    return i

    def __find_five(self, two: str, three: str) -> str:
        for i in self.numbers:
            if len(i) == 5:
                if i != two and i != three:
                    return i

    def __find_six(self, five: str, lower_left: str) -> str:
        for i in self.numbers:
            if len(i) == 6:
                if lower_left in i:
                    if self.__letter1_in_letter2(five, i):
                        return i

    def __find_nine(self, three: str, four: str) -> str:
        for i in self.numbers:
            if len(i) == 6:
                if self.__letter1_in_letter2(three, i) and self.__letter1_in_letter2(four, i):
                    return i

    def __letter1_in_letter2(self, letter1: str, letter2: str) -> bool:
        has_all = True
        for letter in letter1:
            if letter not in letter2:
                has_all = False
                break
        return has_all

    def __same_letter(self, letter1: str, letter2: str) -> bool:
        if len(letter1) != len(letter2):
            return False
        return self.__letter1_in_letter2(letter1, letter2)

    def __find_lower_left(self, eight: str, nine: str) -> str:
        for letter in eight:
            if letter not in nine:
                return letter

    def __str__(self):
        return 'series: ' + str(self.numbers) + ', result: ' + str(self.result)
