#3. re.findall().
import re
result = re.findall(r'\d+','abc123def456')
print(result)



import re
result = re.findall(r'\D+','abc123def456')
print(result)