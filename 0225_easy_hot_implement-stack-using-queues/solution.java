import java.util.LinkedList;
import java.util.Queue;

class MyStack {
    Queue<Integer> mainQueue;
    Queue<Integer> tempQueue;

    public MyStack() {
        this.mainQueue = new LinkedList<>();
        this.tempQueue = new LinkedList<>();
    }
    
    public void push(int x) {
        this.mainQueue.offer(x);
    }
    
    public int pop() {
        int size = this.mainQueue.size();
        for( int i = 0; i < size - 1; i++) {
            this.tempQueue.offer(this.mainQueue.poll());
        }

        int result = this.mainQueue.poll();

        Queue<Integer> t = this.mainQueue;
        this.mainQueue = this.tempQueue;
        this.tempQueue = t;

        return result;
        
    }
    
    public int top() {
        int size = this.mainQueue.size();
        for( int i = 0; i < size - 1; i++) {
            this.tempQueue.offer(this.mainQueue.poll());
        }

        int result = this.mainQueue.peek();

        this.tempQueue.offer(this.mainQueue.poll());

        Queue<Integer> t = this.mainQueue;
        this.mainQueue = this.tempQueue;
        this.tempQueue = t;

        return result;
    }
    
    public boolean empty() {
        return this.mainQueue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */