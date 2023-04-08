# Hex Offsets

All offsets are given as relative addresses to the process base address:
```battlefront.exe+<offset>```

## Server Software

### Number of Players on a Server

#### Steam

The number of players on a server is stored in a 32bit integer.
The number of players on a server is given through the number of bits set to 1.

Offsets:
- 0x518740 [4 bytes, 32bit integer]
- 0x518750 [4 bytes, 32bit integer]

### Number of Players joining a Server

#### Steam

The number of players joining a server is stored in a 32bit integer.
The number of players joining a server is given through the number of bits set to 1.

Offsets:
- 0x503FF0 [4 bytes, 32bit integer]
- 0x58A450 [4 bytes, 32bit integer]

### End of Map / Map change

#### Steam

After the current map is over the name of the next map is stored in as a string of size ???.

Offsets:
- 0x4E6D6C [? bytes, char array]
- 0x638FB0 [? bytes, char array]

### Playernames

#### Steam

...

Offsets:
- 0x51107C [? bytes, char array]

