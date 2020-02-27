//从键盘读入数据

/*
public class  KeyBoard{
	public static void main(String[] args){
        //1.创建键盘扫描对象
        java.util.Scanner s = new java.util.Scanner(System.in);
        //2.调用scanner对象的next()方法开始接收用户键盘输入,以字符串形式接收
        String userInputContent = s.next();
        System.out.println("你输入了：" +userInputContent);
	}
}
*/


//导入要放开头
import java.util.Scanner; 
public class KeyBoard {
//class KeyBoard1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // 从键盘接收数据
        // next方式接收字符串
        System.out.print("next方式接收：");
        // 判断是否还有输入
        if (scan.hasNext()) {
			String str1 = scan.next();
            System.out.print("输入的数据为：" + str1);
        }
        scan.close();
    }
}

//nextLine()接收行数据  hasNextDouble()接收数字
