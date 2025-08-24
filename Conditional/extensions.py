################################################
# Conditional Statements and Logical Operators
################################################

file_name = input("Enter file name: ").strip().lower()

extension = file_name.rsplit(".")[-1]

if extension == "gif":
    print("image/gif")
elif extension == "jpg" or extension == "jpeg":
    print("image/jpeg")
elif extension == "png":
    print("image/png")
elif extension == "pdf":
    print("application/pdf")
elif extension == "txt":
    print("text/plain")
elif extension == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
