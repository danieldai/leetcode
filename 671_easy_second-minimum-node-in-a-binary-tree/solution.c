#include <stdio.h>
#include <limits.h>

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

long ans;

// Helper function to find the second minimum value
void find(struct TreeNode* node, struct TreeNode* root) {
    if (node == NULL) {
        return;
    }

    if (node->val != root->val) {
        if (node->val < ans) {
            ans = node->val;
        }
        return;
    } else {
        find(node->left, root);
        find(node->right, root);
    }
}

// Main function to find the second minimum value in the binary tree
int findSecondMinimumValue(struct TreeNode* root) {
    ans = LONG_MAX;

    find(root, root);

    if (ans == LONG_MAX) {
        return -1;
    } else {
        return (int)ans;
    }
}

int main() {
    // Example usage:
    struct TreeNode* root = createTreeNode(2);
    root->left = createTreeNode(2);
    root->right = createTreeNode(5);
    root->right->left = createTreeNode(5);
    root->right->right = createTreeNode(7);

    int result = findSecondMinimumValue(root);
    printf("Second minimum value: %d\n", result); // Output should be 5

    return 0;
}
