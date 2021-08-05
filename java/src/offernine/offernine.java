package offernine;

import java.util.ArrayDeque;
import java.util.Deque;

class CQueue{
    private Deque<Integer> s1;
    private Deque<Integer> s2;
    public CQueue(){
        s1 = new ArrayDeque<>();
        s2 = new ArrayDeque<>();
    }

    public void appendTail(int value){
        s1.push(value);
        if (s2.isEmpty()){
            move();
        }
    }
    
    public int deleteHead(){
        if (s2.isEmpty()){
            move();
        }
        return s2.isEmpty() ? -1 : s2.pop();
    }

    public void move(){
        while (!s1.isEmpty()){
            s2.push(s1.pop());
        }
    }
}

public class offernine {

    public static void main(String[] args) {
        CQueue obj = new CQueue();
        obj.appendTail(2);
        obj.appendTail(3);
        int param_1 = obj.deleteHead();
        System.out.println(param_1);
    }
}
