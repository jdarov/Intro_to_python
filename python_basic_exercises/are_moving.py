speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)  #true
print(is_moving)  #we DO need paranthesis , otherwise it moves the order over to AND first