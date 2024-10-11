queue = []
emergency_stack = [] 
call_outcomes = [] 

def add_ticket(ticket_id, customer_name, issue, priority):
    ticket = {
        'TicketID': ticket_id,
        'CustomerName': customer_name,
        'Issue': issue,
        'Priority': priority
    }
    
    if priority == 1:
        emergency_stack.append(ticket)
    else:
        queue.append(ticket)

def process_next_call():
    if emergency_stack:
        current_call = emergency_stack.pop()
    elif queue:
        current_call = queue.pop(0)
    else:
        return "No calls to process."

    outcome = f"Processed call from {current_call['CustomerName']} who has {current_call['TicketID']} as ID about {current_call['Issue']}"
    call_outcomes.append(outcome)
    return outcome

def show_queue():
    return queue

def show_emergency_stack():
    return emergency_stack

def show_outcomes():
    return call_outcomes


add_ticket(901, "Mary Jones", "Internet Down", 1)
add_ticket(902, "Peter Lee", "Slow Speed", 2)
add_ticket(900, "b r", "Internet Down", 1)
add_ticket(903, "okj c", "Slow Speed", 1)
add_ticket(904, "efw Jones", "Internet Down", 1)
add_ticket(905, "yeww Lee", "Slow Speed", 1)
add_ticket(906, "vewqw Jones", "Internet Down", 1)
add_ticket(907, "rgerfw Lee", "Slow Speed", 2)
add_ticket(908, "vew Jones", "Internet Down", 2)
add_ticket(909, "htrre Lee", "Slow Speed", 2)
add_ticket(800, "efwe Jones", "Internet Down", 1)
add_ticket(700, "ewfge Lee", "Slow Speed", 2)



print(process_next_call()) 
print(process_next_call())
print(process_next_call()) 
print(process_next_call())
print(process_next_call()) 
print(process_next_call())
print(process_next_call()) 
print(process_next_call())
print(process_next_call()) 
print(process_next_call())
print(process_next_call()) 
print(process_next_call())


print("Remaining Queue:", show_queue())
print("Emergency Stack:", show_emergency_stack())

print("Call Outcomes:", show_outcomes())
