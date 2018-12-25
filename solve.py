from pwn import *

p1 = process('./challenge', env={'LD_PRELOAD':'./libtime.so'})
p1.recv()
p1.sendline('deadbeef')
p1.recvuntil('Key is ')
key = p1.recv()
print key

sleep(3);

p2 = process('./challenge')
p2.sendline(key)
ans = p2.recv()
print ans
