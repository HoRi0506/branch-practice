# Get integer from user
user_num = int(input('Hello, there! Enter som positive integer: '))

# Print user_num for debugging
print(user_num)

# Iteration
for i in range(1, user_num+1):
    if i%3==0:
        print('fizz')
    else:
        print(f'{i}')
