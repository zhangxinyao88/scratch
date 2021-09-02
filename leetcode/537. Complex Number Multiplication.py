
# Two way of sending variable into String
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))
        # both will work for String
        #return '%d+%di' % (a*c-b*d, b*c+a*d)
        return f'{a*c-b*d}+{b*c+a*d}i'
