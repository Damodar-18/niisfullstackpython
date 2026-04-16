#4. re.sub().
import re
result = re.sub(r'\d+','X','abc123def456')
print(result)



import re
result = re.sub(r'\d','X','abc123def456')
print(result)


import re
result = re.sub(r'\d*','X','abc123def456')
print(result)

import re
result = re.sub(r'\D+','X','abc123def456')
print(result)

import re
result = re.sub(r'\D','X','abc123def456')
print(result)