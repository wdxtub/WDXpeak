# Jigsaw

Implement an NxN jigsaw puzzle. Design the data structures and explain an algorithm to solve the puzzle. You can assume that you have a fitsWith method which, when passed two puzzle edges, returns true if the two edges belong together.

## Solution

We will need couple of classes to represent this:

+ Piece
+ Edge (contained by Piece)
+ Jigsaw game

First you need a "Piece" class to represent one piece of a puzzle. Each piece has four sides, each one with a unique outline which will only connect to one other piece.

Edge sides have an "edge" outline. Each side also has a piece id attribute called "adjacent" to store the value of the piece it connects to. Piece provides a "rotate" method which turns the piece 90, 180, or 270 degrees.

The "Jigsaw" class has a number of pieces in the puzzle and a container of pieces. The "Solve" method uses a map to store the association of edges to pieces. It iterates through the pieces and for each edge, looks to see if its compliment is in the map. If so, it rotates the new piece to the correct orientation and sets the adjacent fields in the two edges to point at each other. If not, it adds the edge to the map. With one pass through the pieces, it should have all the pieces in the correct orientation and connected to all of the adjacent pieces.

```java
class Edge {
    enum Type {
        inner, outer, flat
    }
  
    Piece parent;
    Type type;
  
    boolean fitsWith(Edge type) {
    }; // Inners & outer fit together.
}
  
class Piece {
    Edge left, right, top, bottom;
  
    // 90, 180, etc
    Orientation solvedOrientation = 90;
}
  
class Puzzle {
    // Remaining pieces left to put away.
    Piece[][] pieces;
    Piece[][] solution;
    Edge[] inners, outers, flats;
  
    // We're going to solve this by working our way
    // in-wards, starting with the corners.
    // This is a list of the inside edges.
    Edge[] exposed_edges;
  
    void sort() {
  
        // Iterate through all edges,
        // adding each to inners, outers, etc,
        // as appropriate.
        // Look for the corners—add those to solution.
        // Add each non-flat edge of the corner
        // to exposed_edges.
  
    }
  
    void solve() {
        for (Edge edge1 : exposed_edges) {
            // Look for a match to edge1
            if (edge1.type == Edge.Type.inner) {
                for (Edge edge2 : outers) {
                    if (edge1.fitsWith(edge2)) {
                        // We found a match!
                        // Remove edge1 from
                        // exposed_edges.
                        // Add edge2's piece
                        // to solution.
                        // Check which edges of edge2
                        // are exposed, and add
                        // those to exposed_edges.
                    }
                }
                // Do the same thing,
                // swapping inner & outer.
            }
        }
    }
}
```

