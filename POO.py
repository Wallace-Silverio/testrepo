class CountingClicker:
    def _init_ (self, count=0):
        self.count=count
        clicker1=CountingClicker()
        clicker2=CountingClicker(100)
        clicker3=CountingClicker(count=100)

    def _repr_(self):
        return f"CountingClicker(count={self.count})"
    def click(self, num_times=1):
        """Click the clicker some number of times"""
        self.count += num_times
    def read(self):
        return self.count
    def reset(self):
        self.count=0


clicker=CountingClicker()
assert clicker.read()==0
clicker.click()
clicker.click()
assert clicker.read()==2


