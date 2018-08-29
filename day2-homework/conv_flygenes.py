#!/usr/bin/env python3

#Output a new file with ...

import sys

#Read in Map_out.txt file using first argument in command line
map_dict = {}
for line in open(sys.argv[1]):
    prep = line.rstrip("\r\n").split()
#Define your key, which is the Flybase ID in column 1
    key = prep[0]
#Define your value, which is the UniProt ID in column 2
    value = prep[1]
#Tell your dictionary the key and value
    map_dict[key] = value

#Read in t_data.ctab file using standard system in
for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split()
    Flybase_id = fields[8]
    if Flybase_id in map_dict:
        Uniprot_id = map_dict[Flybase_id]
        print(line + "\t" + Uniprot_id)
        if sys.argv[2] == "U":
            print(line + "\t" + "Unknown")
#If user wants "unknown" printed for Flybase IDs that are not in the dictionary, type "U" as second argument in command line
        if sys.argv[2] == "I":
            continue
#If user wants the line ignored for Flybase IDs that are not in the dictionary, type "I" as second argument in command line

#Output file for first 100 lines of "unknown" option called "conv_unknown_100.txt"
#Output file for first 100 lines of "ignored" option called "conv_ignored_100.txt"