package main

import "fmt"

// 定义单链表节点
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	n1 := 0
	if l1 != nil {
		n1 = l1.Val
	}

	n2 := 0
	if l2 != nil {
		n2 = l2.Val
	}

	head := &ListNode{Val: (n1 + n2) % 10}
	carry := (n1 + n2) / 10

	l1 = l1.Next
	l2 = l2.Next

	p := head
	for l1 != nil || l2 != nil || carry != 0 {
		n1 = 0
		if l1 != nil {
			n1 = l1.Val
		}

		n2 = 0
		if l2 != nil {
			n2 = l2.Val
		}

		val := n1 + n2 + carry
		if val > 9 {
			carry = val / 10
			val = val % 10
		} else {
			carry = 0
		}

		p.Next = &ListNode{Val: val}
		p = p.Next

		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
	}

	return head
}

func main() {
	// 示例用法
	l1 := &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 3}}}
	l2 := &ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4}}}

	result := addTwoNumbers(l1, l2)

	// 打印结果
	for result != nil {
		fmt.Printf("%d ", result.Val)
		result = result.Next
	}
}
