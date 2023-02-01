# Binary clock

The clock for who love binary code :>.

Why this?: Because it's fun =)))).
## How to read the binary clock

The following is a short guide explaining how to read the binary clock.

```
| |   | | < 8
| |   | | < 4
| |   | | < 2
| |   | | < 1
H H : M M < Time Digit
```

Each column represents a single digit. The first two columns are the two hour digits, the next two are the minute digits

The bottom row is the low-order bit, which makes it worth a value of 1. The next row up is worth 2, then 4, followed by 8. Adding up the **on** bits (`*`) gives the value of the digit.

Example of 22h47' is:
```
. .   . .
. .   * *
* *   . *
. .   . *

2 2 : 4 7
```

