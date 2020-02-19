//输出hello world

//定义一个公开的类名,这个类名和文件名一致,可以没有，有则只能有一个
public class  HelloWorld{
/**
*类体,不能写java语句，除了声明变量和方法
*public             公开的
*static				静态的
*void				空，该方法没有返回值
*main				主方法
*(String[] args)	main方法的形参列表，String[]是引用数据类型，args是局部变量名
*/
	public static void main(String[] args){   //主方法，程序执行入口，每个类都可以定义
		//方法体，以;终止，字符串用""引起来
		//向终端输出一段消息hello world!
		//System.out.println("hello world!");
		System.out.print("你好");
	}
}
//可以有多个class，编译时每个class会对应生成一个以类名为文件名的class文件
//如果执行改类，则需要有主方法入口
/*
class A
{
}
*/