//�Ӽ��̶�������

/*
public class  KeyBoard{
	public static void main(String[] args){
        //1.��������ɨ�����
        java.util.Scanner s = new java.util.Scanner(System.in);
        //2.����scanner�����next()������ʼ�����û���������,���ַ�����ʽ����
        String userInputContent = s.next();
        System.out.println("�������ˣ�" +userInputContent);
	}
}
*/


//����Ҫ�ſ�ͷ
import java.util.Scanner; 
public class KeyBoard {
//class KeyBoard1 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // �Ӽ��̽�������
        // next��ʽ�����ַ���
        System.out.print("next��ʽ���գ�");
        // �ж��Ƿ�������
        if (scan.hasNext()) {
			String str1 = scan.next();
            System.out.print("���������Ϊ��" + str1);
        }
        scan.close();
    }
}

//nextLine()����������  hasNextDouble()��������
