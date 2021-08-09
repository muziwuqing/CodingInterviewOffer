package offertwentyfourth;

public class offertwentyfourth{
    public static class ListNode{
        int value;
        ListNode next;
        ListNode(int x) {value = x;}
    }


    public static ListNode reverseList(ListNode head){
        if (head == null || head.next == null) return null;
        ListNode rhead = new ListNode(0);
        head = head.next;
        while (head != null) {
            ListNode node = new ListNode(head.value);
            node.next = rhead.next;
            rhead.next = node;
            head = head.next;
        }
        return rhead;
    }

    public static void printList(ListNode head) {
        head = head.next;
        while(head != null){
            System.out.println(head.value);
            head = head.next;
        }
    }

    public static ListNode constructList(int [] arrs){
        ListNode head = new ListNode(0);
        ListNode p = head;
        for (int i=0; i<arrs.length; i++){
            ListNode node = new ListNode(arrs[i]);
            p.next = node;
            p = p.next;
        }
        return head;
    }
    
    public static void main(String[] args) {
        int []arrs = new int[]{1, 2, 3, 4, 5, 6, 7};
        ListNode head = constructList(arrs);
        printList(head);
        ListNode res = reverseList(head);
        printList(res);
    }
}