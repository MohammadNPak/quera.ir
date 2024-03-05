# https://quera.org/problemset/220672


class InvalidMovieTitle(BaseException):
    def __str__(self):
        return "invalid title"

class InvalidMovieDate(BaseException):
    def __str__(self) -> str:
        return "invalid date"

class InvalidMovieQuality(BaseException):
    def __str__(self) -> str:
        return "invalid quality"

class InvalidMovieId(BaseException):
    def __str__(self) -> str:
        return "invalid movie id"

class InvalidCastName(BaseException):
    def __str__(self) -> str:
        return "invalid name"

class InvalidCastId(BaseException):
    def __str__(self) -> str:
        return "invalid cast id"

class AlreadyLink(BaseException):
    def __str__(self) -> str:
        return "already linked"


class Movie:
    last_id=0
    objects={}

    def __init__(self,title,date,quality):
        date=int(date)
        Movie.validate(title,date,quality)
        self.title=title
        self.date=date
        self.quality=quality
        self.casts = []
        self.id = Movie.last_id
        Movie.last_id+=1
        Movie.objects[self.id]=self
        
    @staticmethod
    def validate(title,date,quality):
        if len(title)>20:
            raise InvalidMovieTitle
        if not 1888<=date<=2024:
            raise InvalidMovieDate
        if quality not in ["720p","1080p","4K"]:
            raise InvalidMovieQuality
    
    @classmethod
    def remove(cls,id):
        if not id in Movie.objects:
            raise InvalidMovieId
        
        movie= cls.objects.pop(id)
        for cast_id in movie.casts:
            Cast.objects[cast_id].movies.remove(id)
        return movie

    @classmethod
    def get(cls,id):
        if id not in cls.objects:
            raise InvalidMovieId
        return cls.objects[id]
    
    def __str__(self) -> str:
        return f'{{title:"{self.title}", \
date:"{self.date}", \
quality:"{self.quality}", \
casts:{list(sorted(self.casts))}}}'

    @classmethod
    def filter(cls,pattern,by):
        if by=="title":
            return list(sorted([
                x.id for x in cls.objects.values()
                  if x.title.startswith(pattern)]))
        
        elif by=="quality":
            return list(sorted([
                x.id for x in cls.objects.values()
                  if x.quality == pattern]))
            
        elif by=="date":
            ineq,n=pattern
            if ineq=="=":
                ineq="=="

            return list(sorted([
                x.id for x in cls.objects.values()
                  if eval(f"{x.date}{ineq}{n}") ]))
        else:
            raise Exception("invalid by parameter")



class Cast:
    last_id=0
    objects = {}

    def __init__(self,name) -> None:
        Cast.validate(name)
        self.name=name
        self.movies=[]
        self.id = Cast.last_id
        Cast.last_id+=1
        Cast.objects[self.id]=self


    @staticmethod
    def validate(name):
        if len(name)>20:
            raise InvalidCastName
        if not name.isalpha():
            raise InvalidCastName
    
    @classmethod
    def remove(cls,id):
        if not id in cls.objects:
            raise InvalidCastId
        cast= cls.objects.pop(id)
        for movie_id in cast.movies:
            Movie.objects[movie_id].casts.remove(id)
        return cast
    
    @classmethod
    def get(cls,id):
        if id not in cls.objects:
            raise InvalidCastId
        return cls.objects[id]
    
    def __str__(self) -> str:
        return f'{{name:"{self.name}", \
movies:{list(sorted(self.movies))}}}'


def link(cast_id,movie_id):

    cast_id,movie_id = int(cast_id),int(movie_id)
    cast = Cast.get(cast_id)
    movie = Movie.get(movie_id)
    if cast_id in movie.casts or movie_id in cast.movies:
        raise AlreadyLink
    cast.movies.append(movie.id)
    movie.casts.append(cast.id)


n = int(input())
for i in range(n):
    try:
        command,*data = input().split()
        if command=="ADD-MOVIE":
            movie=Movie(*data)
            print(f"added successfully {movie.id}")
        elif command=="REM-MOVIE":
            movie=Movie.remove(int(data[0]))
            print(f"removed successfully {movie.id}")
        elif command == "ADD-CAST":
            cast = Cast(data[0])
            print(f"added successfully {cast.id}")
        elif command=="REM-CAST":
            cast = Cast.remove(int(data[0]))
            print(f"removed successfully {cast.id}")
        elif command=="SHOW-MOVIE":
            movie = Movie.get(int(data[0]))
            print(movie)
        elif command=="SHOW-CAST":
            cast = Cast.get(int(data[0]))
            print(cast)
        elif command=="LINK-CAST-TO-MOVIE":
            link(*data)
            print(f"successfully linked {data[0]} to {data[1]}")
        elif command == "FILTER-MOVIES-BY-TITLE":
            print(Movie.filter(data[0],"title"))
        elif command=="FILTER-MOVIES-BY-DATE":
            print(Movie.filter(data,"date"))
        elif command=="FILTER-MOVIES-BY-QUALITY":
            print(Movie.filter(data[0],"quality"))

    except BaseException as e:
        print(e)
