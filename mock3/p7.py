class C:
    @staticmethod
    def m(n):
        count = 0
        x = str(n)
        for i in range(1,len(x)):
            if x[i-1] <= x[i]:
                count += 1
        if count != len(x)-1:
            return False
        else:
            return True
C.m(123)