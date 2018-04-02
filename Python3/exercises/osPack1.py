"""
Prints out the number of digits in PI. Definied by
the DIGITS env variable or defaults to 10.
"""

#!/usr/bin/env python3.6

from math import pi
from os import getenv

digits = getenv('DIGITS', 10)

print(str(digits) + " of Pi will now print:")
print("%.*f" % (int(digits), pi))
