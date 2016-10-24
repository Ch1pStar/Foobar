public class Answer { 
  public static int[] answer(int h, int[] q){
    int size = (int) (Math.pow(2, h)-1);
    for(int val=0; val<q.length; val++){
      if(q[val] == size){
        q[val] = -1;
      }else{
        q[val] = parent(q[val]);
      }
    }
    return q;
  }
    
  public static int parent(int node){
    int x = node;
    int bit = x;
    
    while((x & bit)!=0 && notSimpleCase(x)){
      int y = x + popcount(x);
      bit = getMSBmask(y & ~x);
      int mask = (bit << 1) - 1;
      int z = (x & mask) + popcount(x & ~mask);

      if ((z == mask) && (x & (bit << 1))!=0){
          return node + 1;  
      }

      x = z;
    }

    if (notSimpleCase(x)){
        return node + 1;
    }
    else{
      return node + 1 + (( (x+1) & x)!=0? 0: x);
    }
  }

  public static int popcount(int x){
    return Integer.bitCount(x);
  }
  
  public static int getMSBindex(int x){
    return 31 - Integer.numberOfLeadingZeros(x);
  }
  
  public static int getMSBmask(int x){ 
    return 1 << getMSBindex(x); 
  }
  
  public static boolean notSimpleCase(int x){
    return ((x+1) & x)!=0 && ((x+2) & (x+1))!=0; 
  }
}