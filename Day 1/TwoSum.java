import java.util.*;

public class TwoSum{
    public static void main(String[] args) {
        List<Double> l=new ArrayList<>();
        double [] nums={1,2,3,4,5,6};
        double k=90;
        for (Double d:nums){
            l.add(d);
        }
        System.out.print(checkSum(l,k));
    }
    public static boolean checkSum(List<Double> l, double k){
        /**
         * check if the sum of two numbers in list l equals a double k
         * @params: List<Double> -the list to check
         * @params: Double l- the desired sum
         * return: a boolean 
         */
        Set<Double> seen=new HashSet<Double>();
        for (Double var : l) {
            if (seen.contains(k-var)){
                return true;
            }
            seen.add(var);
        }
        return false;

    }
}