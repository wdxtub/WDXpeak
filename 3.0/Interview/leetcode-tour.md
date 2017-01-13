# Leetcode 思路及个人想法

<!-- MarkdownTOC -->

- Edit Distance
    - Solution
- Multiply Strings
    - Solution
- Remove Linked List Elements
    - Solution

<!-- /MarkdownTOC -->

## Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

+ a) Insert a character
+ b) Delete a character
+ c) Replace a character

### Solution

    public class Solution {
        public int minDistance(String word1, String word2) {
            if (word1 == "" && word2 == ""){
                return 0;
            }
            if (word1.equals("")){
                return word2.length();
            }
            if (word2.equals("")){
                return word1.length();
            }

            int l1 = word1.length();
            int l2 = word2.length();
            int[][] distance = new int[l1+1][l2+2];

            for (int j = 0; j <= l2; j++){
                distance[0][j] = j;
            }

            for (int i = 0; i <= l1; i++){
                distance[i][0] = i;
            }

            for (int i = 1; i <= l1; i++){
                for (int j = 1; j <= l2; j++){
                    if (word1.charAt(i-1) != word2.charAt(j-1)){
                        distance[i][j] = min3(distance[i][j-1], distance[i-1][j], distance[i-1][j-1]) + 1;
                    }
                    else{
                        distance[i][j] = distance[i-1][j-1];
                    }

                }
            }
            return distance[l1][l2];
        }

        public int min3(int d1, int d2, int d3){
            return Math.min(Math.min(d1, d2), d3);
        }
    }

## Multiply Strings

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.

### Solution

    public class Solution {
        public String multiply(String num1, String num2) {
            String n1 = new StringBuilder(num1).reverse().toString();
            String n2 = new StringBuilder(num2).reverse().toString();

            int[] result = new int[n1.length()+n2.length()];
            for(int i=0; i < n1.length(); i++){
                for(int j=0; j < n2.length(); j++){
                    result[i+j] += (n1.charAt(i)-'0') * (n2.charAt(j)-'0');
                }
            }

            StringBuilder sb = new StringBuilder();
            for(int i = 0; i < result.length; i++){
                int digit = result[i]%10;
                int carry = result[i]/10;
                if( i+1 < result.length){
                    result[i+1] += carry;
                }
                sb.insert(0, digit);        // prepend
            }

            while(sb.charAt(0)=='0' && sb.length()>1){
                sb.deleteCharAt(0);
            }
            return sb.toString();
        }
    }

## Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example

    Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
    Return: 1 --> 2 --> 3 --> 4 --> 5

### Solution

    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) { val = x; }
     * }
     */
    public class Solution {
        public ListNode removeElements(ListNode head, int val) {
            ListNode dummy = new ListNode(0);
            ListNode backup = dummy;
            while (head != null){
                if (head.next != null){
                    if (head.val != val){
                        dummy.next = head;
                        dummy = dummy.next;
                        head = head.next;
                    }
                    else {
                        head = head.next;
                    }
                }
                else {
                    if (head.val != val){
                        dummy.next = head;
                        dummy = dummy.next;
                        head = head.next;
                    }
                    else {
                        dummy.next = null;
                        head = head.next;
                    }
                }
            }
            return backup.next;
        }
    }
