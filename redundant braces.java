public class Solution {
    public int braces(String A) {
        Stack<Character> stack = new Stack<>();
        for(char ch: A.toCharArray()){
            if(ch==')'){
                char top= stack.peek();
                stack.pop();
                
                if(top=='(')
                return 1;
                else{
                    int count=0;
                    while(top!='('){
                        top=stack.peek();
                        stack.pop();
                        count++;
                    }
                    if(count==1)
                    return 1;
                }
            }
            else{
            stack.add(ch);}
        }
         return 0;
    }
   
}
