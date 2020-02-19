/*
//封装
public class Puppy{
	//定义一个成员变量，不能直接"类名.变量名"访问，需要通过对象访问
   int puppyAge;
   //感觉是初始化
   public Puppy(String name){
      // 这个构造器仅有一个参数：name
      System.out.println("小狗的名字是 : " + name ); 
   }
   //通过set和get进行封装
   public void setAge( int age ){
       puppyAge = age;
   }
   public int getAge( ){
       System.out.println("小狗的年龄为 : " + puppyAge ); 
       return puppyAge;
   }
 
   public static void main(String[] args){
      // 创建对象 
      Puppy myPuppy = new Puppy( "tommy" );
      // 通过方法来设定age 
      myPuppy.setAge( 2 );
      // 调用另一个方法获取age 
      myPuppy.getAge( );
      //你也可以像下面这样访问成员变量 
      System.out.println("变量值 : " + myPuppy.puppyAge ); 
   }
}
*/


/*
//继承
public class UdClass { 
	//私有变量导致不能进行方法覆盖
    //private String name;  
    //private int id;
	String name;  
    int id;
    public UdClass(String myName, int myid) { 
        name = myName; 
        id = myid;
    } 
    public void eat(){ 
        System.out.println(name+"正在吃"); 
    }
    public void sleep(){
        System.out.println(name+"正在睡");
    }
    public void introduction() { 
        System.out.println("大家好！我是"         + id + "号" + name + "."); 
    } 
}
//继承
class Penguin extends UdClass { 
    public Penguin(String myName, int myid) { 
        super(myName, myid); 
    } 
}
//特有方法
class Bird extends UdClass { 
    public Bird(String myName, int myid) { 
        super(myName, myid); 
    } 
	public void udaction() { 
    System.out.println(id + "号" + name + "." + "会飞"); 
    } 
}
//方法覆盖
class Mouse extends UdClass { 
    public Mouse(String myName, int myid) { 
        super(myName, myid); 
	} 
	public void introduction() { 
    System.out.println("发生方法重写了！大家好！我是"         + id + "号" + name + "."); 
    } 
}
class TestClass{
	public static void main(String[] args){
		Penguin P = new Penguin("企鹅",1);
		P.eat();
		P.sleep();
		P.introduction();
		Mouse M = new Mouse("老鼠",2);
		M.eat();
		M.sleep();
		M.introduction();
		Bird B = new Bird("鸟",3);
		B.eat();
		B.sleep();
		B.introduction();
		B.udaction();
	}
}
*/


//多态
//程序入口类(实例化对象及调用) -- 人类 -- 宠物类 -- 具体宠物类
//类(宠物)是一个中间抽象类，连接人和具体宠物，让具体宠物继承自宠物类，宠物类抽象出方法让具体宠物类进行方法覆盖，人类参数为宠物类，可以利用多态，使传入参数不同，调用不同方法
//当出现新需求时，只需要让新需求继承自中间抽象类，这样的话，就可以"添加具体宠物类和新增程序入口类方法"，"不用修改"人类的传入参数
public class UdClass {
	public static void main(String[] args) {
		Master zhangsan = new Master();
		//Cat tom = new Cat();
		//zhangsan.feed(tom);
		zhangsan.feed(new Cat());
		zhangsan.feed(new Dog());
	}
}

//public class Pet {
class Pet {
	public void eat(){
		
	}
}

//public class Master {
class Master {
	//public void feed(Pet pet = new Cat()){
	public void feed(Pet pet){
		pet.eat();
	}
}

//public class Cat extends Pet {
class Cat extends Pet {
	public void eat(){
		System.out.println("小猫吃鱼");
	}
}
class Dog extends Pet {
	public void eat(){
		System.out.println("小狗吃肉");
	}
}