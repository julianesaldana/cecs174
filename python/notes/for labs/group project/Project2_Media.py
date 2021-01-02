"""
Julian Saldana, Michael Yi, Triniti Boykin, Robyn Garces

julian (group leader)
- framework for all code
- set up and organization
- contributed to subclasses
- heavily contributed to the subclasses’ methods creation(checkOut/checkIn)

michael
- __repr__ and getting the subclasses to show attributes
- framework for all code
- contributed to work in print formatting
- contributed to subclasses

robyn
- comments
- contributed to debugging entire program
- contributed to Media class
- contributed to counters
- contributed pseudocode

triniti
- comments
- contributed to debugging entire program
- contributed to Media class
- contributed to Member classes
- contributed pseudocode
"""


class Media:
    ctr = 0  # keeps track of total amount of medias if needed.

    def __init__(self, title, author, publisher):  # common attributes in all classes
        self.title = title
        self.author = author
        self.publisher = publisher
        Media.ctr += 1  # increments if media instance is created


class Book(Media):
    ctr = 0  # Keeps track of total number of books checked out

    def __init__(self, title, author, publisher, num_pages):
        super().__init__(title, author, publisher)  # access attributes from parent class
        self.num_pages = num_pages  # specific attribute for books only
        Book.ctr += 1  # counts how many book medias exist

    def __repr__(self):
        return "{} written by {}, published by {}, {} pages".format(self.title, self.author,
                                                                    self.publisher,
                                                                    self.num_pages)  # returns book information


class Video(Media):
    ctr = 0  # counter for how many videos are checked out in total

    def __init__(self, title, author, publisher, run_time):
        super().__init__(title, author, publisher) # access attributes from parent class
        self.run_time = run_time  # adds specific attribute for videos only
        Video.ctr += 1  # counts how many video media instances exist

    def __repr__(self):
        return "{} shot by {}, published by {}, {} minutes long".format(self.title, self.author,
                                                                        self.author,
                                                                        self.run_time)  # returns video information


class Member:
    ctr = 0  # item count
    book_ctr = 0  # books checked out
    video_ctr = 0  # videos checked out
    all_media = {}  # all items checked out

    def __init__(self, name):
        self.name = name
        self.mediactr = 0  # default media counter for each member instance
        Member.ctr += 1  # counting how many member instances are created

    def checkOut(self, media):
        if media not in Member.all_media:
            if self.mediactr < 2:  # check number of items checked out as limit is 2
                if isinstance(media, Book):  # checking media type
                    Member.book_ctr += 1   # counter for book media type
                elif isinstance(media, Video):
                    Member.video_ctr += 1  # counter for video media type
                self.mediactr += 1  # total media count
                Member.all_media[media] = self.name
                print("{}, has checked out: {}\n".format(self.name, media))  # print item information
            else:
                print("Sorry: {}, you have reached the maximum (2) "
                      "amount of items to checkout, so you may not check out: {}.\n".format(self.name, media))
        else:
            print("Sorry: {}, {}, is already checked out by: {}\n".format(self.name, media, Member.all_media[
                media]))  # executes when item is already checked out

    def checkIn(self, media):
        for things, names in Member.all_media.items():
            if things == media:
                Member.all_media.pop(things)  # replace item so the status is not checked out anymore
                print("{}, has checked in {}\n".format(self.name, media))
                break

    def printCheckedOutItems(self):
        print("Items checked out by, {}:".format(self.name))  # prints all items checked out by member
        for medias in Member.all_media:
            if Member.all_media[medias] == self.name:
                if isinstance(medias, Book):  # checks for books checked out
                    print("Book: {}".format(medias))  # prints book information
        for medias in Member.all_media:
            if Member.all_media[medias] == self.name:
                if isinstance(medias, Video):  # checks for videos checked out
                    print("Video: {}".format(medias))  # prints video information
        print()


def displayStats():
    print("********************")   # display all information regarding library
    print("\nRecord of library:\n")
    print("Total number of books = {}\n".format(Book.ctr))
    print("Number of books checked out = {}\n".format(Member.book_ctr))
    print("Total number of videos = {}\n".format(Video.ctr))
    print("Number of videos checked out = {}\n".format(Member.video_ctr))
    print("Total number of members = {}\n".format(Member.ctr))

    print("********************")

    print("\nThe following items are checked out of the library:\n")
    print("Books:")
    for medias in Member.all_media:
        if isinstance(medias, Book):  # shows which member checked out which book
            print("{}, checked out by: {}".format(medias, Member.all_media[medias]))
    print()
    print("Videos:")
    for medias in Member.all_media:
        if isinstance(medias, Video):  # shows which member checked out which video
            print("{}, checked out by: {}".format(medias, Member.all_media[medias]))


book1 = Book("book 1", "author 1", "publisher 1", 100)
book2 = Book("book 2", "author 2", "publisher 2", 200)
book3 = Book("book 3", "author 3", "publisher 4", 300)

video1 = Video("video 1", "author 1", "publisher 1", 100)
video2 = Video("video 2", "author 2", "publisher 2", 200)
video3 = Video("video 3", "author 3", "publisher 1", 300)

Joe = Member("Joe Smith")
Jim = Member("Jim Stuart")

Joe.checkOut(book1)
Joe.checkOut(video1)
Joe.checkOut(book2)
Joe.printCheckedOutItems()

Jim.checkOut(book2)
Jim.checkOut(video1)
Jim.checkOut(video2)
Jim.printCheckedOutItems()

Joe.checkIn(book1)

displayStats()
