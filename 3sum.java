public class Solution {
    public int threeSumClosest(int[] A, int B) {
        int min=Integer.MAX_VALUE;
        int last=0;
        Arrays.sort(A);
        for(int i=0;i<A.length;i++){
           int j=i+1,k=A.length-1;
           while(j<k){
               int sum=A[i]+A[j]+A[k];
               int subs=Math.abs(sum-B);
               if(subs==0) 
               return sum;
               if(subs<min){
                   min=subs;
                   last = sum;
               }
               if(sum<=B)
               j++;
               else
               k--;
               
           }}
           return last;
    }}

