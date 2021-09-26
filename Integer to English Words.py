class Solution:
    def numberToWords(self, num: int) -> str:
        SingleDigit = ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
        DoubleDigit = ("Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
        ZeroDigit = ("Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
        
        words= []
        num = list(str(num))
        if num[0] == "0": return "Zero"
        
        def SingleDigitFun():
            while num[0] == "0":
                del num[0]
                if num == []:
                    break
            else:
                if len(num) in (10, 9, 7, 6, 4, 3, 1):
                    words.append(SingleDigit[int(num[0])-1])
                    del num[0]
                    if len(num) == 9:
                        words.append("Billion")
                    elif len(num) == 8:
                        words.append("Hundred")
                        if num[0:2] == ["0","0"]:
                            words.append("Million")
                    elif len(num) == 6:
                        words.append("Million")
                    elif len(num) == 5:
                        words.append("Hundred")
                        if num[0:2] == ["0","0"]:
                            words.append("Thousand")
                    elif len(num) == 3:
                        words.append("Thousand")
                    elif len(num) == 2:
                        words.append("Hundred")
                    
        def DoubleDigitFun():
            while num[0] == "0":
                if num != []:
                    del num[0]
                if num == [] or len(num) <= 1:
                    break
            else:
                if num[0] == "1":
                    if num[1] == "0" and len(num) in (8, 5, 2):
                        words.append("Ten")
                        del num[0]
                        del num[0]
                        if len(num) == 6:
                            words.append("Million")
                        elif len(num) == 3:
                            words.append("Thousand")
                    else:
                        if len(num) in (5,8,2):
                            words.append(DoubleDigit[int(num[1])-1])
                        if len(num) == 8:
                            words.append("Million")
                            del num[0]
                            del num[0]
                        elif len(num) == 5:
                            words.append("Thousand")
                            del num[0]
                            del num[0]
                else:
                    if len(num) in (8, 5, 2):
                        words.append(ZeroDigit[int(num[0])-2])
                        if num[1] != "0":
                            words.append(SingleDigit[int(num[1])-1])
                        if len(num) == 8:
                            words.append("Million")
                        if len(num) == 5:
                            words.append("Thousand")
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
    
