package Number;

public class FIRST {
    static String s1 = "hhh"; /*
                               * 通常将类的属性成为全局变量（成员变量），将方法中的属性称为局部变量
                               * 全局变量在类体中声明 ，局部变量在方法体中声明 s1是全局变量 s2是局部变量
                               */

    public static void main(String[] args) {
        String s2 = "java";
        System.out.println(s1);
        System.out.println(s2);
    }
}
