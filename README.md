# A* Algorithm in Python

This code implements the A* algorithm, which can be used to find the shortest path between two points in a graph. This implementation uses a 2D coordinate system to represent the nodes in the graph. This code way not meant to be an a polished software, just a reusable algorithm implementation in python, so you may have to make modifications.

## Usage

1. Input the number of paths, number of nodes, and number of edges in the graph.
2. Input the start and end nodes for each path.
3. Input the x and y coordinates for each node.
4. Input the nodes and weights for each edge.
5. Call the `algorithm` function with the start and end node indices to get the shortest distance between them.

## Input

- `number of paths \n`: number of paths
- `number of nodes \n`: number of nodes
- `number of edges \n`: number of edges

**Paths:**
- `index of start \t index of end` (repeat `number of paths` times)

**Nodes:**
- `x coordinate of node n \t y coordinate of node n` (repeat `number of nodes` times)

**Edges:**
- `index of start \t index of end` (repeat `number of edges` times)

## License

This project is licensed under the terms of the [MIT license](license.md).
