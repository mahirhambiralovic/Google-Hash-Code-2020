def main():
    outstring = ""
    B,L,D,scores,libraries = read() # libraries is [id,NBooks,TDays,MShipsperday,[books]]
    list.sort(libraries, key=get_days)
    #print("Days total are: " + str(D))
    day = 0
    n_libraries = 0
    for lib in libraries:
        if day < D:
            possible_n_books = len(lib[4]) - day
            id = lib[0]
            outstring += str(id) + " " + str(possible_n_books) + "\n"

            for i in range(len(lib[4]) - day):
                outstring+=str(lib[4][i]) + " "
            outstring += "\n"
            day += lib[2]
            n_libraries +=1
    outstring = str(n_libraries) + "\n" + outstring
    f = open("output.txt","w+")
    f.write(outstring)
    #print(outstring)




def get_days(lib):
    return lib[2]



def read():
    f = open("data/e_so_many_books.txt")
    #f = open("data/a_example.txt")

    line = f.readline().split()
    B = int(line[0])
    L = int(line[1])
    D = int(line[2])
    scores = {int(i) for i in f.readline().split()}

    libraries = []


    for l in range(L):
        line = f.readline().split()
        N = int(line[0])
        T = int(line[1])
        M = int(line[2])
        books = [int(i) for i in f.readline().split()]
        libraries.append([l,N,T,M,books])
    return B,L,D,scores,libraries

if __name__ == "__main__":
    main()
