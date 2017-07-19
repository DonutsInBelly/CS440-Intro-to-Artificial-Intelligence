package Assign1;

public class test8 {
    public static void main(String[] args) {
        AStar as = new AStar();
        int iter = 1000;
        int totalexpand = 0;
        for (int i = 1; i<=iter; i++) {
            Board b = new Board(10,10,0.25);
            totalexpand += as.maxSearch(b);
        }
        System.out.println((double)totalexpand/iter);
    }
}
