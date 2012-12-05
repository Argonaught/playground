CC 		= gcc
CFLAGS		= -Wall -Wextra -nostdlib -fno-builtin -nostartfiles -nodefaultlibs
LD		= ld

OBJFILES	= ../build/loader.o ../build/kernel.o

all: 		../bin/kernel.img

../build/%.o: 	%.s	
	as -o $@ $<

../build/%.o: 	%.c	
	$(CC) $(CFLAGS) -o $@ $<

../bin/kernel.bin: 	$(OBJFILES)
	$(LD) -T linker.ld -o $@ $^

../bin/kernel.img:	../bin/kernel.bin
	dd if=/dev/zero of=../build/pad bs=1 count=750
	cat ../lib/grub/stage1 ../lib/grub/stage2 ../build/pad $< > $@

clean:
	$(RM) ../build/* ../bin/kernel.bin ../bin/kernel.img

install:
	$(RM) ../build/* ../bin/kernel.bin 
