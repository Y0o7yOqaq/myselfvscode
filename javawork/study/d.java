/*
 * 一个Java程序中不一定要有public class
 * 一个Java源程序中可以定义多个class
 * 一个class定义会对应生成一个xxx.class字节码文件
 * 一个Java源文件中只能有一个public class
 * 且public的class的类名应与源文件名相同
 * 每一个class中都可以编写main方法,设定程序的入口
 * 在命令窗口执行Java x时，要求x.class中必须有main方法，否则会出现运行阶段的错误
 */
class a {
  public static void main(String[] args) {
    System.out.println("a's main method invoke!'");
    ;
  }
}

class b {
  public static void main(String[] args) {
    System.out.println("b's main method invoke!'");
    ;
  }
}

class c {
  public static void main(String[] args) {
    System.out.println("c's main method invoke!'");
    ;
  }
}

public class d {
  public static void main(String[] args) {
    System.out.println("d's main method invoke!'");
    ;
  }
}
