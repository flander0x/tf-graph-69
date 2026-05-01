import json
import sys
from typing import Dict, List, Set

def parse_terraform_plan(plan_file: str) -> Dict[str, Set[str]]:
    """
    Parse Terraform plan JSON and extract resource dependencies.
    
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
        
        # Parse dependencies from triggers and references
        if 'change' in change and 'actions' in change['change']:
            # Check for references in the change
            if 'after' in change['change']:
                after = change['change']['after']
                for key, value in after.items():
                    if isinstance(value, str) and '${' in value:
                        # Extract resource references from expressions
                        import re
                        refs = re.findall(r'\$\{([a-zA-Z0-9_]+\.[a-zA-Z0-9_]+)\}', value)
                        dependencies[resource_name].update(refs)
    
    return dependencies

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python parse_terraform_plan_1.py <plan_file.json>")
        sys.exit(1)
    
    deps = parse_terraform_plan(sys.argv[1])
    for resource, deps_list in deps.items():
        print(f"{resource}: {sorted(deps_list)}")
