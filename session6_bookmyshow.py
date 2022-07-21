#Book my show ->data structure for movie ticket booking
#perform oPerations -> 1. Searching 2. sorting   3. filter

movies_in_ludhiana={
    'language1':'English',
    'language2':'Punjabi',
    'movies':[
        {
            'Name':'Khao Peeo Aish Kro',
            'Rating':'83%',
            'Release Date':'7 July 2022',
            'language':'Punjabi'
        },
        {
            'Name':'Captain America',
            'Rating':'91%',
            'Release Date':'19 June 2022',
            'language':'English'
         }
    ]

}

movies_in_chandigarh={
    'language1':'Hindi',
    'language2':'Punjabi',
    'movies':[

        {
            'Name':'Chal Mera Putt 3 ',
            'Rating':'95%',
            'Release Date':'1 may 2022',
            'language':'Punjabi'
         }
    ]

}

movies_in_Delhi={
    'language1':'English',
    'language2':'Hindi',
    'movies':[
        {
            'Name':'Thor',
            'Rating':'90%',
            'Release Date':'30 june 2022',
            'language':'English'
        },
        {'Name':'Article 15  ',
            'Rating':'88%',
            'Release Date':'14 may 2022',
            'language':'Hindi'
         },
        {  'Name':'Badhai Ho  ',
            'Rating':'92%',
            'Release Date':'11 april 2022',
            'language':'Hindi'
         }
    ]

}
#idx          0                   1                     2
#movie lgth   2                1                  3

book_my_show=[movies_in_ludhiana,movies_in_chandigarh,movies_in_Delhi]


def search_movies_by_language(movie_language):

    for idx in range(len(book_my_show)):
        for idx1 in range(len(book_my_show[idx]['movies'])):
            if book_my_show[idx]['movies'][idx1]['language']==movie_language:
                print(book_my_show[idx]['movies'][idx1])
                print("~~~~~~~~~~~~~~")

def sort_cities():
    n = len(book_my_show)
    for idx1 in range(0, len(book_my_show)):
        for idx2 in range(0, n - idx1 - 1):

            if len(book_my_show[idx2]['movies']) > len(book_my_show[idx2 + 1]['movies'] ):
                book_my_show[idx2], book_my_show[idx2 + 1] = book_my_show[idx2 + 1], book_my_show[idx2]




def filter_movies():

    for idx in range(len(book_my_show)):
        for idx1 in range(len(book_my_show[idx]['movies'])):
             print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
             print(book_my_show[idx]['movies'][idx1]['Name'])

             print(book_my_show[idx]['movies'][idx1]['Release Date'])

             print("~~~~~~~~~~~~~~")





#menu driven program
print("Welcome to Book MY Show")
print("~~~~~~~~~~~~~~~~")

choice="yes"

while choice=="yes":

    print("1. Search movies By Language")
    print("2. Sort cities on based on Number of movies in Cineplex")
    print("3. Filter movies to display only Name or Rating")
    option=int(input("enter your choice :(1,2,3)"))

    if option==1:
        print("1. Search movies By Language")
        language=input("Enter the Language ")
        search_movies_by_language(movie_language=language)
    elif option==2:
        print("2. Sort cities on based on Number of movies in Cineplex")
        sort_cities()

        for idx in range(len(book_my_show)):
            print(book_my_show[idx])
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print()

    elif option==3:
        print("3. Filter movies to display only Name or Rating")
        filter_movies()
    else:
        print("Invalid Input")


    choice= input("Yes to continue and No to Quit")

print("Thank you for using Book mY Show")


