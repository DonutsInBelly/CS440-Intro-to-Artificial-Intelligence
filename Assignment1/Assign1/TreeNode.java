package Assign1;
import java.util.ArrayList;

public class TreeNode {
    public int x;
    public int y;
    public int depth;
    public double distance;
    public TreeNode parent;
    public ArrayList<TreeNode> children;

    public TreeNode() {
        this.parent = null;
        this.children = new ArrayList<TreeNode>();
    }

    public TreeNode(int x, int y) {
        this.x = x;
        this.y = y;
        this.parent = new TreeNode();
        this.depth = 0;
        this.children = new ArrayList<TreeNode>();
    }

    public TreeNode(int x, int y, TreeNode parent) {
        this.x = x;
        this.y = y;
        this.depth = parent.depth + 1;
        this.parent = parent;
        this.children = new ArrayList<TreeNode>();
    }

    public TreeNode(int x, int y, double distance) {
        this.x = x;
        this.y = y;
        this.distance = distance;
        this.parent = parent;
        this.children = new ArrayList<TreeNode>();
    }

    public TreeNode(int x, int y, TreeNode parent, double distance) {
        this.x = x;
        this.y = y;
        this.depth = parent.depth + 1;
        this.distance = distance;
        this.parent = parent;
        this.children = new ArrayList<TreeNode>();
    }

    public void addChild(TreeNode child) {
        this.children.add(child);
        return;
    }

    public boolean hasNoChildren() {
        return this.children.isEmpty();
    }

    public String toString() {
        return "(" + this.y + ", " + this.x + ")";
    }
}
