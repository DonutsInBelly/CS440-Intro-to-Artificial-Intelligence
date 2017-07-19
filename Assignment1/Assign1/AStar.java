package Assign1;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.concurrent.TimeUnit;

public class AStar {

    public TreeNode euclideanSearch(Board b) {
        long startTime = System.nanoTime();

        // Start A*
        Node curr = null, prev = null;
        Paths p = new Paths(b);
        ArrayList<Node> visited = new ArrayList<Node>();
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        b.src.euclideanDistance(b.dest);
        pq.add(b.src);
        while (pq.peek() != null) {
            //System.out.println("ayyy");
            curr = pq.poll();
            if (prev != null) {
                // p.addChild(prev, curr);
            }
            visited.add(curr);
            if (curr.x == b.dest.x && curr.y == b.dest.y) {
                // Success
                System.out.println("Found Path");
                break;
            }
            for (Node child : curr.children) {
                child.euclideanDistance(b.dest);
                if (visited.contains(child)) {
                    continue;
                }
                if (!child.isBlocked) {
                    p.addChild(curr, child);
                    pq.add(child);
                }
            }
            prev = curr;
        }

        long endTime = System.nanoTime();
        long deltaTime = endTime - startTime;
        System.out.println("Elapsed time (ms): " + deltaTime/1000000 + "ms");
        /*
        TreeNode t = p.shortestPath();
        while (t!=null) {
            System.out.println(t);
            t=t.parent;
        }
        */
        return p.shortestPath();
    }

    public TreeNode manhattanSearch(Board b) {
        long startTime = System.nanoTime();

        // Start A*
        Node curr = null, prev = null;
        Paths p = new Paths(b);
        ArrayList<Node> visited = new ArrayList<Node>();
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        b.src.manhattanDistance(b.dest);
        pq.add(b.src);
        while (pq.peek() != null) {
            //System.out.println("ayyy");
            curr = pq.poll();
            if (prev != null) {
                // p.addChild(prev, curr);
            }
            visited.add(curr);
            if (curr.x == b.dest.x && curr.y == b.dest.y) {
                // Success
                System.out.println("Found Path");
                break;
            }
            for (Node child : curr.children) {
                child.manhattanDistance(b.dest);
                if (visited.contains(child)) {
                    continue;
                }
                if (!child.isBlocked) {
                    p.addChild(curr, child);
                    pq.add(child);
                }
            }
            prev = curr;
        }

        long endTime = System.nanoTime();
        long deltaTime = endTime - startTime;
        System.out.println("Elapsed time (ms): " + deltaTime/1000000 + "ms");
        /*
        TreeNode t = p.shortestPath();
        while (t!=null) {
            System.out.println(t);
            t=t.parent;
        }
        */
        return p.shortestPath();
    }

    public int maxSearch(Board b) {
        long startTime = System.nanoTime();

        // Start A*
        Node curr = null, prev = null;
        // Paths p = new Paths(b);
        ArrayList<Node> visited = new ArrayList<Node>();
        PriorityQueue<Node> pq = new PriorityQueue<Node>();
        b.src.maxDistance(b.dest);
        pq.add(b.src);
        int expand = 0;
        while (pq.peek() != null) {
            //System.out.println("ayyy");
            curr = pq.poll();
            if (prev != null) {
                // p.addChild(prev, curr);
            }
            visited.add(curr);
            if (curr.x == b.dest.x && curr.y == b.dest.y) {
                // Success
                System.out.println("Found Path");
                break;
            }
            for (Node child : curr.children) {
                child.maxDistance(b.dest);
                if (visited.contains(child)) {
                    continue;
                }
                if (!child.isBlocked) {
                    expand++;
                    // p.addChild(curr, child);
                    pq.add(child);
                }
            }
            prev = curr;
        }

        long endTime = System.nanoTime();
        long deltaTime = endTime - startTime;
        System.out.println("Elapsed time (ms): " + deltaTime/1000000 + "ms");
        /*
        TreeNode t = p.shortestPath();
        while (t!=null) {
            System.out.println(t);
            t=t.parent;
        }
        */
        return expand;
    }
}
