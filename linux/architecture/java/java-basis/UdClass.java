/*
//��װ
public class Puppy{
	//����һ����Ա����������ֱ��"����.������"���ʣ���Ҫͨ���������
   int puppyAge;
   //�о��ǳ�ʼ��
   public Puppy(String name){
      // �������������һ��������name
      System.out.println("С���������� : " + name ); 
   }
   //ͨ��set��get���з�װ
   public void setAge( int age ){
       puppyAge = age;
   }
   public int getAge( ){
       System.out.println("С��������Ϊ : " + puppyAge ); 
       return puppyAge;
   }
 
   public static void main(String[] args){
      // �������� 
      Puppy myPuppy = new Puppy( "tommy" );
      // ͨ���������趨age 
      myPuppy.setAge( 2 );
      // ������һ��������ȡage 
      myPuppy.getAge( );
      //��Ҳ�����������������ʳ�Ա���� 
      System.out.println("����ֵ : " + myPuppy.puppyAge ); 
   }
}
*/


/*
//�̳�
public class UdClass { 
	//˽�б������²��ܽ��з�������
    //private String name;  
    //private int id;
	String name;  
    int id;
    public UdClass(String myName, int myid) { 
        name = myName; 
        id = myid;
    } 
    public void eat(){ 
        System.out.println(name+"���ڳ�"); 
    }
    public void sleep(){
        System.out.println(name+"����˯");
    }
    public void introduction() { 
        System.out.println("��Һã�����"         + id + "��" + name + "."); 
    } 
}
//�̳�
class Penguin extends UdClass { 
    public Penguin(String myName, int myid) { 
        super(myName, myid); 
    } 
}
//���з���
class Bird extends UdClass { 
    public Bird(String myName, int myid) { 
        super(myName, myid); 
    } 
	public void udaction() { 
    System.out.println(id + "��" + name + "." + "���"); 
    } 
}
//��������
class Mouse extends UdClass { 
    public Mouse(String myName, int myid) { 
        super(myName, myid); 
	} 
	public void introduction() { 
    System.out.println("����������д�ˣ���Һã�����"         + id + "��" + name + "."); 
    } 
}
class TestClass{
	public static void main(String[] args){
		Penguin P = new Penguin("���",1);
		P.eat();
		P.sleep();
		P.introduction();
		Mouse M = new Mouse("����",2);
		M.eat();
		M.sleep();
		M.introduction();
		Bird B = new Bird("��",3);
		B.eat();
		B.sleep();
		B.introduction();
		B.udaction();
	}
}
*/


//��̬
//���������(ʵ�������󼰵���) -- ���� -- ������ -- ���������
//��(����)��һ���м�����࣬�����˺;������þ������̳��Գ����࣬���������������þ����������з������ǣ��������Ϊ�����࣬�������ö�̬��ʹ���������ͬ�����ò�ͬ����
//������������ʱ��ֻ��Ҫ��������̳����м�����࣬�����Ļ����Ϳ���"��Ӿ���������������������෽��"��"�����޸�"����Ĵ������
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
		System.out.println("Сè����");
	}
}
class Dog extends Pet {
	public void eat(){
		System.out.println("С������");
	}
}