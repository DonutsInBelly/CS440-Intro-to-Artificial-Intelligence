package Assign1;
import java.util.Queue;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

public class BreadthFirstSearch {

    public TreeNode runBFS(Board b) {
        long startTime = System.nanoTime();

        Node curr;
        Paths p = new Paths(b);
        ArrayList<Node> visited = new ArrayList<Node>();
        Queue<Node> q = new LinkedList<Node>();
        q.add(b.grid[0][0]);
        while (q.peek() != null) {
            curr = q.poll();
            visited.add(curr);
            //System.out.println("This Node: "+curr.x+", "+curr.y);
            if (curr.x == b.dest.x && curr.y == b.dest.y) {
                //System.out.println("Success!");
            }
            //System.out.println("Children: " + curr.children);
            for (Node child : curr.children) {
                //System.out.println(child.x+","+child.y);
                if (visited.contains(child)) {
                    continue;
                }
                if (!child.isBlocked) {
                    p.addChild(curr, child);
                    q.add(child);
                }
            }
        }
        /*
        TreeNode t = p.shortestPath();
        while (t!=null) {
            System.out.println(t);
            t=t.parent;
        }*/
        long endTime = System.nanoTime();
        long deltaTime = endTime - startTime;
        System.out.println("Elapsed time (ms): " + deltaTime/1000000 + "ms");
        return p.shortestPath();
    }
}
