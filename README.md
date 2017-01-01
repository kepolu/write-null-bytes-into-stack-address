# write-null-bytes-into-stack-address

from nergal's phrack article p58-0x4, he said that...

"One problem remains: passing to a function an argument which
contains 0. But when multiple function calls are available, there is a
simple solution. The first few called functions should insert 0s into the
place occupied by the parameters to the next functions.

  Strcpy is the most generic function which can be used. Its second
argument should point to the null byte (located at some fixed place,
probably in the program image), and the first argument should point to the
byte which is to be nullified. So, thus we can nullify a single byte per a
function call. If there is need to zero a few int32 location, perhaps other
solutions will be more space-effective. For example,
sprintf(some_writable_addr,"%n%n%n%n",ptr1, ptr2, ptr3, ptr4); will nullify
a byte at some_writable_addr and nullify int32 locations at ptr1, ptr2,
ptr3, ptr4. Many other functions can be used for this purpose, scanf being
one of them (see [5]).

  Note that this trick solves one potential problem. If all libraries
are mmapped at addresses which contain 0 (as in the case of Solar
Designer non-exec stack patch), we can't return into a library directly,
because we can't pass null bytes in the overflow payload. But if strcpy (or 
sprintf, see [3]) is used by the attacked program, there will be the 
appropriate PLT entry, which we can use. The first few calls should be the
calls to strcpy (precisely, to its PLT entry), which will nullify not the 
bytes in the function's parameters, but the bytes in the function address 
itself. After this preparation, we can call arbitrary functions from 
libraries again."

choose base stack address ( use 'info proc mappings' in gdb or 'pmap `pidof <your-running-binary>`' ) which has writable flag.
Add it with your custom offset ( assume it will contains the last 1-byte LSB (Least Significant Byte) ) and continue with 3-bytes next.

NB: ASLR must be off, because when it's on, it will be randomize stack base address each execution.. cheers.. :)
