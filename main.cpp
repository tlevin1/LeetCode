#include <iostream>

#include<bits/stdc++.h>

using namespace std;
// Program to check if BST is valid BST
// BST Properties:
// left subtree  < root
// right subtree > root
// both left and right subtrees must be valid BSTs

// time complexity for this implementation = O(n) (We traverse every node once)
class node
{
public:
    int data;
    node* left;
    node* right;

    /* Constructor that allocates
    a new node with the given data
    and NULL left and right pointers. */
    node(int data)
    {
        this->data = data;
        this->left = NULL;
        this->right = NULL;
    }
};

int isBSTUtil(node* node, int min, int max);

int isBST(node* node)
{
    return(isBSTUtil(node, INT_MIN, INT_MAX));
}
int isBSTUtil(node* node, int min, int max)
{
    // Method:
    // using BST Util we can traverse tree and keep track of min and max
    // we can visit every node once

    // empty bst (considered still valid)
    if(node == NULL){
        return 1;
    }
    // checking min/max constraint for BSTs
    if(node -> data < min || node -> data > max){
        // returns false
        return 0;
    }
    // recursive function call to check subtrees recursively
    return isBSTUtil(node -> left,min,node -> data -1) && isBSTUtil(node -> right,node -> data + 1,max);

}
int main() {

    node *root = new node(1);
    root->left = new node(2);
    root->right = new node(5);
    root->left->left = new node(1);
    root->left->right = new node(3);

    if(isBST(root))
        cout<<"Is BST";
    else
        cout<<"Not a BST";

    return 0;
}
