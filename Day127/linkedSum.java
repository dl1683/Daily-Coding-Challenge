import java.util.*;
public class linkedSum{
    public static void main(String[] args) throws Exception{
        LinkedList list=new LinkedList<>();
        list.add(2);
        list.add(4);
        int n=convertToNum(list);
        System.out.println("n "+ n);
        list.clear();
        list=convertToListRec(n, list);
        System.out.println("List " +list);
    }

    public static int convertToNum(LinkedList list) throws Exception{
        /**
         * Convert a LinkedList into a number given.
         */
        int i=0;
        int sum=0;
        while( !list.isEmpty()){
            sum+=(int)(list.pop()) *Math.pow(10, i);
            i++;
        }
        return sum;
    }

    public static LinkedList convertToListRec(int a,LinkedList list) {
        /**
         * Convert the int a into a LinkedList using tail recursion. 
         * @Return: LinkedList list
         */
        if(a<10){
            list.add(a); //method returns boolean so we have to return on the next line
            return list;
        }
        else{
            list.add(a%10);
            convertToListRec(a/10,list);
            return list;
        }
    }
}
