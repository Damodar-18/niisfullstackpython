#7.  use txt.
import re
txt = "The rain in spain"
X = re.findall("[a-d]",txt)
print(X)

# using findall() function.
import re
txt = "The rain in Spain"
X = re.findall("[^a-z]",txt)
print(X)


import re
txt = "The rain in Spain"
X = re.findall("[^a-zA-Z]",txt)
print(X)


import re
txt = "The ra16283in in Sp4a9in"
X = re.findall("[0-9]",txt)
print(X)

import re
txt = "The ra16283in in Sp4a9i6n"
X = re.findall("[0-9][a-z]",txt)
print(X)


import re
txt = "The ra169in in Sp4a95872in"
X = re.findall("[0-9][0-9]",txt)
print(X)


import re
txt = "The ra169in in Sp4a95872in"
X = re.findall("[0-9]{3}",txt)
print(X)

import re
txt = "The ra169in in Sp4a95872i6n"
X = re.findall("[0-9]+",txt)
print(X)