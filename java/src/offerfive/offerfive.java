package offerfive;


public class offerfive {
    public static String replaceSpace(String s){
        StringBuffer str = new StringBuffer(s);
        int P1 = str.length() - 1;
        for (int i=0; i <= P1; i++) {
            if (str.charAt(i) == ' ') {
                str.append("  ");
            }
        }
        int P2 = str.length() - 1;
        for (; P1 < P2; P1--, P2--){
            char c = str.charAt(P1);
            if (str.charAt(P1) != ' '){
                str.setCharAt(P2, c);
            } else {
                str.setCharAt(P2, '0');
                str.setCharAt(P2-1, '2');
                str.setCharAt(P2-2, '%');
                P2 -= 2;
            }
        }
        return str.toString();
    }

    public static void main(String[] args) {
        String s = "     ";
        String res = replaceSpace(s);
        System.out.println(res);
    }
}
