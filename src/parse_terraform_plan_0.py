import json
from typing import Dict, List, Set, Any

def parse_terraform_plan(plan_file: str) -> Dict[str, Set[str]]:
    """
    Parse Terraform plan JSON file and extract resource dependencies.
    
    Args:
        plan_file: Path to the Terraform plan JSON file
        
    Returns:
        Dictionary mapping resource names to their dependencies
    """
    with open(plan_file, 'r') as f:
        plan_data = json.load(f)
    
    dependencies: Dict[str, Set[str]] = {}
    
    # Extract resource changes
    for change in plan_data.get('resource_changes', []):
        resource_name = change['address']
        dependencies[resource_name] = set()
        
        # Parse dependencies from change metadata
        if 'depends_on' in change:
            for dep in change['depends_on']:
                # Extract resource name from dependency reference
                if 'resource.' in dep:
                    dep_resource = dep.split('.')[-1]
                    dependencies[resource_name].add(dep_resource)
        
        # Parse provider dependencies
        if 'provider' in change:
            provider_ref = change['provider']
            dependencies[resource_name].add(provider_ref)
    
    return dependencies
