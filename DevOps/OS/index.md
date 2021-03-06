# Ubuntu

## Check version
```bash
lsb_release -a
```

## Services
```bash
# List all services
service --status-all
ls /etc/init.d/
ls /etc/rc*.d/
```


## Performances
```bash
# Check directory used space
du -h --max-depth=1 | sort -g

# Check disk space
df -h

# Check RAM
free -m

# GUI RAM monitor
sudo apt-get install htop
htop
```

### Alias and useful commands

```bash
# Sorted list of memory usage
alias dirsorted='du -h --max-depth=1 | sort -g'
alias memsorted='ps -o pid,user,%mem,command ax | sort -b -k3 -r | less'
```

## Ubuntu directory structure
1. / – Root
2. /bin – User Binaries
3. /sbin – System Binaries
4. /etc – Configuration Files
5. /dev – Device Files
6. /proc – Process Information
7. /var – Variable Files
8. /tmp – Temporary Files
9. /usr – User Programs
10. /home – Home Directories
11. /boot – Boot Loader Files
12. /lib – System Libraries
13. /opt – Optional add-on Applications
14. /mnt – Mount Directory
15. /media – Removable Media Devices
16. /srv – Service Data
