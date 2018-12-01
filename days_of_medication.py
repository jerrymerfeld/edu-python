#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("Please provide the dose and the total count of medication.\n")
else:
    dose = sys.argv[1]
    total = sys.argv[2]
    days = int(total)/int(dose)
    print(days) 
