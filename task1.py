class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
    
    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def display(self):
        return " -> ".join(map(str, self.to_list())) if self.head else "Empty list"

# функція, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    
    return prev

# функція, сортування злиттям
def merge_sort_linked_list(head):
    if not head or not head.next:
        return head
    
    mid = get_middle(head)
    left = head
    right = mid.next
    mid.next = None
    
    left_sorted = merge_sort_linked_list(left)
    right_sorted = merge_sort_linked_list(right)
    return merge_two_sorted_lists(left_sorted, right_sorted)


def get_middle(head):
    if not head:
        return head
    slow = head
    fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    return prev

# функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список
def merge_two_sorted_lists(list1, list2):
    dummy = ListNode(0)
    current = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
        
    current.next = list1 or list2
    
    return dummy.next


def create_list(arr):
    head = ListNode(arr[0])
    current = head
    
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    
    return head


def print_list(head):
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    return " -> ".join(result) if result else "Empty list"


# =================================================================================

list = create_list([1, 2, 3, 4, 5])
reversed_list = reverse_linked_list(list)
print("реверс", print_list(reversed_list))

list1 = create_list([5, 2, 1, 3, 4, 7])
print("\nСортування дано", print_list(list1))
sorted_list = merge_sort_linked_list(list1)
print("отримали", print_list(sorted_list))




list2 = create_list([1, 3, 5, 7])
list3 = create_list([2, 4, 6, 8, 10])
print("\nсписок1", print_list(list2))
print("список2", print_list(list3))

merged_list = merge_two_sorted_lists(list2, list3)
print("merged_list", print_list(merged_list))
