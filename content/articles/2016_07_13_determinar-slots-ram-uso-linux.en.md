Title: Determining RAM slots in use on Linux
Date: 2016-07-13 20:28
Tags: linux, ram, dmidecode, lshw, hardware, memory
Lang: en
Category: Linux
Slug: determinar-slots-ram-uso-linux
Summary: Linux commands to determine how many RAM slots are occupied and their capacity using dmidecode, lshw, and hardware inspection techniques

How many **RAM slots do you have occupied** and how many are free? Linux provides tools to inspect memory configuration without opening the computer.

## dmidecode: The Main Tool

### Basic Memory Information
```bash
# View all memory information
sudo dmidecode -t memory

# Specific memory type (table 16)
sudo dmidecode -t 16

# Installed sizes only
sudo dmidecode -t memory | grep -i size
```

**Typical Output**:
```
Size: 8192 MB
Size: 8192 MB
Size: No Module Installed
Size: No Module Installed
```

### Detailed Information per Slot
```bash
# Granular information for each slot (table 17)
sudo dmidecode -t 17

# Compact summary
sudo dmidecode -t 17 | grep -E "(Size|Locator|Speed|Type:)"
```

**Information Provided**:
- **Locator**: Physical slot identifier (DIMM_A1, DIMM_B1, etc.)
- **Size**: Installed capacity or "No Module Installed"
- **Type**: DDR3, DDR4, etc.
- **Speed**: Speed in MT/s

## lshw: Alternative with Structured Format

```bash
# Memory information with lshw
sudo lshw -class memory

# Physical memory only (no cache)
sudo lshw -class memory | grep -A 10 "System Memory"

# More compact format
sudo lshw -short -class memory
```

## Useful Scripts for Analysis

### Occupied Slots Counter
```bash
#!/bin/bash
echo "=== RAM Slot Analysis ==="
TOTAL_SLOTS=$(sudo dmidecode -t 17 | grep "Size:" | wc -l)
OCCUPIED_SLOTS=$(sudo dmidecode -t 17 | grep "Size:" | grep -v "No Module" | wc -l)
FREE_SLOTS=$((TOTAL_SLOTS - OCCUPIED_SLOTS))

echo "Total Slots: $TOTAL_SLOTS"
echo "Occupied Slots: $OCCUPIED_SLOTS" 
echo "Free Slots: $FREE_SLOTS"
```

### Detailed Summary
```bash
#!/bin/bash
echo "=== Current RAM Configuration ==="
sudo dmidecode -t 17 | awk '
/Memory Device/,/^$/ {
    if(/Locator:/) locator=$2
    if(/Size:/ && !/No Module/) {
        size=$2" "$3
        print locator": "size
    }
    if(/Size:.*No Module/) print locator": Empty"
}'
```

## Additional Useful Information

### Maximum Supported Capacity
```bash
# Maximum total capacity
sudo dmidecode -t 16 | grep "Maximum Capacity"

# Maximum number of devices
sudo dmidecode -t 16 | grep "Number Of Devices"
```

### Speed and Type Verification
```bash
# Configured speed
sudo dmidecode -t 17 | grep -E "(Speed|Configured)"

# Memory type
sudo dmidecode -t 17 | grep "Type:" | grep -v "Error"
```

## Example of Interpreted Output

```bash
$ sudo dmidecode -t 17 | grep -E "(Locator|Size|Type:)" | head -12

Locator: DIMM_A1
Size: 8192 MB  
Type: DDR4

Locator: DIMM_A2
Size: No Module Installed
Type: Unknown

Locator: DIMM_B1  
Size: 8192 MB
Type: DDR4

Locator: DIMM_B2
Size: No Module Installed
Type: Unknown
```

**Interpretation**: 
- 4 total slots (DIMM_A1, A2, B1, B2)
- 2 slots occupied with 8GB DDR4 each
- 2 free slots available

## Important Limitations

⚠️ **Accuracy**: Command-line tools may not perfectly reflect physical hardware

⚠️ **Privileges**: Root permissions are required to access DMI information

⚠️ **Compatibility**: Some embedded systems may not provide complete information

For **maximum certainty**, physical inspection is still recommended, but these tools provide sufficiently accurate information for most cases.

*Original source*: [Unix & Linux Stack Exchange](http://unix.stackexchange.com/questions/33249/how-to-determine-the-amount-of-ram-slots-in-use)
