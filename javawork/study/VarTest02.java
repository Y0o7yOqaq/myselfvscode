/* 
 * 关于Java语言当中的变量
 *  1、在方法体中的Java代码，是遵守自上而下的顺序依次逐行执行的。
 *      前一行代码必须完整的结束，之后的程序才能执行。
 *  2、在同一个作用域当中，变量名不能重名，但可以重新赋值。
 */

public class VarTest02 {
    public static void main(String[] args) {
        int i = 100;
        System.out.println(i);
        i = 200;
        System.out.println(i);
    }
}
