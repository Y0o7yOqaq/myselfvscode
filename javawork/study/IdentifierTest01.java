/*
    关于Java中的标识符
        1.什么是标识符？
            -在Java源程序中凡是程序员有权利自己命名的单词都是标识符
            -标识符可以标识的元素：
             *类名
             *方法名
             *接口名
             *常量名
             *变量名
             ....
        2.标识符的命名规则【属于语法，会报错】
            -由“数字、字母、下划线_、美元符号$”组成，不能含有其他字符
            -不能以数字开头
            -严格区分大小写
            -“关键字”不能做标识符
            -理论上没有长度限制，但不要太长
        3.标识符的命名规范【不属于语法，不会报错，但影响他人阅读】
            -最好见名知意

                public class UserService{
                    public void login(String username,String password){

                    }
                }

            -遵守驼峰命名方式  SystemService UserService CustomerService ...
            
            -类名、接口名：首字母大写，后面每个单词首字母大写
             变量名、方法名：首字母小写，后面每个单词首字母大写
             常量名：全部大写,多个单词之间用 _ 隔开；

*/
public class IdentifierTest01 {            //IdentifierTest01是一个类名，名字可以修改
    public static void main(String[] args){//main是一个方法名，args是一个变量名
        int i=10;                          //i是一个变量名 
        System.out.println(i);
    }
}




