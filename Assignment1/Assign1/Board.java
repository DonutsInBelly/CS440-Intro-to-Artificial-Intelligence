package Assign1;
import java.util.ArrayList;

public class Board {
    public Node[][] grid;
    private int length;
    private int width;
    private double p;
    public Node src;
    public Node dest;

    public Board(int length, int width, double p) {
        this.grid = new Node[length][width];
        this.length = length;
        this.width = width;

        //Initializes all the cells of the grid
        for (int i = 0; i < this.length; i++) {
            for (int j = 0; j < this.width; j++) {
                this.grid[i][j] = new Node(i, j, p, this.grid);
            }
        }

        ArrayList<Node> visited = new ArrayList<Node>();
        for (Node[] row : grid) {
            for (Node n : row) {
                if (n.x > 0) {
                    n.children.add(this.grid[n.x - 1][n.y]);
                }
                if (n.x < this.length-1) {
                    n.children.add(this.grid[n.x + 1][n.y]);
                }
                if (n.y < this.width-1) {
                    n.children.add(this.grid[n.x][n.y + 1]);
                }
                if(n.y > 0) {
                    n.children.add(this.grid[n.x][n.y - 1]);
                }
            }
        }

        //Sets source and dest to 'clear'
        this.src = this.grid[0][0];
        this.dest = this.grid[length-1][width-1];
        this.src.isBlocked = false;
        this.dest.isBlocked = false;
    }

    public void updateBoard(TreeNode route) {
        TreeNode curr = route;
        while (curr != null) {
            this.grid[curr.x][curr.y].isPath = true;
            curr = curr.parent;
        }
    }

    public void eraseBoard(TreeNode route) {
        TreeNode curr = route;
        while (curr != null) {
            this.grid[curr.x][curr.y].isPath = false;
            curr = curr.parent;
        }
    }

    public int length() {
        return this.length;
    }

    public int width() {
        return this.width;
    }

    public void print() {
        //Prints the grid
        for (int i = 0; i < this.length; i++) {
            for (int j = 0; j < this.width; j++) {
                if(this.grid[i][j] == this.src || this.grid[i][j] == this.dest || this.grid[i][j].isPath){
                    System.out.print(" X ");
                }
                else if(this.grid[i][j].isBlocked == false){
                    System.out.print(" _ ");
                }
                else{
                    System.out.print("[_]");
                }
            }
            System.out.println();
        }
    }
}
