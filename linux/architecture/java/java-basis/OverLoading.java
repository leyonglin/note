/*
//定义方法
public class UdMethod {
  public static void main(String[] args) {
    int num1 = 1;
    int num2 = 2;
 
    System.out.println("交换前 num1 的值为：" +
                        num1 + " ，num2 的值为：" + num2);
 
    // 调用swap方法
    swap(num1, num2);
    System.out.println("交换后 num1 的值为：" +
                       num1 + " ，num2 的值为：" + num2);
  }
  public static void swap(int n1, int n2) {
    System.out.println("\t进入 swap 方法");
    System.out.println("\t\t交换前 n1 的值为：" + n1
                         + "，n2 的值：" + n2);
    // 交换 n1 与 n2的值
    int temp = n1;
    n1 = n2;
    n2 = temp;
 
    System.out.println("\t\t交换后 n1 的值为 " + n1
                         + "，n2 的值：" + n2);
  }
}
*/

/*
//重载Overload
public class OverLoading {
    public int test(){
        System.out.println("test1");
        return 1;
    }
 
    public void test(int a){
        System.out.println("test2");
    }   
 
    //以下两个参数类型顺序不同
    public String test(int a,String s){
        System.out.println("test3");
        return "returntest3";
    }   
 
    public String test(String s,int a){
        System.out.println("test4");
        return "returntest4";
    }   
 
    public static void main(String[] args){
        OverLoading o = new OverLoading();
        System.out.println(o.test());
        o.test(1);
        System.out.println(o.test(1,"test3"));
        System.out.println(o.test("test4",1));
    }
}
*/

/*
test1   #方法内语句输出
1	    #调用方法后输出返回值
test2   #方法内语句输出
test3
returntest3
test4
returntest4
*/


/*
//方法重写Override
//参数列表必须完全与被重写方法的相同 ...
class Animal{
   public void move(){
      System.out.println("动物可以移动");
   }
}
 
class Dog extends Animal{
   public void move(){
      //super.move(); // 应用super类的方法
      System.out.println("狗可以跑和走");
   }
}

public class OverLoading{
   public static void main(String args[]){
 
      Animal b = new Dog(); // Dog 对象
      b.move(); //执行 Dog类的方法
 
   }
}
*/


/*
//方法递归
public class OverLoading {
    public static void main(String[] args) {
        System.out.println("公众号：Java3y：" + sum(100));
    }
    public static int sum(int n) {
		//终止条件
        if (n == 1) {
            return 1;
        } else {
            return sum(n - 1) + n;
        }
    }
}
*/





