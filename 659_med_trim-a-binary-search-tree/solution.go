package main

import "fmt"

// TreeNode represents a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// trimBST trims the binary search tree based on the given range [low, high].
func trimBST(root *TreeNode, low int, high int) *TreeNode {
	if root == nil {
		return nil
	}

	// If the current node's value is within the range [low, high]
	if low <= root.Val && root.Val <= high {
		root.Left = trimBST(root.Left, low, high)
		root.Right = trimBST(root.Right, low, high)
		return root
	}

	// If the current node's value is less than the low boundary
	if root.Val < low {
		return trimBST(root.Right, low, high)
	}

	// If the current node's value is greater than the high boundary
	return trimBST(root.Left, low, high)
}

func main() {
	// Example usage:
	root := &TreeNode{Val: 3}
	root.Left = &TreeNode{Val: 0}
	root.Right = &TreeNode{Val: 4}
	root.Left.Right = &TreeNode{Val: 2}
	root.Left.Right.Left = &TreeNode{Val: 1}

	low := 1
	high := 3
	trimmedRoot := trimBST(root, low, high)

	// Print the trimmed tree (For testing purpose)
	printTree(trimmedRoot)
}

// Helper function to print the tree (In-order traversal)
func printTree(node *TreeNode) {
	if node == nil {
		return
	}
	printTree(node.Left)
	fmt.Println(node.Val)
	printTree(node.Right)
}
