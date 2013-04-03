PyDecrypt
=========

Simple Python decrypter for hashes. Currently MD5 only. Checking is only really efficient currently up to around 5 alpha-numeric characters. 

Installation
------------

Download all files in the repository to one folder. Navigate to the directory in your terminal/command prompt, and then run ```python setup.py install```

You can also install via pip: ```pip install pydecrypt```

Usage 
------------

Call the MD5 Decrypter in your code by using ```pydecrypt.brute_force_md5(value)```, where "value" is your MD5 hash. The module will also return the final value of the key, so you can assign it straight into a variable if you wish.

Example program
-------------
```python
import pydecrypt

value = raw_input("Enter your MD5 hash: ")
pydecrypt.brute_force_md5(value)
```

The other way this module can be used is like this:
```python
import pydecrypt

value = raw_input("Enter your MD5 hash: ")
decrypted_hash = pydecrypt.brute_force_md5(value)
print decrypted_hash
```

This assigns the result of ```pydecrypt.brute_force_md5(value)``` to the variable ```decrypted_hash```, which is printed in the next line.

