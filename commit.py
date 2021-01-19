import os, sys

commit_message = ""

if len(sys.argv) == 1:
    print("[Syntax] Please use: commit.py <Message>")
    exit()

for arg in enumerate(sys.argv[1:]):
    commit_message = commit_message + str(arg).split(", ")[1].replace("'", "").replace(")", "") + " "

print("[*   ] Add files to git...")
os.system("git add *")

print("[ *  ] Commit files to git...")
os.system('git commit -m "' + commit_message + '"')

print("[  * ] Push files to git...")
os.system("git push")

print("[   *] All files pushed to git!")