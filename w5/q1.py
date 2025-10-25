# (1) Explain the various ways of importing module contents with examples.
# Python offers several methods to import module contents:
# - Import entire module: `import math` (access as `math.sqrt(16)`)
# - Import specific items: `from math import sqrt, pi` (use directly: `sqrt(16)`)
# - Import all items: `from math import *` (discouraged due to namespace issues)
# - Import with alias: `import math as m` (use as `m.sqrt(16)`)
# - Import specific items with aliases: `from math import sqrt as square_root` (use as `square_root(16)`)
