#include <stdio.h>
#include <stdlib.h>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

// Function to create a new TreeNode
struct TreeNode* createTreeNode(int val) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->val = val;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Function to trim the binary search tree
struct TreeNode* trimBST(struct TreeNode* root, int low, int high) {
    if (root == NULL) {
        return NULL;
    }

    // If the current node's value is within the range [low, high]
    if (low <= root->val && root->val <= high) {
        root->left = trimBST(root->left, low, high);
        root->right = trimBST(root->right, low, high);
        return root;
    }

    // If the current node's value is less than the low boundary
    if (root->val < low) {
        return trimBST(root->right, low, high);
    }

    // If the current node's value is greater than the high boundary
    return trimBST(root->left, low, high);
}

int main() {
    // Example usage:
    struct TreeNode* root = createTreeNode(3);
    root->left = createTreeNode(0);
    root->right = createTreeNode(4);
    root->left->right = createTreeNode(2);
    root->left->right->left = createTreeNode(1);

    int low = 1, high = 3;
    struct TreeNode* trimmedRoot = trimBST(root, low, high);

    // Normally you would add code here to print the tree and check the result
    // For now, let's just free the memory
    // Note: You'd need to write a function to free the tree nodes recursively
    return 0;
}
