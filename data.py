#!/usr/bin/python3
# Example data.py file
(
    # Title
    "Time of excecution in seconds",
    # Headers
    ["Computer", "mafft", "mrbayes", "build-mplayer", "build-php",
        "compress-gzip", "dcraw", "encode-flac", "gnupg"],
    # Test results for each computer
    {
        "A": [18.95, 42.51, 163.14, 87.3, 22.06, 109.64, 13.86, 14.79],
        "B": [20.81, 49.69, 287.17, 461.28, 19.47, 92.81, 10.68, 28.27],
        "C": [15.2, 800.96, 3.89, 289.57, 16.69, 76.23, 9.34, 17.34],
        "D": [37.45, 50.81, 751.93, 757.42, 33.53, 100.75, 29.2, 15.32]
    },
    # Type of data (LIB | HIB)
    "LIB"
)
