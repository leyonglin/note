
/*
//if���
public class Judgement {
   public static void main(String args[]){
      int x = 50;
      if( x == 10 ){
         System.out.print("Value of X is 10");
      }else if( x == 20 ){
         System.out.print("Value of X is 20");
      }else if( x == 30 ){
         System.out.print("Value of X is 30");
      }else{
         System.out.print("���� else ���");
      }
   }
}
*/


/*
//switch���
public class Judgement {
   public static void main(String args[]){
      int i = 0;
	  //switch��case����ı��ʽֻ����int��String����,�Լ��Զ�����ת���������Ǳ�����ͣ���ͬ�汾��һ��
      switch(i){
         case 0:
            System.out.println("0");
         case 1:
            System.out.println("1");
         case 2: case 3:                   //case�ϲ�
            System.out.println("2����3");break; //��ѡ����� case ������û�� break ���ʱ��ƥ��ɹ��󣬴ӵ�ǰ case ��ʼ����������case��ֵ�������ֱ������break����Ϊswitch��͸
         default:
            System.out.println("default");
      }
   }
}
*/


public class Judgement {
   public static void main(String args[]) {
      int x=1;
	  //myforΪ��forѭ�������ƣ����Բ�д�������Ǹ�break��continue����ʱָ��
      myFor:for(; x < 6;) {  
         System.out.print("value of x : " + x );
         System.out.print("\n");
		 x++;
      }
	  System.out.print("out for x : " + x );
   }
}