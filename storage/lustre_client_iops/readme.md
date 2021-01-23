## why client_iops.py for lustre client
- lustre 2.12.2 does not support collectl
- collectl for lustre 2.8.0 does not provide iops data other than writes/reads
  - e.g., when open/close/etc. are needed

## how
- python2/python3 client_iops.py

## to improve
- automatically locate the log file instead of hard coding
- sampling inverval configurable

## sample md_stats
```
snapshot_time             1611379935.686576 secs.usecs
read_bytes                24171493 samples [bytes] 1 880033224 265110931821
write_bytes               2238386 samples [bytes] 1 464312015 92635949694
ioctl                     3453472 samples [regs]
open                      24954124 samples [regs]
close                     24949831 samples [regs]
mmap                      26496911 samples [regs]
seek                      417608264 samples [regs]
fsync                     578 samples [regs]
readdir                   8805354 samples [regs]
setattr                   989375 samples [regs]
truncate                  52731 samples [regs]
flock                     30 samples [regs]
getattr                   353538590 samples [regs]
link                      270358 samples [regs]
unlink                    588626727 samples [regs]
symlink                   38561 samples [regs]
mkdir                     110032 samples [regs]
rmdir                     361281 samples [regs]
rename                    37362 samples [regs]
statfs                    1084004 samples [regs]
alloc_inode               610726029 samples [regs]
setxattr                  206715 samples [regs]
getxattr                  2766603 samples [regs]
getxattr_hits             86 samples [regs]
listxattr                 200968 samples [regs]
removexattr               989097 samples [regs]
inode_permission          5952672345 samples [regs]
```
