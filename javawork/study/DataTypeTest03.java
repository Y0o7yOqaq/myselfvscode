/* 
 *      转义字符  “\字符”
 *          '\ddd':   1~3位八进制数据所表示的字符，如'\123';
 *          '\u0000': 4位十六进制数据所表示的字符，0000可换为其他数字，如'\u0000';
 *          '\\':     反斜杠；
 *          '\'':     单引号；
 *          '\n':     换行符；
 *          '\t':     垂直制表符，将光标移到下一个制表符的位置；
 *          '\r':     回车；
 *          '\b':     退格；
 *          '\f':     换页；
 */
public class DataTypeTest03 {
    public static void main(String[] args) {
        char a = '\123';
        char b = '\u2605';
        char c = '\\';
        char d = '\f';
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
    }
}
