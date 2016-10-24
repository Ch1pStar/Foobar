public class Answer {
  public static int answer(int s, int l){

    int res = 0,
      i = 0,
      line = l,
      groupStart = s;
    
    while(line>0){
      i=0;
      while(i<line){
        res ^= groupStart+i++;
      }
      groupStart += l;
      line--;
    }
    
    return res;
  }
}
