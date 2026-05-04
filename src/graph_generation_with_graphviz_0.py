from graphviz import Digraph
import os

def create_dependency_graph(parsed_resources, output_dir="output"):
    """Create a dependency graph from parsed resources using Graphviz."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    dot = Digraph(comment='Dependency Graph', format='png')
    dot.attr(rankdir='LR')
    
    # Add nodes for each resource
    for resource in parsed_resources:
        dot.node(resource['name'], resource['name'])
    
    # Add edges for dependencies
    for resource in parsed_resources:
        for dependency in resource.get('dependencies', []):
            if dependency in [r['name'] for r in parsed_resources]:
                dot.edge(dependency, resource['name'])
    
    # Render the graph
    output_path = os.path.join(output_dir, 'dependency_graph')
    dot.render(output_path, cleanup=True)
    
    return f"{output_path}.png"
