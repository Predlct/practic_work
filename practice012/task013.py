

tickets = input('Enter tickets-number:\n').split()
quantity = 0

for ticket in tickets:
    quantity += 1
    half_t = len(ticket) // 2
    if len(ticket) % 2 == 0:
        if sum([int(i) for i in ticket[:half_t]]) == sum([int(i) for i in ticket[half_t:]]):
            print(quantity)

