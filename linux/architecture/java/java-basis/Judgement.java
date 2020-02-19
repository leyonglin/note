
/*
//if语句
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
         System.out.print("这是 else 语句");
      }
   }
}
*/


/*
//switch语句
public class Judgement {
   public static void main(String args[]){
      int i = 0;
	  //switch和case后面的表达式只能是int和String类型,以及自动类型转换，不能是别的类型，不同版本不一样
      switch(i){
         case 0:
            System.out.println("0");
         case 1:
            System.out.println("1");
         case 2: case 3:                   //case合并
            System.out.println("2或者3");break; //可选，如果 case 语句块中没有 break 语句时，匹配成功后，从当前 case 开始，后续所有case的值都会输出直到遇到break，称为switch穿透
         default:
            System.out.println("default");
      }
   }
}
*/


public class Judgement {
   public static void main(String args[]) {
      int x=1;
	  //myfor为该for循环的名称，可以不写，作用是给break和continue跳过时指定
      myFor:for(; x < 6;) {  
         System.out.print("value of x : " + x );
         System.out.print("\n");
		 x++;
      }
	  System.out.print("out for x : " + x );
   }
}