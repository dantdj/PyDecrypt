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

The available parameters for the `brute_force_md5` function are as such: `(value[,minimum_char][,log])`.

`value` = MD5 hash to be decrypted.

`minimum_char` = Optional, used to denote the minimum length of the decrypted hash if such a guess can be made. Aims to reduce generation of unnecessary combinations. Set to 1 by default.

`log` = Optional, used to determine whether the module logs its output to the terminal/command prompt window. Set to False by default.  

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

