def hello():
  print("hello user")
hello()
def pack(a,c,e):
  return[a,c,e]
print(pack(2,4,6))  
def eat_lunch(options):
  if len(options) == 0:
    print("My lunchbox is empty")
  else:
    for i in range(len(options)):
      if i == 0:
        print(f"First I eat {options[0]}")
      else:
        print(f"Next I eat {options[i]}")

eat_lunch([])
eat_lunch(["PBNJ"])
eat_lunch(["apple", "PBNJ", "oreos"])
       
