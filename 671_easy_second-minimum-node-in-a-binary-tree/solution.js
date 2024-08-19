// Definition for a binary tree node.
class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

// Helper function to find the second minimum value
function find(node, root, ans) {
    if (node === null) {
        return;
    }

    if (node.val !== root.val) {
        if (node.val < ans.value) {
            ans.value = node.val;
        }
        return;
    } else {
        find(node.left, root, ans);
        find(node.right, root, ans);
    }
}

// Main function to find the second minimum value in the binary tree
function findSecondMinimumValue(root) {
    let ans = { value: Number.MAX_SAFE_INTEGER };

    find(root, root, ans);

    return ans.value === Number.MAX_SAFE_INTEGER ? -1 : ans.value;
}

// Example usage:
const root = new TreeNode(2, 
    new TreeNode(2), 
    new TreeNode(5, 
        new TreeNode(5), 
        new TreeNode(7)
    )
);

console.log(findSecondMinimumValue(root)); // Output should be 5
