def iq_test(numbers):

   
    num = numbers.split()
    n_odd = 0
    n_even = 0
    
    # finding the unique number out
    
    for n in num:
        if int(n)%2 == 0:
            n_even += 1
        else:
            n_odd += 1
            
       # getting the index of odd num when others are even
        for m in num:
            if n_even > 1:
                if int(m)%2 != 0:
                    h = num.index(m)
                    return h+1
        # getting the index of even num when others are odd
            elif n_odd > 1:
                if int(m)%2 == 0:
                    r = num.index(m)
                    return r+1
