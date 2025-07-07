def read_log(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

        print("[+] Reading Log File...\n")
        for line in lines:
            print(line.strip())

    except FileNotFoundError:
        print(f"[-] Log file not found: {filepath}")
    except Exception as e:
        print(f"[-] Error reading log file: {e}")


if __name__ == "__main__":
    read_log("C:/Users/HP/ThreatEye/data/local_logs/dummy_syslog.log")


#Ingesting logs (from file, later maybe real-time stream)
#Sanitizing and printing them

