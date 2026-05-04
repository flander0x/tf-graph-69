from graphviz import Digraph
import os

def create_dependency_graph(resources, output_dir="output"):
    """Create dependency graph from parsed resources using Graphviz"""
    dot = Digraph(comment='Dependency Graph')
    dot.attr(rankdir='LR')
    
    # Create nodes for all resources
    for resource in resources:
        dot.node(resource.name, resource.name)
    
    # Create edges for dependencies
    for resource in resources:
        for dependency in resource.dependencies:
            if dependency in [r.name for r in resources]:
                dot.edge(dependency, resource.name)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Render and save graph
    output_path = os.path.join(output_dir, "dependency_graph")
    dot.render(output_path, format='png', cleanup=True)
    
    return output_path + '.png'
