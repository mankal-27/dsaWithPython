class Solution:
    def classify_sign(self, n):
        if(n > 0):
            return "Positive"
        elif (n < 0):
            return "Negative"
        else:
            return "Zero"
