import json
from typing import Dict, List, Set, Tuple

def parse_terraform_plan(plan_file: str) -> Dict[str, Set[str]]:
    """
    Parse Terraform plan JSON and extract resource dependencies.
    
    Args:
        plan_file: Path to the Terraform plan JSON file
        
    Returns:
        Dictionary mapping each resource to its dependencies
    """
    with open(plan_file, 'r') as f:
        plan = json.load(f)
    
    dependencies: Dict[str, Set[str]] = {}
    
    # Extract resource changes
    for change in plan.get('resource_changes', []):
        resource = change['address']
        dependencies[resource] = set()
        
        # Parse depends_on
        for dep in change.get('depends_on', []):
            dependencies[resource].add(dep)
        
        # Parse provider dependencies
        for provider in change.get('provider', []):
            dependencies[resource].add(provider)
    
    # Add relationships between resources based on references
    for change in plan.get('resource_changes', []):
        resource = change['address']
        change_info = change.get('change', {})
        
        # Parse references in actions
        if 'actions' in change_info:
            for action in change_info['actions']:
                if isinstance(action, dict):
                    for key, value in action.items():
                        if isinstance(value, dict) and 'references' in value:
                            for ref in value['references']:
                                if ref != resource:
                                    dependencies[resource].add(ref)
    
    return dependencies

def build_dependency_graph(dependencies: Dict[str, Set[str]]) -> Dict[str, List[str]]:
    """
    Convert dependency dictionary to adjacency list format for graphing.
    
    Args:
        dependencies: Dictionary mapping resources to their dependencies
        
    Returns:
        Adjacency list representation of the dependency graph
    """
    graph = {}
    for resource, deps in dependencies.items():
        graph[resource] = list(deps)
    return graph
