import random
import string

def main():
    try:
        size = 25000
        size2 = 16
        a = ''.join(random.choices(string.ascii_letters, k=1))
        rstring = ''.join(random.choices(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=size))
        while True:
            rstring = rstring.join(random.choices(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=size))
            if len(rstring) >= 25000000:
                break
            else:
                pass
        f = open(f'{a.join(random.choices(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation, k=size2))}.bit', "a")
        f.write(rstring)
        #main()
    except:
        pass

main()
