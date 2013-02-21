PyDecrypt
=========

Simple Python decrypter for hashes. Currently MD5 only, and limited to 4 alphabetical characters for fast decryption.
5 alphabetical characters decryption is available, but generating the files will use ~1.5GB of RAM and take a good few minutes. After that, however, the searching for a hash is nearly instant and uses barely any RAM.

Installation
------------

Download all files in the repository to one folder. Navigate to the directory in your terminal/command prompt, and then run ```python setup.py install```

You can also install via pip: ```pip install pydecrypt```

Usage 
------------

Call the MD5 Decrypter in your code by using ```PyDecrypt.MD5Decrypt(value)```, where "value" is your MD5 hash. The module will also return the final value of the key, so you can assign it straight into a variable if you wish.

Example program
-------------
```python
import PyDecrypt

value = raw_input("Enter your MD5 hash: ")
PyDecrypt.MD5Decrypt(value)
```

The other way this module can be used is like this:
```python
import PyDecrypt

value = raw_input("Enter your MD5 hash: ")
decrypted_hash = PyDecrypt.MD5Decrypt(value)
print decrypted_hash
```

This assigns the result of ```PyDecrypt.MD5Decrypt(value)``` to the variable ```decrypted_hash```, which is printed in the next line.

