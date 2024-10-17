class A:
    var1 = "Learn"
class B:
    var2 = "Think"
class C(A, B):
    var3 = "Earn"

samp1 = C()
print(samp1.var1)
print(samp1.var2)
print(samp1.var3)