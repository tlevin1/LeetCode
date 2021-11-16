#include <iostream>

/*Given the head of a linked list and an integer val,
 remove all the nodes of the linked list that has Node.val == val, and return the new head.
Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:

Input: head = [], val = 1
Output: []
Example 3:

Input: head = [7,7,7,7], val = 7
Output: []


Constraints:

The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
 */

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    // time complexity : O(N)
    ListNode* removeElements(ListNode* head, int val) {
        ListNode* curr = head;
        // sentinal node to ensure list is never empty/headless, does not contain any data
        ListNode* sentinal = new ListNode(0);
        sentinal -> next = head;
        ListNode *prev = sentinal;
        // node to delete
        ListNode *temp = nullptr;

        //traverse list to find element to delete
        while(curr != nullptr) {
            if (curr->val == val) {
                // update next
                prev->next = curr->next;
                temp = curr;
            } else {
                prev = curr;
            }
            curr = curr->next;
            if (temp != nullptr) {
                delete temp;
                temp = nullptr;
            }
        }
            // return head of modified list
            ListNode *ret = sentinal -> next;
            delete sentinal;
            return ret;
        }
};

int main() {
    //Input: head = [1,2,6,3,4,5,6], val = 6
    //Output: [1,2,3,4,5]
    Solution s;
    ListNode *head = new ListNode(1);
    std::cout << head -> val << std::endl;
    head -> next = new ListNode(2);
    head = s.removeElements(head,1);
    std::cout << head -> val << std::endl;
    return 0;
}



