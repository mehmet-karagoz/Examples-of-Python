def is_prime(num):
    if num <= 1:
        return False
    else:
        for x in range(2,num):
            if (num % x) == 0:
                return False
        else:
            return True
