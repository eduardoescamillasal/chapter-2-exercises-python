from math_utils import isprime
def test_isprime():
  assert(isprime(3) == True)
  assert(isprime(4) == False)
  assert(isprime(10) == False)
  assert(isprime(23) == True)