import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Mult{
    public static void main(String[] args){
        List<Integer> l=new ArrayList<>();
        for (int i = 1; i < 6; i++) {
            l.add(i);
        }
        l=products(l);
        System.out.println(l.toString());
        
    }
    public static List<Integer> products(List<Integer> l){
        int length=l.size();
        int[] preProd=new int[length];
        int[] afterProd=new int[length];
        preProd[0]=l.get(0);
        for (int i=1;i<length;i++) {
            preProd[i]=preProd[i-1]*l.get(i);
        }
        
        afterProd[length-1]=l.get(length-1);
        for(int i=length-2;i>=0;i--){
            afterProd[i]=afterProd[i+1]*l.get(i);
        }
        List<Integer> result=new ArrayList<>();
        for (int i = 0; i < length; i++) {
            if (i == 0){
                result.add(afterProd[i + 1]);
            }
            else if( i == length - 1){
                result.add(preProd[i - 1]);
            }
            else{
                result.add(preProd[i - 1] * afterProd[i + 1]);
            }
        }     
        return result;
    }
}