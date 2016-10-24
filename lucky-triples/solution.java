public class Answer {
  public static int answer( int[] arr){
    int combs = 0;
    int[] nd = new int[arr.length];

    for( int i = 1; i < arr.length-1; ++i){
      for( int j = 0; j < i; ++j){
        if( arr[i] % arr[j] == 0)
          ++nd[i];
      }
    }

    for( int i = 2; i < arr.length; i++){
      for( int j = 1; j < i; ++j){
        if( arr[i] % arr[j] == 0)
          combs += nd[j];
      }
    }

    return combs;
  }

}