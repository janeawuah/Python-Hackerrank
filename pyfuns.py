def list_comprehension(x,y,z,n):     
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n])
        

def main():
    x = int(input("Please enter a value for X: "))
    y = int(input("Please enter a value for Y: "))
    z = int(input("Please enter a value for Z: "))
    n = int(input("Please enter a value for N: "))

    list_comprehension(x,y,z,n)
main()