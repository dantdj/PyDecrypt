import hashlib
import itertools
import string

 
def brute_force_md5(target_hash, minimum_char=1, log=True):

    for i in range(minimum_char, 6):
        product = itertools.product(string.ascii_lowercase + string.digits, repeat=i)
        char_space = itertools.imap(''.join, product)
        if log:
            print
            print "Beginning strings of length %d..." % i
 
        for combination in char_space:
            if hashlib.md5(combination).hexdigest() == target_hash:
                if log:
                    print "Found hash at %s" % combination
                return combination
 
        if log:
            print "...And searched. No result found."
  
if __name__ == "__main__":
    print brute_force_md5(raw_input("md5 to search for: "))
