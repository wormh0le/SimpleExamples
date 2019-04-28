inp =input("Enter Info: ").strip()

with open("demo.save","w") as f:
 f.write(inp)
 f.close()

with open("demo.save","r") as f:
 print(f.read())
 f.close()