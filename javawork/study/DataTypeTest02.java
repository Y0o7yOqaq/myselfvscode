/* 基本数据类型默认值
 * byte               0
 * short              0
 * int                0
 * long               0
 * float              0.0f
 * double             0.0d
 * boolean            false(true为1，false为0)
 * char               '\u0000'(空格)
 * 
 */
public class DataTypeTest02 {
    static byte a;// 成员变量未初始化，系统自动会给默认值。
    static short b;
    static int c;
    static long d;
    static float e;
    static double f;
    static boolean g;
    static char h;

    public static void main(String[] args) {
        /*
         * int i;
         * System.out.println(i); 局部变量未初始化，报错
         */
        System.out.println(a); // 0
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        System.out.println(f);
        System.out.println(g);
        System.out.println(h);
        System.out.println(".........");

    }
}
