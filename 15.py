# Disc #1 has 13 positions; at time=0, it is at position 1.
# Disc #2 has 19 positions; at time=0, it is at position 10.
# Disc #3 has 3 positions; at time=0, it is at position 2.
# Disc #4 has 7 positions; at time=0, it is at position 1.
# Disc #5 has 5 positions; at time=0, it is at position 3.
# Disc #6 has 17 positions; at time=0, it is at position 5.

# For each: (t + id)%size = size-start_pos
t=0
looking_for_part_one = True
while True:
    if (t+1)%13 == 13-1 and \
       (t+2)%19 == 19-10 and \
       (t+3)%3 == 3-2 and \
       (t+4)%7 == 7-1 and \
       (t+5)%5 == 5-3 and \
       (t+6)%17 == 17-5 :
           if looking_for_part_one:
               looking_for_part_one = False
               print(t)
           if (t+7)%11 == 0:
               print(t)
               exit()
    t += 1
