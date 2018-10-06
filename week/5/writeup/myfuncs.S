section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

        ;your code goes here!

        mov     qword  [rbp-24], rdi ; move dst copy ptr to stack
        mov     eax, esi             ; move src copy ptr to eax
        mov     dword  [rbp-32], edx ; copy final index
        mov     byte  [rbp-28], al   ; copy byte to set to over
        mov     dword  [rbp-4], 0    ; initialize counter
.msloop:
        mov     eax, dword  [rbp-4]  ; move counter to eax
        cmp     eax, dword  [rbp-32] ; check if counter == target index
        je      .exit                ; jmp to exit if so
        mov     edx, dword  [rbp-4]  ; otherwise move counter back to eax
        mov     rax, qword  [rbp-24] ; move dst address to rax
        add     rdx, rax             ; inc dst address
        movzx   eax, byte  [rbp-28]  ; move byte to copy into eax 
        mov     byte  [rdx], al      ; move byte to copy into memory ptr @ rdx
        add     dword  [rbp-4], 1    ; increment counter
        jmp     .msloop
.exit:
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame
        mov     qword [rbp-24], rdi ; put dst copy ptr to stack
        mov     qword [rbp-32], rsi ; put src ptr to stack
        mov     dword [rbp-36], edx ; copy final index/size
        mov     dword [rbp-4], 0    ; set i = 0
.scloop:
        mov     edx, dword [rbp-4]  ; move current counter to eax
        mov     rax, qword [rbp-32] ; load src ptr
        add     rax, rdx            ; increment src ptr
        mov     rcx, rdx            ; move src ptr to rcx
        mov     rdx, qword [rbp-24] ; copy dst ptr to rdx
        add     rdx, rcx            ; switcheroo
        movzx   eax, byte [rax]     ; grab the pertinent byte
        mov     byte [rdx], al      ; more byte grabbing
        add     dword [rbp-4], 1    ; add 1 to the index
.check:
        mov     eax, dword [rbp-4]  ; move final index/size to eax
        cmp     eax, dword [rbp-36] ; check if we're done
        jl      .scloop             ; loop again if not
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
