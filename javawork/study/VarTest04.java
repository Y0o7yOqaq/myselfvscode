/* 
 * 变量的分类：
 *  1.成员变量
 *      在方法体外，类体内声明的变量
 *  2.局部变量
 *      在方法体中声明的变量
 * 
 *  在不同的作用域中，变量名是可以相同的
 *  在同一个作用域中，变量名不能改名
 * 
 *  "就近原则"
 */
public class VarTest04 {

    public static void main(String[] args) {
        int i = 200;// 局部变量
        System.out.println(i);
        System.out.println(k);// 输出k为100
        doSome();
    }

    static int k = 100;// 成员变量，声明的位置不影响变量的值

    public static void doSome() {
        int k = 10;// 局部变量，在方法体内声明的局部变量会覆盖同一变量名的成员变量
        System.out.println(k);// 输出k为10
    }
}
