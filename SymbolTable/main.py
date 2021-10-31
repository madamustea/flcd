from SymbolTable import SymTable

s=SymTable(5)
print(s.insert("a"))
print(s.insert("b"))
print(s.insert("x"))
print(s.insert("a"))
print(s.getSize())


