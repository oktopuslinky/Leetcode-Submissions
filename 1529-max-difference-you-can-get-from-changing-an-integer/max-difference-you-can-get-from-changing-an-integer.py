class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = list(str(num))
        a = num[:]
        b = num[:]
        
        digit_to_change_a, digit_to_change_b = None, None
        for digit in a:
            if digit != '9':
                digit_to_change_a = digit
                break
        
        for digit in b:
            if digit != '1' and digit != '0':
                digit_to_change_b = digit
                break

        if digit_to_change_b == num[0]:
            new_b_digit = '1'
        else:
            new_b_digit = '0'

        for i, digit in enumerate(num):
            if digit_to_change_a and digit == digit_to_change_a:
                a[i] = '9'
            if digit_to_change_b and digit == digit_to_change_b:
                b[i] = new_b_digit
        
        return int("".join(a)) - int("".join(b))