import string
import random
import uuid

characters = string.ascii_letters + string.digits

# To check whether duplicate code is been generated for 1 Crore iterations
code = {}
for _ in range(100000000):
    string_val = ''.join(random.choice(characters) for _ in range(8))
    if code.get(string_val):
        print(string_val)
        # break
    code[string_val] = 1

# code = {}
# for _ in range(10000000):
#     string_val = uuid.uuid4()
#     if code.get(string_val):
#         print(string_val)
#         # break
#     code[string_val] = 1