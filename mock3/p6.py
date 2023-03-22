class C:
    def __init__(self,array):
        self.array = array
    
    def m(self,n):
        self.n = n
        self.count = 0
        for self.arr in self.array:
            if self.arr[0] > 0 and self.arr[1] > 0:
                self.count += 1
        if self.n < self.count:
            return True
        else:
            return False

