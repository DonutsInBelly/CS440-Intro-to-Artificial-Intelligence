package Assign1;

import java.util.NoSuchElementException;

public class Queue {
    private Node first;
    private Node last;
    private int n;

    public Queue(Node src){
        first = src;
        last = null;
    }

    public boolean isEmpty(){
        return first == null;
    }

    public void enqueue(Node node){
        Node oldLast = last;
        last = node;
        if(isEmpty()){
            first = last;
        }
        else{
            oldLast.next = last;
        }
    }

    public Node dequeue(){
        if(isEmpty()) throw new NoSuchElementException("Queue underflow :'(");
        Node current = first;
        first = first.next;
        if(isEmpty()) last = null;
        return current;
    }
}
