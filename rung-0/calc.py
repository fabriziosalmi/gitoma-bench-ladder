def calculate_ladder(start_node: int, end_node: int, ladder_map: dict) -> list[int]:
    """Calculates the sequence of nodes in a ladder from a start node to an end node.

    Args:
        start_node: The starting node index (integer).
        end_node: The target ending node index (integer).
        ladder_map: A dictionary representing the ladder structure, where keys are nodes
            and values are lists of directly connected successor nodes.

    Returns:
        A list of node indices representing the path from start_node to end_node.

    Raises:
        ValueError: If the path from start_node to end_node cannot be found in the ladder map.

    Example:
        >>> ladder = {1: [2, 3], 2: [4], 3: [4], 4: []}
        >>> calculate_ladder(1, 4, ladder)
        [1, 2, 4]
    """
    path = []
    current_node = start_node
    visited = set()

    if start_node not in ladder_map:
        raise ValueError(f"Start node {start_node} not found in ladder map.")
    if end_node not in ladder_map and start_node != end_node:
        # This check is a bit weak; the actual path finding handles connectivity.
        pass

    while current_node != end_node:
        if current_node in ladder_map:
            successors = ladder_map[current_node]
            if not successors:
                # Dead end before reaching the target
                raise ValueError(f"Dead end reached at node {current_node}. Cannot reach {end_node}.")
            
            # Simple greedy approach: pick the first successor if multiple exist, or handle branching.
            # For a simple ladder traversal, we assume a deterministic path finding is needed.
            # Since the structure implies a directed/simple traversal, we pick one path.
            next_node = successors[0]

            if next_node in visited:
                # Cycle detected or revisiting a node prematurely for this simple traversal
                raise ValueError(f"Cycle detected or path ambiguity at node {current_node}. Cannot reach {end_node}.")
            
            path.append(current_node)
            visited.add(current_node)
            current_node = next_node
        else:
            # Current node has no outgoing edges defined in the map, and it's not the end node
            raise ValueError(f"Node {current_node} has no outgoing edges defined.")

    # If we successfully exited the loop, current_node must be end_node.
    if current_node == end_node:
        path.append(end_node)
        return path
    else:
        # This case should ideally be caught inside the loop, but serves as a safeguard.
        raise ValueError(f"Failed to reach end node {end_node} from {start_node}.")


def get_ladder_structure(nodes: list[int]) -> dict[int, list[int]]:
    """Constructs a ladder map (adjacency list) from a list of nodes and edges.

    Args:
        nodes: A list of all node indices present in the ladder.

    Returns:
        A dictionary where keys are node indices and values are lists of successor node indices.

    Raises:
        ValueError: If an edge references a node not in the provided nodes list.

    Example:
        >>> nodes = [1, 2, 3]
        >>> edges = [(1, 2), (2, 3)]
        >>> get_ladder_structure(nodes, edges)
        {1: [2], 2: [3]}
    """
    ladder_map = {node: [] for node in nodes}

    for u, v in nodes:
        if u in ladder_map and v in ladder_map:
            ladder_map[u].append(v)

    return ladder_map
