#A loader for Grub to hook into. taken from wiki.osdev.org/Bare_Bones
#ostensibly can be used by other boot loaders as it has the multi boot header
.global loader

#this is the boot eader. presumably this creates a load of values that grub reads. 
#TODO find out what these do. probably look up the grub documentation
.set ALIGN,	1<<0
.set MEMINFO,	1<<1
.set FLAGS,	ALIGN | MEMINFO
.set MAGIC,	0x1BADB002
.set CHECKSUM,	-(MAGIC + FLAGS)

.align 4
.long MAGIC
.long FLAGS
.long CHECKSUM

#set up the stack
.set STACKSIZE, 0x4000
.lcomm stack, STACKSIZE             #, 32 		#why the align param? (3rd param 32)
#reserve memorey for these in the .bss section. this will be available in the kernel.c 
.comm mdb, 4
.comm magic, 4

loader:
	movl $(stack + STACKSIZE), %esp
	movl %eax, magic		#get the magic number passed from grub?
	movl %ebx, mdb			#get the multiboot data structure. again passed from grub I think

	call kmain

	cli				#disable interrupts. find out why.

hang:
	hlt
	jmp hang 			#Just to make sure? we already hit halt no?
