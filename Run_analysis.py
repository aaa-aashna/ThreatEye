import argparse
import os
from colorama import init

# Assuming correlate_logs is in core/correlate.py
from core.correlate import correlate_logs

init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="ThreatEye Log Analyzer")

    parser.add_argument(
        "--log", 
        required=True, 
        help="Path to the syslog file"
    )
    parser.add_argument(
        "--feed", 
        required=True, 
        help="Path to the threat feed JSON"
    )
    parser.add_argument(
        "--out", 
        default="output/alerts.log", 
        help="Path to output the alerts log file"
    )

    args = parser.parse_args()

    # Call the correlate function
    correlate_logs(args.log, args.feed, args.out)

if __name__ == "__main__":
    main()
