import re
txt = "The ra169in in Sp4a95872i6n"
X = re.findall("[0-9]*",txt)
print(X)

import re
txt = "The ra169in in Sp4a95872i6n"
X = re.findall("[0-9]?",txt)
print(X)