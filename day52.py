#Write a program to find the intersection point of two linked lists.
print ("\nWilson - Day 52 of #100DaysOfCode\n") 
print("\nprogram to find the intersection point of two linked lists\n")

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_intersection(head1, head2):
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    length1 = get_length(head1)
    length2 = get_length(head2)

    length_diff = abs(length1 - length2)

    longer_list = head1 if length1 > length2 else head2
    shorter_list = head1 if length1 <= length2 else head2

    for _ in range(length_diff):
        longer_list = longer_list.next

    while longer_list and shorter_list:
        if longer_list == shorter_list:
            return longer_list

        longer_list = longer_list.next
        shorter_list = shorter_list.next

    return None

head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

head2 = ListNode(7)
head2.next = ListNode(8)
head2.next.next = head1.next.next.next

intersection_point = find_intersection(head1, head2)

if intersection_point:
    print("intersection point value:", intersection_point.value)
else:
    print("no intersection point found.")
