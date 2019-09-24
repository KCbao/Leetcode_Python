## 1. Create empty class
```
class Test:
    pass
```

## 2. str vs repr
```
class Test: 
    def __init__(self, a, b): 
        self.a = a 
        self.b = b 
  
    def __repr__(self): 
        return "Test a:%s b:%s" % (self.a, self.b) 
  
    def __str__(self): 
        return "From str method of Test: a is %s," \ 
              "b is %s" % (self.a, self.b) 
  
# Driver Code         
t = Test(1234, 5678) 
print(t) # This calls __str__()  From str method of Test: a is 1234,b is 5678
print([t]) # This calls __repr__() [Test a:1234 b:5678]
```

- if no __repr__ is defined, then default is used
```
print(t): <__main__.Test instance at 0x7fa079da6710>
```