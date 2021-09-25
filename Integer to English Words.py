#https://leetcode.com/problems/integer-to-english-words/
class Solution:
    def numberToWords(self, num: int) -> str:
        SingleDigit = ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
        DoubleDigit = ("Eleven", "Twelve", "Thieteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
        ZeroDigit = ("Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
        
        words= []
        num = list(str(num))
        
        def SingleDigitFun():
            if num[0] == "0":
                del num[0]
            else:
                words.append(SingleDigit[(int(num[0]))-1])
                if len(num) == 10:
                    words.append("Billion")
                    del num[0]
                elif len(num) == 9 or 6 or 3:
                    words.append("Hundred")
                    del num[0]
                elif len(num) == 7:
                    words.append("Million")
                    del num[0]
                elif len(num) == 4:
                    words.append("Thousand")
                    del num[0]
                    
        def DoubleDigitFun():
            if num[0] == "0":
                del num[0]
            else:
                if num[0] == 1:
                    if num[1] == 0:
                        words.append("Ten")
                        del num[0]
                        del num[0]
                    else:
                        words.append(DoubleDigit[int(num[1])-1])
                        del num[0]
                        del num[0]
                else:
                    words.append(ZeroDigit[int(num[0])-2])
                    words.append(SingleDigit[int(num[0])])
                    if len(num) == 8:
                        words.append("Million")
                    elif len(num) == 5:
                        words.append("Thousand")
                    # elif len(num) == 2:
                    #     words.append("Hundred")
                    del num[0]
                    del num[0]
        
        if len(num) == 10:
            SingleDigitFun()
        if len(num) == 9:
            SingleDigitFun()
        if len(num) == 8:
            DoubleDigitFun()
            
        if len(num) == 7:
            SingleDigitFun()
        if len(num) == 6:
            SingleDigitFun()
        if len(num) == 5:
            DoubleDigitFun()
            
        if len(num) == 4:
            SingleDigitFun()
        if len(num) == 3:
            SingleDigitFun()
        if len(num) == 2:
            DoubleDigitFun()
            
        if len(num) == 1:
            SingleDigitFun()
        
        return " ".join(words)
        
