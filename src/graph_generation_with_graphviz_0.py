from graphviz import Digraph

def generate_dependency_graph(resources):
    """
    Generate a dependency graph using Graphviz from parsed resources.
    resources: list of dicts with 'name', 'depends_on' keys
    """
    dot = Digraph(comment='Resource Dependency Graph', format='png')
    dot.attr('node', shape='box', style='rounded', fontname='Arial')
    dot.attr('edge', arrowhead='vee', fontname='Arial')

    for resource in resources:
        name = resource['name']
        dot.node(name, name)
        for dep in resource.get('depends_on', []):
            dot.edge(dep, name)

    return dot
