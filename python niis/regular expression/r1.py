#1.re.match().
import re
result = re.match(r'\d+','123ab56c')
print(result.group())