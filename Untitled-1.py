def tower_of_hanoi(n,A,B,C):
    if(n==1):
      print(f"move{n} from {A} to {C}")
      return
    tower_of_hanoi(n-1,A,C,B)
    print(f"move{n} from {A} to {C}")
    tower_of_hanoi(n-1,B,A,C)

if __name__=="__main__":
    print("enter no of disks")
    n=int(input())
    A=1
    B=2
    C=3
    tower_of_hanoi(n,A,B,C)
    