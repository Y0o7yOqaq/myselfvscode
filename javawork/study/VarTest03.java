/* 
 *  变量的作用域
 *      1、变量的作用域：
 *          变量的有效范围，出了变量的作用域就无法访问变量
 *          出了大括号就不认识了
 */
public class VarTest03 {
    static int k = 50;// static不能去掉

    public static void main(String[] args) {
        int i = 100;// 变量i的作用域是整个main方法，i在其中是有效的，可见的，能被访问的。
        System.out.println(k);
        System.out.println(i);

        for (int a = 0; a < 10; a++) {

        }
        // System.out.println(a);无法访问a变量，a变量在循环中声明，a变量的作用域为for循环内，循环结束后，a变量的内存就被回收了

        int j;
        for (j = 0; j < 10; j++) {

        }
        System.out.println(j);//变量j可以访问，j变量在main方法中声明，j变量的作用域为main方法中。
    }

    public static void doSome() {
        // System.out.println(i);无法访问main方法中的变量i，已经出了变量i的作用域
        System.out.println(k);
    }
}
