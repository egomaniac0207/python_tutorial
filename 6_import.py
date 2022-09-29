import sys
from mypackages import import_ref as ref

print(sys.platform)
print(ref.call1(1,3))
print(ref.call2(1,3))