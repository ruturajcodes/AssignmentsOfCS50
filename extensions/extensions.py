def main():
    extension = input("File name: ").strip().lower().split(".")
    # print(extension[:])
    size = len(extension[-1])
    last = extension[-1]
    # print(extension[-1])

    if size == 3:
        for_ext3(last)
    else:
        for_ext4(last)

def for_ext3(last):
    if "gif" in last:
        print("image/gif")

    elif "jpg" in last:
        print("image/jpeg")

    elif "png" in last:
        print("image/png")

    elif "txt" in last:
        print("text/plain")
    elif "pdf" in last:
        print("application/pdf")
    elif "zip" in last:
        print("application/zip")
    else:
        print("application/octet-stream")

def for_ext4(last):
    if "jpeg" in last:
        print("image/jpeg")
    else:
        print("application/octet-stream")

main()