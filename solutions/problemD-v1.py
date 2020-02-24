import helpers


def main():
   B,L,D,scores,libraries = helpers.read('./data/d_tough_choices.txt')
     
   ansLibs = []
    #libraries = [[id, [book1,book2,...]] , [id, [book1,book2,...]]]

   for i in range(0,(L-1)/2):

        lib = libraries[2*i]
        ansLibs.append([lib[0], lib[4]])


   helpers.output(ansLibs, "outputs/D_v1.txt")


if __name__ == "__main__":
    main()
