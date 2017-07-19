package Assign1;

import java.lang.*;
import java.util.ArrayList;
import java.lang.Comparable;
import java.util.Comparator;

public class Node implements Comparator<Node>, Comparable<Node> {
    public int x;
    public int y;
    public double distance = 0;
    public Boolean isBlocked;
    public Boolean isDiscovered;
    public Boolean isPath = false;
    //private int f;
    //private int g;
    //private int h;
    public Node next; // To be used for stacks and queues
    public Node north; // Used to keep track of neighbors
    public Node south;
    public Node east;
    public Node west;
    public ArrayList<Node> children;

    public Boolean getIsBlocked(double p){
        if(Math.random() >= p){
            return false;
        }
        else{
            return true;
        }
    }

    public Node(int x, int y, double p, Node[][] grid){
        this.x = x;
        this.y = y;
        this.isBlocked = getIsBlocked(p);
        this.isDiscovered = false;
        this.next = null;

        this.north = null;
        this.south = null;
        this.east = null;
        this.west = null;
        this.children = new ArrayList<Node>();
        //System.out.println("This Node: "+this.x+", "+this.y);
        /*
        if(x > 0) {
            System.out.println((x-1)+","+y);
            this.north = grid[x - 1][y];
            this.children.add(grid[x - 1][y]);
        }
        if(x < Main.length-1) {
            System.out.println((x+1)+","+y);
            this.south = grid[x + 1][y];
            this.children.add(grid[x + 1][y]);
        }
        if(y < Main.width-1) {
            System.out.println(x+","+(y+1));
            this.east = grid[x][y + 1];
            this.children.add(grid[x][y + 1]);
        }
        if(y > 0) {
            System.out.println((x)+","+(y-1));
            this.west = grid[x][y - 1];
            this.children.add(grid[x][y - 1]);
        }*/
    }

    public double euclideanDistance(Node dest) {
        this.distance = Math.sqrt(Math.pow((this.x - dest.x), 2)+Math.pow((this.y - dest.y), 2));
        return this.distance;
    }

    public double manhattanDistance(Node dest) {
        this.distance = Math.abs(this.x - dest.x) + Math.abs(this.y - dest.y);
        return this.distance;
    }

    public double maxDistance(Node dest) {
        // this.distance = 0.25*this.euclideanDistance(dest) + (1-0.25)*this.manhattanDistance(dest);
        this.distance = Math.pow(Math.pow(Math.abs(this.x - dest.x), 0.25) + Math.pow(Math.abs(this.y - dest.y),0.25),1/0.25);
        return this.distance;
    }

    public int compareTo(Node a) {
        if (this.distance < a.distance) {
            return -1;
        } else if (this.distance == a.distance) {
            return 0;
        } else {
            return 1;
        }
    }

    public int compare(Node a, Node b) {
        if (a.distance < b.distance) {
            return -1;
        } else if (a.distance == b.distance) {
            return 0;
        } else {
            return 1;
        }
    }

    public String toString() {
        return "(" + this.x + ", " + this.y + ")";
    }
}
