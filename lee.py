import glob

def filesearch(word=""):
    """Returns a list with all files with the word/extension in it"""
    file = []
    for f in glob.glob("*"):
        if word[0] == ".":
            if f.endswith(word):
                file.append(f)
                return file
        elif word in f:
            file.append(f)
            return file
    return file

lookfor = "example", ".py"
for w in lookfor:
    print(f"{w:10} found => {filesearch(w)}")
