"""first_position_tail = input()
second_position_body = input()
third_position_head = input()

this_list = [third_position_head, second_position_body, first_position_tail]
print(this_list)"""

tail = input()
body = input()
head = input()

this_list = [tail, body, head]
this_list[0], this_list[2] = this_list[2], this_list[0]
print(this_list)
