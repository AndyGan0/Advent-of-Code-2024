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
    






all_monkeys_sequence_to_prices = {}

for s in secret_numbers:
    prices = [s%10]
    change_seq = []

    current_monkey_sequence_to_prices = {}

    for i in range(3):    
        s = produce_next_secret_number(s)
        prices.append(s%10)
        change_seq.append(prices[-1] - prices[-2])


    for i in range(3,2000):
        s = produce_next_secret_number(s)
        prices.append(s%10)
        change_seq.append(prices[-1] - prices[-2])

        sequence_to_get = (change_seq[-4], change_seq[-3], change_seq[-2], change_seq[-1])

        if sequence_to_get not in current_monkey_sequence_to_prices:
            current_monkey_sequence_to_prices[sequence_to_get] = prices[-1]

    
    for seq in current_monkey_sequence_to_prices:
        if seq in all_monkeys_sequence_to_prices:
            all_monkeys_sequence_to_prices[seq] += current_monkey_sequence_to_prices[seq]

        else:
            all_monkeys_sequence_to_prices[seq] = current_monkey_sequence_to_prices[seq]

        




max_value_sequence = max(all_monkeys_sequence_to_prices, key= all_monkeys_sequence_to_prices.get)
print(all_monkeys_sequence_to_prices[max_value_sequence])