/*
//���巽��
public class UdMethod {
  public static void main(String[] args) {
    int num1 = 1;
    int num2 = 2;
 
    System.out.println("����ǰ num1 ��ֵΪ��" +
                        num1 + " ��num2 ��ֵΪ��" + num2);
 
    // ����swap����
    swap(num1, num2);
    System.out.println("������ num1 ��ֵΪ��" +
                       num1 + " ��num2 ��ֵΪ��" + num2);
  }
  public static void swap(int n1, int n2) {
    System.out.println("\t���� swap ����");
    System.out.println("\t\t����ǰ n1 ��ֵΪ��" + n1
                         + "��n2 ��ֵ��" + n2);
    // ���� n1 �� n2��ֵ
    int temp = n1;
    n1 = n2;
    n2 = temp;
 
    System.out.println("\t\t������ n1 ��ֵΪ " + n1
                         + "��n2 ��ֵ��" + n2);
  }
}
*/

/*
//����Overload
public class OverLoading {
    public int test(){
        System.out.println("test1");
        return 1;
    }
 
    public void test(int a){
        System.out.println("test2");
    }   
 
    //����������������˳��ͬ
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
test1   #������������
1	    #���÷������������ֵ
test2   #������������
test3
returntest3
test4
returntest4
*/


/*
//������дOverride
//�����б������ȫ�뱻��д��������ͬ ...
class Animal{
   public void move(){
      System.out.println("��������ƶ�");
   }
}
 
class Dog extends Animal{
   public void move(){
      //super.move(); // Ӧ��super��ķ���
      System.out.println("�������ܺ���");
   }
}

public class OverLoading{
   public static void main(String args[]){
 
      Animal b = new Dog(); // Dog ����
      b.move(); //ִ�� Dog��ķ���
 
   }
}
*/


/*
//�����ݹ�
public class OverLoading {
    public static void main(String[] args) {
        System.out.println("���ںţ�Java3y��" + sum(100));
    }
    public static int sum(int n) {
		//��ֹ����
        if (n == 1) {
            return 1;
        } else {
            return sum(n - 1) + n;
        }
    }
}
*/





