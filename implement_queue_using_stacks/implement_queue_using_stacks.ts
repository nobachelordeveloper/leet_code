class MyQueue {
  stack: any[];
  constructor() {
    this.stack = [];
  }

  push(x: number): void {
    this.stack.push(x);
  }

  pop(): number {
    return this.stack.shift();
    //const [top,...rest] = this.queue
    //this.queue = rest
    //return top
  }

  peek(): number {
    return this.stack[0];
  }

  empty(): boolean {
    return this.stack.length === 0;
  }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */
