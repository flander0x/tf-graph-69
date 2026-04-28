#!/usr/bin/env python3
"""
Basic CLI interface for tf-graph-69.
Parses Terraform plan file and output format.
"""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Generate a graph from Terraform plan file."
    )
    parser.add_argument(
        "plan_file",
        type=str,
        help="Path to the Terraform plan file (JSON format)"
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["png", "pdf", "svg", "dot"],
        default="png",
        help="Output format for the graph (default: png)"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="tf_graph",
        help="Output filename (without extension, default: tf_graph)"
    )

    args = parser.parse_args()

    if not args.plan_file:
        print("Error: Plan file path is required.", file=sys.stderr)
        sys.exit(1)

    print(f"Processing plan file: {args.plan_file}")
    print(f"Output format: {args.format}")
    print(f"Output filename: {args.output}.{args.format}")

if __name__ == "__main__":
    main()
