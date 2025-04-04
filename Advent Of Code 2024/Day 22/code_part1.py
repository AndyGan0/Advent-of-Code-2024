import math



# Load the grid
filename = "Day 22\input.txt"
with open(filename, 'r') as file:
    secret_numbers = [line for line in file]
secret_numbers = [x[:-1] if x[-1] == '\n' else x for x in secret_numbers ]
secret_numbers = [int(x.strip()) for x in secret_numbers ]






def produce_next_secret_number(secret_number):

    def mix(a,b):
        return a^ b
    
    def prune(a):
        return a % 16777216

    secret_number = mix(secret_number, secret_number * 64)
    secret_number = prune(secret_number)

    secret_number = mix(secret_number, math.floor( secret_number / 32))
    secret_number = prune(secret_number)

    secret_number = mix(secret_number, secret_number * 2048)
    secret_number = prune(secret_number)

    return secret_number
    


all_secret_number = []
for s in secret_numbers:
    for i in range(2000):        
        s = produce_next_secret_number(s)    
    all_secret_number.append(s)

        


sum = sum(all_secret_number)
print(sum)