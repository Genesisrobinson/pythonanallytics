class abc:
    common=10
    def __init__(self):
        self.value=0
    def calc(self,temp):
        self.value=temp
        return self.value+1

x =abc()
y =abc()
ret=x.calc(5)
ret1=x.calc(15)
print(x.common)
print(y.common)
print(ret)
print(ret1)


