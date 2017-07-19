package Assign1;
import java.util.Queue;
import java.util.Stack;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

public class DepthFirstSearch {

    public TreeNode runDFS(Board b){
        long startTime = System.nanoTime();

        Node curr;
        Paths p = new Paths(b);
        ArrayList<Node> visited = new ArrayList<Node>();
        Stack<Node> s = new Stack<>();
        s.addElement(b.grid[0][0]);

        while (!s.isEmpty()){
            curr = s.pop();
            visited.add(curr);
            //System.out.println("This node: " +curr.x+", "+curr.y);
            if(curr.x == b.dest.x && curr.y == b.dest.y){
                //System.out.println("Success!!");
            }
            //System.out.println("Children: " +curr.children);
            for(Node child : curr.children){
                //System.out.println(child.x", "+child.y);
                if(visited.contains(child)){
                    continue;
                }
                if(!child.isBlocked){
                    p.addChild(curr, child);
                    s.push(child);
                }
            }
        }
        long endTime = System.nanoTime();
        long deltaTime = endTime - startTime;
        System.out.println("Elapsed time (ms): " +  deltaTime/1000000 + "ms");
        return p.shortestPath();
    }
}

