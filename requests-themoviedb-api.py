import requests

class theMovieDb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "48d48d33238ae5be0c44fa5529b37d01"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self,keyword):
        response = requests.get(f"{self.api_url}/search/keyword?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

bilgiler = theMovieDb()

while True:
    secim = input("1- Popular Filmler\n2- Çıkış\nSeçim:")

    if secim == "2":
        break
    else:
        if secim =="1":
            movies = bilgiler.getPopulars()
            for movie in movies['results']:
                print(f"Adı: {movie['name']} - Oylama: {movie['vote_average']} - Çıkış Tarihi:{movie['release_date']}")
        
