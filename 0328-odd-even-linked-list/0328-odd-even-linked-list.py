class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        init_Odd_node = ListNode()
        odd_node = init_Odd_node

        init_even_node = ListNode()
        even_node = init_even_node
        is_Odd = True

        end_of_odd_node = ListNode()
        while head is not None:
            # 홀수 일떄
            if is_Odd:
                next_val = head.val
                next_node = head.next
                odd_node.next = ListNode(next_val, next_node)
                odd_node = odd_node.next
                odd_node.next = None
                end_of_odd_node = odd_node
                head = head.next
                is_Odd = False

            # 짝수 일떄
            else :
                next_val = head.val
                next_node = head.next
                even_node.next = ListNode(next_val, next_node)
                even_node = even_node.next
                even_node.next = None
                head = head.next
                is_Odd = True


        end_of_odd_node.next = init_even_node.next

        return init_Odd_node.next
