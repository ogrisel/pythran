#from http://rosettacode.org/wiki/Happy_numbers#Python
def happy(n):
    past = set()			
    while n <> 1:
        n = sum(int(i)**2 for i in str(n))
        if n in past:
            return False
        past.add(n)
    return True

def test():
    return [x for x in xrange(500) if happy(x)][:8]
