# MRO - Method Resolution Order

class A(): 
    pass

class B(A): 
    pass

class C(B): 
    pass

class D(C, B): 
    pass


# Check how the pyton will route through the multiple inheritances...
print(D.mro())
print(D.__mro__)










