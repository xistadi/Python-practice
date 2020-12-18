def some(*args):
    result = 1
  
    for a in args:
        result *= a
        num = len(args)
    return result, num

a = [int(s) for s in input("Введите число:\n").split(',')] 
print(some(*a))