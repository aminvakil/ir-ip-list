import sys
import ipaddress

output = [] if len(sys.argv) == 2 else None
input_file = open(sys.argv[1]) if output is not None else sys.stdin

for line in input_file:
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
                    if output is None:
                        print(sub)
                    else:
                        output.append(str(sub))
            else:
                if output is None:
                    print(cidr)
                else:
                    output.append(str(cidr))
    else:
        # Pass existing CIDR lines through as-is
        if output is None:
            print(line)
        else:
            output.append(line)

if output is not None:
    input_file.close()
    with open(sys.argv[1], 'w') as file:
        file.write('\n'.join(output))
        file.write('\n')
