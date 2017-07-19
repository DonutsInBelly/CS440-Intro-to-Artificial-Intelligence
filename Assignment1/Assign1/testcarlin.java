package Assign1;

public class testcarlin {
    public static void main(String[] args) {
        Board b= new Board(12,12,0.25);
        b.print();
        BreadthFirstSearch bs = new BreadthFirstSearch();
        DepthFirstSearch ds = new DepthFirstSearch();
        AStar as = new AStar();

        TreeNode euclidPath = as.euclideanSearch(b);
        b.updateBoard(euclidPath);
        b.print();
        b.eraseBoard(euclidPath);

        TreeNode manhatPath = as.manhattanSearch(b);
        b.updateBoard(manhatPath);
        b.print();
        b.eraseBoard(manhatPath);

        TreeNode path1 = bs.runBFS(b);
        b.updateBoard(path1);
        b.print();
        b.eraseBoard(path1);

        TreeNode path2 = ds.runDFS(b);
        b.updateBoard(path2);
        b.print();
        b.eraseBoard(path2);
    }
}
