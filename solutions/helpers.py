
def read(filepath):
    with open(filepath) as f:
        line = f.readline().split()
        B = int(line[0])
        L = int(line[1])
        D = int(line[2])
        scores = [int(i) for i in f.readline().split()]

        libraries = []


        for l in range(L):
            line = f.readline().split()
            N = int(line[0])
            T = int(line[1])
            M = int(line[2])
            books = [int(i) for i in f.readline().split()]
            libraries.append([l,N,T,M,books])
        return B,L,D,scores,libraries


def output(libraries, path="output.txt"):
    #libraries = [[id, [book1,book2,...]] , [id, [book1,book2,...]]]
    outstring = str(len(libraries)) + "\n"
    for lib in libraries:
        outstring += str(lib[0]) + " " + str(len(lib[1])) + "\n"
        for book in lib[1]:
            outstring += str(book) + " "
        outstring+="\n"

    f = open(path, "w+")
    f.write(outstring)
    f.close()


def get_points(library, book_scores):
    #scores = scores
    points = 0
    for book in library[4]:
        points += book_scores[book]
    return points

# returns book points
def get_book_point_lib(libraries, scores):
    books = {}
    covered_books = set()
    i = 0 # index of book we're at
    for library in libraries:
        points = 0
        for book in library[4]:
            if book not in covered_books:
                covered_books.add(book)
                books[book] = scores[i]
                i+=1
    return books
