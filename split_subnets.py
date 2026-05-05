import sys
import ipaddress

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    if '-' in line:
        start_str, end_str = line.split('-')
        start = ipaddress.IPv4Address(start_str.strip())
        end = ipaddress.IPv4Address(end_str.strip())
        
        # Summarize the IP range into proper CIDR blocks
        for cidr in ipaddress.summarize_address_range(start, end):
            # Split blocks larger than /24 into individual /24 subnets
            if cidr.prefixlen < 24:
                for sub in cidr.subnets(new_prefix=24):
                    print(sub)
            else:
                print(cidr)
    else:
        # Pass existing CIDR lines through as-is
        print(line)
