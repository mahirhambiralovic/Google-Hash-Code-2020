import helpers as h

def main():
    B,L,D,scores,libraries = h.read("../data/e_so_many_books.txt") # libraries is [id,NBooks,TDays,MShipsperday,[books]]
    # TODO Call get_points
    book_scores = get_book_point_lib(libraries,scores)

    #list.sort(libraries, key=lambda library:get_points(library,book_scores), reverse=True)
    tot_points = 0
    # sort books by value and at total points to calculate average
    for lib in libraries:
        list.sort(lib[4], key=lambda book:book_scores[book], reverse=True)
        tot_points += get_points(lib, book_scores)
    average_points = tot_points/L
    list.sort(libraries, key=lambda library:get_points2(library, book_scores, average_points), reverse=True)
    ansLibs = []

    day = 0
    new_libraries = []
    for lib in libraries:
        day_local = day + lib[2] # Add time to set up
        books_to_scan = []
        while day_local < D:
            list.sort(lib[4], key=lambda book:book_scores[book], reverse=True) #sort
            books_to_scan.append(lib[4][0:lib[2]])
            for i in range(lib[2]):
                if i < len(lib[4]):
                    books_to_scan.append(lib[4][i])
                    book_scores[lib[4][i]] = 0
            day_local += lib[2] #iterate over days
        new_libraries.append([lib[0],books_to_scan])


    #print("Days total are: " + str(D))
    for i in range(int((L-1)/2)):
         lib = new_libraries[2*i]
         ansLibs.append([lib[0], lib[4]])
    h.output(ansLibs, "../outputs/E_v1.txt")
    #print(outstring)

def get_points2(library, book_scores, average_points):
    #scores = scores
    points = 0
    for book in library[4]:
        points += book_scores[book]
    points *= library[3]
    points -= average_points*library[2]
    return points


def get_points(library, book_scores):
    #scores = scores
    points = 0
    for book in library[4]:
        points += book_scores[book]
    return points

#returns book scores
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


def get_days(lib):
    return lib[2]

if __name__ == "__main__":
    main()
