from ast import List
from typing import Optional


class Brano:
    def __init__(self, titolo: str, autore: str, durata: int) -> None:
        self.titolo = titolo
        self.autore = autore
        self.durata = durata

    def titolo(self) -> str:
        return self._titolo

    def titolo(self, valore: str) -> None:
        if not valore:
            raise ValueError("Il titolo non può essere vuoto")
        self._titolo = valore

    def autore(self) -> str:
        return self._autore

    def autore(self, valore: str) -> None:
        if not valore:
            raise ValueError("L'autore non può essere vuoto")
        self._autore = valore

    def durata(self) -> int:
        return self._durata

    def durata(self, valore: int) -> None:
        if valore <= 0:
            raise ValueError("La durata deve essere positiva")
        self._durata = valore

    def short_song(self) -> bool:
        return self.durata <= 180

    def __str__(self) -> str:
        return f"{self.titolo} - {self.autore} ({self.durata} secondi)"


class Playlist:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.brani = [] 

    def aggiungi_brano(self, brano: Brano) -> None:
        self.brani.append(brano)

    def durata_totale(self) -> int:
        return sum(brano.durata for brano in self.brani)

    def __str__(self) -> str:
        return f"Playlist: {self.nome} ({len(self.brani)} brani)"


class CD:
    def __init__(self, titolo: str, autore: str, brani: Optional[List[Brano]] = None) -> None:
        self.titolo = titolo
        self.autore = autore
        self.brani = brani if brani is not None else []

    def aggiungi_brano(self, brano: Brano) -> None: 
        self.brani.append(brano)

    def durata_totale(self) -> int:
        totalDuration = 0
        for brano in self.brani:
            totalDuration += brano.durata
        return totalDuration


    def filtra_brani_per_autore(self, autore: str) -> List[Brano]:
        newList = []
        for brano in self.brani:
            if autore == brano.autore:
                newList.append(brano)
        return newList


    def copia_brani(self) -> List[str]:
        newBrani = []
        for brano in self.brani:
            newBrani.append(brano)
        return newBrani
        
    
    def __str__(self) -> str: 
        descrizione = [str(brano) for brano in self.brani]  
        return f"CD: {self.titolo} di {self.autore}\n- " + "\n- ".join(descrizione)


if __name__ == "__main__":
    brano1 = Brano("Opinel", "Simba la Rue", 137)
    brano2 = Brano("Cagoule", "Simba la Rue", 170)
    brano3 = Brano("Ca**i miei", "Simba la Rue", 135)

    print(brano1)
    print(f"E' un brano breve? {brano2.short_song()}")

    cd = CD("SimbaGoated", "Simba la Rue", [brano1, brano2, brano3])
    print(cd)
    print(f"Durata totale: {cd.durata_totale()} secondi")

    playlist = Playlist("Simba4Real")
    playlist.aggiungi_brano(brano1)
    playlist.aggiungi_brano(brano2)
    print(playlist)
    print(f"Durata playlist: {playlist.durata_totale()} secondi")