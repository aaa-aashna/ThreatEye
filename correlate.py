import json
import re
#Scan system logs for any IP addresses that match known malicious IPs from a threat feed


def load_threat_feed(path):
    with open(path, 'r') as f:
        return json.load(f)

def extract_ips(line):
    return re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)

def correlate_logs(log_path, feed_path):
    feed = load_threat_feed(feed_path)
    malicious_ips = set(feed["malicious_ips"])

    with open(log_path, 'r') as f:
        lines = f.readlines()

    print("[+] Correlating log with threat feed...\n")
    for line in lines:
        ips = extract_ips(line)
        for ip in ips:
            if ip in malicious_ips:
                print(f"[ALERT]  Match found: {ip}")
                print(f"   → Log Entry: {line.strip()}\n")


if __name__ == "__main__":
    correlate_logs("data/local_logs/dummy_syslog.log", "data/threat_feed.json")
