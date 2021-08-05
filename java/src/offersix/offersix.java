package offersix;

import java.util.Arrays;

public class offersix {
    public static class ListNode{
        int val;
        ListNode next;
        ListNode(int x) { val = x;}
    }
    /*
    public static int[] reversePrint(ListNode head){
        Stack<Integer> stack = new Stack<>();
        while (head != null) {
            stack.push(head.val);
            head = head.next;
        }
        int []res = new int[stack.size()];
        int i=0;
        while (!stack.empty()) {
            res[i++] = stack.pop();
        }
        return res;
    }
    */
    public static int[] reversePrint(ListNode head){
        int count = 0;
        ListNode tmp = head;
        while (tmp != null) {
            tmp = tmp.next;
            count++;
        }
        int []res = new int[count];
        int j = count - 1;
        while (head != null) {
            res[j] = head.val;
            head = head.next;
            j--;
        }
        return res;
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(0);
        ListNode rt = head;
        for(int i = 1; i < 10; i++) {
            ListNode node = new ListNode(i);
            rt.next = node;
            rt = rt.next;
        }
        int [] res = reversePrint(head);
        System.out.println(Arrays.toString(res));
    }

}
