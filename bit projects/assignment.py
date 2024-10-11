from collections import deque
festival_events = ["Music Concert", "Food Festival", "Art Exhibition", "Comedy Show"]
order_queue = deque()
undo_stack = deque()
def display_events():
    print("\nAvailable Festival Events:")
    for i, event in enumerate(festival_events, 1):
        print(f"{i}. {event}")
def book_ticket(event_number, customer_name):
    if event_number < 1 or event_number > len(festival_events):
        print("Invalid event number!")
        return

    event = festival_events[event_number - 1]
    order = (customer_name, event)
    order_queue.append(order)
    undo_stack.append(order)
    print(f"\nBooking confirmed: {customer_name} -> {event}")
def process_order():
    if order_queue:
        order = order_queue.popleft()
        print(f"\nProcessing order for {order[0]}: {order[1]}")
    else:
        print("\nNo orders to process.")

def undo_booking():
    if undo_stack:
        last_booking = undo_stack.pop()
        print(f"\nBooking undone for {last_booking[0]} -> {last_booking[1]}")
        order_queue.remove(last_booking)
    else:
        print("\nNo bookings to undo.")
def main():
    while True:
        print("\n1. Display Festival Events")
        print("2. Book a Ticket")
        print("3. Process Next Order")
        print("4. Undo Last Booking")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            display_events()

        elif choice == "2":
            display_events()
            try:
                event_number = int(input("\nEnter event number to book: "))
                customer_name = input("Enter your name: ")
                book_ticket(event_number, customer_name)
            except ValueError:
                print("Invalid input. Please enter a valid event number.")

        elif choice == "3":
            process_order()

        elif choice == "4":
            undo_booking()

        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

main()