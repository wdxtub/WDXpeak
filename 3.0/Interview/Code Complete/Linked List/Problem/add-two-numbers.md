# Add Two Numbers

出处

Given two linked lists, each element of the lists is a integer. Write a function to return a new list, which is the “sum” of the given two lists.

+ Part a. Given input (7->1->6) + (5->9->2), output 2->1->9. 
+ Part b. Given input (6->1->7) + (2->9->5), output 9->1->2.

## Solution

对于a，靠前节点的解不依赖靠后节点，因此顺序遍历求解即可。对于b，靠前节点的解依赖于靠后节点(进位)，因此必须用递归或栈处理。并且，子问题返回的结果，可以是一个自定义的结构(进位 + sub-list)。当然，对于问题b，也可以通过逆向列表之后再用a的解法求解。同时，注意到该题还是处理两个链表的问题，所以可以先处理常规情况(两个链表都有剩下节点)，再处理边界情况(其中一个链表已经遍历完毕)。

## Complexity

时间复杂度 O(n)

## Code

For part a

```java
Node addList(Node head1, Node head2){
	Node head = new Node(-1);
   int num1 = 0, count1 = 0;
   int num2 = 0, count2 = 0;
   int result = 0;

   while (head1 != null){
       num1 += head1.data * Math.pow(10,count1);
       count1++;
       head1 = head1.next;
   }

   while (head2 != null){
       num2 += head2.data * Math.pow(10,count2);
       count2++;
       head2 = head2.next;
   }
   result = num1 + num2;

   Node cur = head;

   while(result > 0){
       cur.next = new Node(result % 10);
       cur = cur.next;
       result /= 10;
   }

   return head.next;
}
```

---

For part b

```java
Node addList(Node head1, Node head2){
   Node head = new Node(-1);
   int num1 = 0, count1 = 0;
   int num2 = 0, count2 = 0;
   int result = 0;

   while (head1 != null){
       num1 = num1 * 10 + head1.data;
       count1++;
       head1 = head1.next;
   }

   while (head2 != null){
       num2 = num2 * 10 + head2.data;
       count2++;
       head2 = head2.next;
   }
   result = num1 + num2;

   Node cur = head;

   while(result > 0){
       Node temp = new Node(result % 10);
       temp.next = cur.next;
       cur.next = temp;
       result /= 10;
   }

   return head.next;
}
```

---
 
cpp version

```cpp
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *dummy = new ListNode(0), *p = dummy;
        int carry = 0;
        while(l1 || l2 || carry) {
            if(l1) {
                carry+=l1->val;
                l1 = l1->next;
            }
            if(l2) {
                carry+=l2->val;
                l2 = l2->next;
            }
            p->next = new ListNode(carry%10);
            carry /= 10;
            p = p->next;
        }
        return dummy->next;
    }
};
```


