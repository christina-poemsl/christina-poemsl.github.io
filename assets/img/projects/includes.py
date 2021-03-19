import numpy as np

import sys
import os

TEMPLATE = """
{{% include image.html image="projects/{folder}/{fn}" %}}
<p align="center">{desc}</p>
"""

def main():
    
    folder = sys.argv[1].rstrip("/")
    includes, nums = [], []
    
    for fn in os.listdir(folder):

        if fn != "thumb.jpg":
            
            splits = fn[:-4].split("_")

            try:
                num = int(splits[0])
            except:
                continue

            if len(splits) == 4:
                desc = "{}, {}, {}".format(*splits[1:])
            elif len(splits) == 3:
                desc = "{} {}".format(*splits[1:])

            includes.append(TEMPLATE.format(folder=folder, fn=fn, desc=desc))
            nums.append(int(num))


    ics = np.argsort(nums)

    for ix in ics:
        print(includes[ix])    

if __name__ == "__main__":
    main()
