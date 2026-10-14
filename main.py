from lesson2_hw import add_player, top_players, average_score, greet, countdown, players
from lesson3_hw import Film, FilmSiyahisi
from lesson4_hw import Mahni, Podcast, Playlist


def main():
    print("DERS 2")
    add_player(players, "Leyla", 250)
    print(top_players(players))
    print(average_score(players))
    print(greet("ali"))
    for number in countdown(3):
        print(number)

    print("\nDERS 3")
    siyahi = FilmSiyahisi()
    siyahi.elave_et(Film.from_string("Inception|2010|8.8"))
    siyahi.elave_et(Film.from_string("Interstellar|2014|8.6"))
    print(len(siyahi))
    print(siyahi.en_yaxsi())
    print(len(set(siyahi.filmler)))

    print("\nDERS 4")
    mahni = Mahni("Yellow", "Coldplay", 269)
    podcast = Podcast("Kosmos", "Elm saati", 1800, 12)
    print(mahni)
    print(podcast)
    print(sorted([mahni, Mahni("Numb", "Linkin Park", 185)]))
    pl1 = Playlist("Birinci")
    pl2 = Playlist("Ikinci")
    pl1.elave_et(mahni)
    pl2.elave_et(podcast)
    print("Yellow" in pl1)
    print(len(pl1 + pl2))
    print(len(pl1))
    print(pl1.elave_olundu())
    print(Playlist.__mro__)


if __name__ == "__main__":
    main()
