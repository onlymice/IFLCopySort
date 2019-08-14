# IFLCopy

Just simple Copy/SortByMode Script for the 3ds Max's  .ifl (Image File List)  format

### Requirements

- Python >= 3



### What it can do?

It will copy the original file into buffer then move lines according to the selected **Mode** and save everything as one or multiple files(**Multiple files** if mode with a **copy_on_each** was passed to an arguments)

**Modes**

- **top2bottom** - move specified number of lines from **top** to **bottom** of the selected file
- **bottom2top** -  same as **top2bottom** but flipped lines

- **copy_on_each_top2bottom** - move specified number of lines from  **top** to **bottom** of the selected file and make copy of the file on each line shift ( files would be saved as "out0.ifl", "out1.ifl" and etc...)
- **copy_on_each_bottom2top** - same as **copy_on_each_top2bottom** but flipped lines
- **help** - helpme

### Usage

`python Script.py --lines 1 --mode top2bottom --file test.ifl --output {out.ifl}`

`--lines` - how many lines should be moved {Requires digits as input} (default: 1)

`--file` - file name or path to the .ifl file to make a COPY

`--output` - location of where an output files should be saved

``--mode`` - which mode to use



