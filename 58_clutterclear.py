import os
files=os.listdir("clutter")
i=1
for file in files:
    if file.endswith(".png"):
        print(file)
    os.rename("clutter",f"image/{i}.png")
    i+=1