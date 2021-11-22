# IP addresses collected from DNS server
ips = ['117.116.102.108', 
        '97.103.123.100',
        '111.109.97.105',
	'110.95.110.97',
	'109.101.115.95',
	'97.110.100.95',
	'115.101.99.114',
	'101.116.95.103',
	'97.109.101.125']

# parse and change to char
flag = []

for ip in ips:
    # separate the numbers, still strings
    nums = ip.split('.')
    for num in nums:
        flag.append(chr(int(num)))

print(''.join(flag))
