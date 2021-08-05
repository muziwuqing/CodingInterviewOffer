package offertenfirst;


public class offertenfirst{
    public static int fib(int n){
        int a = 0, b = 1;
        for(int i = 0; i < n; i++){
            int tmp = (a + b) % 1000000007;
            a = b;
            b = tmp;
        }
        return a;
    }
    public static void main(String[] args) {
        System.out.println(fib(47));
    }
}