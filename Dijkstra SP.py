def dijkstra(graf, mulai):
    jarak = {simpul: float('inf') for simpul in graf}
    jarak[mulai] = 0
    kunjungan = set()

    while len(kunjungan) < len(graf):
        simpul_sekarang = min((jarak[simpul], simpul) for simpul in graf if simpul not in kunjungan)[1]
        kunjungan.add(simpul_sekarang)

        for tujuan, bobot in graf[simpul_sekarang].items():
            if jarak[simpul_sekarang] + bobot < jarak[tujuan]:
                jarak[tujuan] = jarak[simpul_sekarang] + bobot

    return jarak

if __name__ == "__main__":
    graf = {
        'A': {'B': 14, 'D': 12, 'F': 10},
        'B': {'A': 14, 'C': 17, 'D': 20, 'E': 15, 'F': 18},
        'C': {'B': 17, 'E': 13},
        'D': {'A': 12, 'B': 20, 'E': 16, 'F':11},
        'E': {'B': 15, 'C': 13, 'D': 16, 'F': 11},
        'F': {'A': 10, 'B': 18, 'D': 11, 'E':11}
    }
    mulai_simpul = 'D'
    shortest_distances = dijkstra(graf, mulai_simpul)
    print("\n","Jarak terpendek dari simpul {}: ke C adalah :".format(mulai_simpul), shortest_distances['C'], "\n")