//Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key
// of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

//As a reminder, a binary search tree is a tree that satisfies these constraints:

//The left subtree of a node contains only nodes with keys less than the node's key.
//The right subtree of a node contains only nodes with keys greater than the node's key.
//Both the left and right subtrees must also be binary search trees.

//Example 1:
//Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
//Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

//Example 2:
//Input: root = [0,null,1]
//Output: [1,null,1]

//Example 3:
//Input: root = [1,0,2]
//Output: [3,3,2]

//Example 4:
//Input: root = [3,2,4,1]
//Output: [7,9,4,10]

//Constraints:
//The number of nodes in the tree is in the range [1, 100].
//0 <= Node.val <= 100
//All the values in the tree are unique.
//root is guaranteed to be a valid binary search tree.

// * Definition for a binary tree node.



#include <iostream>
using namespace std;


  struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
  };

class Solution {
public:
    // method to transform a BST to a GST
    TreeNode* bstToGst(TreeNode* root) {
        // traverse BST in reverse - inorder traversal reversed so Right -> Root -> Left
        // reverse gives the keys in decreasing order
        // as traverse keep track of all nodes greater to curr and store sum
        int sum = 0;
        TreeNode* t = bstHelper(root,sum);
        return t;
    }
    TreeNode* bstHelper(TreeNode* curr,int& sum){
        // base case
        if(!curr){
            return curr;
        }

        // visit right 1st
        bstHelper(curr -> right,sum);
        sum = sum + curr -> val;
        curr -> val = sum;
        //cout << curr -> val << endl;
        // visit root 2nd
        //bstHelper(curr,sum);
        // visit left last
        bstHelper(curr -> left,sum);
        return curr;
    }
    void printBst(struct TreeNode* root){
    // inorder traversal
    // RLR
        if(root == NULL) {
            return;
        }

        printBst(root -> left);
        cout << root -> val;
        cout << " " ;
        printBst(root -> right);
        }

    void printBstPre(struct TreeNode* root){
        // preorder traversal
        // RLR
        if(root == NULL) {
            cout << "null ";
            return;
        }
        cout << root -> val;
        cout << " " ;
        printBstPre(root -> left);
        printBstPre(root -> right);
    }

};


int main(){
    //Example 1:
    //Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    //Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
    Solution s;

    TreeNode* root = new TreeNode(4);
    root -> right = new TreeNode(6);
    root -> left = new TreeNode(1);
    root -> left -> right = new TreeNode(2);
    root -> left -> left = new TreeNode(0);
    root -> right -> right = new TreeNode(7);
    root -> right -> left = new TreeNode(5);
    root -> left -> right -> right  = new TreeNode(3);
    root -> right -> right -> right = new TreeNode(8);

    s.printBstPre(root);
    cout << endl;
    TreeNode* t = s.bstToGst(root);
    s.printBstPre(t);

    return 0;
}
