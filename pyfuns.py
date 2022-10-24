def list_comprehension(x,y,z,n):     
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n])
        


# Function to find the runnerup score
def runnnerup_score(arr_of_scores):
    # for i in arr_of_scores:
    #     print (i)
    # arr = set(map(int, input().split()))
    arr_of_scores = set(arr_of_scores)
    arr_of_scores = sorted(arr_of_scores)
    print(arr_of_scores[-2])
    



# Main function
def main():
    # for list comprehension
    # x = int(input("Please enter a value for X: "))
    # y = int(input("Please enter a value for Y: "))
    # z = int(input("Please enter a value for Z: "))
    # n = int(input("Please enter a value for N: "))

    # list_comprehension(x,y,z,n)

# ------------------------------------------------------------------------------------------------------------------------------------
    # for runnerup_score
    an_array = [2,3,6,6,5]
    runnnerup_score(an_array)

main()