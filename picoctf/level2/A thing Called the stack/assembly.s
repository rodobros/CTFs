foo:
    pushl %ebp            # esp - 4
    mov %esp, %ebp        
    pushl %edi            # esp - 4
    pushl %esi            # esp - 4
    pushl %ebx            # esp - 4
    sub $0x12c, %esp      # esp - 300
    movl $0x1, (%esp)     
    movl $0x2, 0x4(%esp)
    movl $0x3, 0x8(%esp)
    movl $0x4, 0xc(%esp)
