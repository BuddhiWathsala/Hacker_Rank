import java.util.*;

public class dog{

public static void main(String [] args){
  
        Scanner in = new Scanner(System.in);
        ArrayList<Integer> total = new ArrayList<Integer>();
        int tests = in.nextInt();
        for (int j = 0; j < tests; j++) {
          int countDogs = in.nextInt();
          int countWalkers = in.nextInt();
          ArrayList<Integer> diffList = new ArrayList<Integer>();
          int dogSizeArray[] = new int[countDogs];
          for (int k = 0; k < dogSizeArray.length; k++) {
              dogSizeArray[k] = in.nextInt();
            }
            Arrays.sort(dogSizeArray);
            int[] diff = new int[countDogs - 1];
            for (int l = 0; l < dogSizeArray.length - 1; l++) {
                diff[l] = dogSizeArray[l + 1] - dogSizeArray[l];
            }
            Arrays.sort(diff);

            int count = 0;
            int extra = (countDogs - countWalkers);
            for (int i = 0; i < extra; i++) {
                count = count + diff[i];
            }
            total.add(count);
        }
       for (int n = 0; n < total.size(); n++) {
            System.out.println(total.get(n));
       }
}
}
