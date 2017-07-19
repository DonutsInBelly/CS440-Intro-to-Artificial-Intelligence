package Assign1;

public class Main {
    public static int length = 5;
    public static int width = 5;
    public static double p = 0.2;

    public static boolean BFS(Node src, Node dest){

        Queue frontier = new Queue(src);
        // Queue path = new Queue(src);
        while(!frontier.isEmpty()){
            Node current = frontier.dequeue();
            if(current == dest){
                return true;
            }
            if(current.north != null && !current.north.isDiscovered && !current.north.isBlocked){
                current.north.isDiscovered = true;
                frontier.enqueue(current.north);
            }
            if(current.south != null && !current.south.isDiscovered && !current.south.isBlocked){
                current.south.isDiscovered = true;
                frontier.enqueue(current.south);
            }
            if(current.east != null && !current.east.isDiscovered && !current.east.isBlocked){
                current.east.isDiscovered = true;
                frontier.enqueue(current.east);
            }
            if(current.west != null && !current.west.isDiscovered && !current.west.isBlocked){
                current.west.isDiscovered = true;
                frontier.enqueue(current.west);
            }
        }
        return false;
    }


    public static void main(String[] args) {
        Node[][] grid = new Node[length][width];


        //Initializes all the cells of the grid
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < width; j++) {
                grid[i][j] = new Node(i, j, p, grid);
            }
        }

        //Sets source and dest to 'clear'
        Node src = grid[0][0];
        Node dest = grid[length-1][width-1];
        src.isBlocked = false;
        dest.isBlocked = false;

        //Prints the grid
        for (int i = 0; i < length; i++) {
            for (int j = 0; j < width; j++) {
                if(grid[i][j] == src || grid[i][j] == dest){
                    System.out.print(" X ");
                }
                else if(grid[i][j].isBlocked == false){
                    System.out.print(" _ ");
                }
                else{
                    System.out.print("[_]");
                }
            }
            System.out.println();
        }

        if(BFS(src, dest)){
            System.out.println("PATH FOUND!");
        }
        else{
            System.out.println("NO PATH!!");
        }
    }
}
