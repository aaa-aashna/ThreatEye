import re

def extract_ips(line):
    return re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)

def read_log(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

        print("[+] Parsing Log File...\n")
        for line in lines:
            ips = extract_ips(line)
            print(f"LOG: {line.strip()}")
            if ips:
                print(f" → Found IP(s): {', '.join(ips)}\n")

    except FileNotFoundError:
        print(f"[-] Log file not found: {filepath}")
    except Exception as e:
        print(f"[-] Error reading log file: {e}")


if __name__ == "__main__":
   read_log("C:/Users/HP/ThreatEye/data/local_logs/dummy_syslog.log")


#Ingesting logs (from file, later maybe real-time stream)
#Sanitizing and printing them

