import sys
from os.path import splitext
from PIL import Image, ImageOps

acceptable = [".jpg",".png",".jpeg"]

def main():
    check_file()
    try:
        myimage = Image.open(sys.argv[1])  
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # before = Image.open(sys.argv[1], mode='r', formats=None)
    # cropped = ImageOps.fit(sys.argv[1], size = (600,600), method=Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

    tshirt = Image.open("shirt.png")
    tsize = tshirt.size
    # print(size)

    puppet = ImageOps.fit(myimage, size = tsize, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

    puppet.paste(tshirt, tshirt)

    puppet.save(sys.argv[2])


    # Image.paste("shirt.png", box=None, mask=None)










def check_file():
    if len(sys.argv) == 3:
        root_ext1 = splitext(sys.argv[1])
        root_ext2 = splitext(sys.argv[2])

        # if root_ext1[1] == root_ext2[1]
        ext1 = root_ext1[1].lower()
        ext2 = root_ext2[1].lower()
        # print(root_ext1[1])
        # print(root_ext2[1])
        if ext1 and ext2 in acceptable:
            if ext1 != ext2:
                sys.exit("Input and output have different extensions")
        elif ext1 and ext2 not in acceptable:
            sys.exit("Invalid output")

        # if ext1 == ext2:
        #     sys.exit("Extension match!")



    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()