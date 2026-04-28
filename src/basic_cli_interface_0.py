#!/usr/bin/env python3
import argparse
import sys
from typing import Optional

def main() -> int:
    parser = argparse.ArgumentParser(description='Convert Terraform plan to graph')
    parser.add_argument('plan_file', help='Path to Terraform plan file')
    parser.add_argument('--output-format', choices=['dot', 'png', 'svg'], 
                       default='dot', help='Output format (default: dot)')
    
    args = parser.parse_args()
    
    print(f"Processing plan file: {args.plan_file}")
    print(f"Output format: {args.output_format}")
    
    # Placeholder for actual implementation
    return 0

if __name__ == '__main__':
    sys.exit(main())
