package implement_queue_using_stacks;

import java.util.EmptyStackException;
import java.util.Stack;

class MyQueue {
    Stack<Integer> stack;

    public MyQueue() {
        this.stack = new Stack<Integer>();
    }

    public void push(int x) {
        this.stack.push(x);
    }

    public int pop() {
        if (this.stack.isEmpty()) {
            throw new EmptyStackException();
        }
        Stack<Integer> tempStack = new Stack<>();
        while (stack.size() > 1) {
            tempStack.push(stack.pop());
        }
        int firstNumber = stack.pop();
        while (!tempStack.isEmpty()) {
            stack.push(tempStack.pop());
        }
        return firstNumber;
    }

    public int peek() {
        return this.stack.get(0);
    }

    public boolean empty() {
        return this.stack.size() == 0;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */