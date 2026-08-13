 #Scope & Global keyword


total_seats_booked=0 #global variable



def book_seat(n:int):
    global total_seats_booked
    total_seats_booked += n
    print(f"Booked {n} seats"
          f"Total number of seats booked so far is : {total_seats_booked}")

def reset_booking():
    global total_seats_booked
    total_seats_booked=0
    print("Booking has been sucessfully reset\n")


book_seat(5)
book_seat(3)
reset_booking()
book_seat(2)