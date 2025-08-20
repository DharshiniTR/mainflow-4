import re
from collections import defaultdict, Counter
from datetime import datetime
import os

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        self.date_pattern = r'\[\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4}\]'
        self.request_pattern = r'"(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH) (.+?) HTTP/\d\.\d"'
        self.status_pattern = r' \d{3} '

    def parse_logs(self):
        """Parse the log file and extract relevant information"""
        data = {
            'ip_counts': defaultdict(int),
            'status_counts': defaultdict(int),
            'url_counts': defaultdict(int),
            'hourly_counts': defaultdict(int),
            'total_requests': 0
        }
        
        with open(self.log_file, 'r') as file:
            for line in file:
                data['total_requests'] += 1
                
                # Extract IP address
                ip_match = re.search(self.ip_pattern, line)
                if ip_match:
                    data['ip_counts'][ip_match.group()] += 1
                
                # Extract status code
                status_match = re.search(self.status_pattern, line)
                if status_match:
                    status = status_match.group().strip()
                    data['status_counts'][status] += 1
                
                # Extract URL
                request_match = re.search(self.request_pattern, line)
                if request_match:
                    data['url_counts'][request_match.group(2)] += 1
                
                # Extract hour of the day
                date_match = re.search(self.date_pattern, line)
                if date_match:
                    date_str = date_match.group()[1:-1]
                    try:
                        dt = datetime.strptime(date_str, '%d/%b/%Y:%H:%M:%S %z')
                        data['hourly_counts'][dt.hour] += 1
                    except ValueError:
                        pass
        
        return data
    
    def analyze(self, top_n=10):
        """Analyze the log data and return formatted results"""
        data = self.parse_logs()
        
        # Get top IPs
        top_ips = Counter(data['ip_counts']).most_common(top_n)
        top_status = Counter(data['status_counts']).most_common()
        top_urls = Counter(data['url_counts']).most_common(top_n)

        print("Total Requests:", data['total_requests'])
        print("\nMost Frequent IP Addresses:")
        for ip, count in top_ips:
            print(f"{ip}: {count}")

        print("\nResponse Codes:")
        for code, count in top_status:
            print(f"{code}: {count}")

        print("\nMost Accessed URLs:")
        for url, count in top_urls:
            print(f"{url}: {count}")

def main():
    log_file = input("Enter the path to the log file: ")
    
    # Check file size
    if os.path.getsize(log_file) > 100 * 1024 * 1024:  # 100 MB
        print("Error: Log file exceeds 100 MB limit.")
        return
    
    analyzer = LogAnalyzer(log_file)
    analyzer.analyze()

if __name__ == "__main__":
    main()
