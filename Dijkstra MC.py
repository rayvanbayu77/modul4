def dijkstra(graf, mulai):
    biaya = {simpul: float('inf') for simpul in graf}
    biaya[mulai] = 0
    kunjungan = set()

    while len(kunjungan) < len(graf):
        simpul_sekarang = min((biaya[simpul], simpul) for simpul in graf if simpul not in kunjungan)[1]
        kunjungan.add(simpul_sekarang)

        for tujuan, bobot in graf[simpul_sekarang].items():
            if biaya[simpul_sekarang] + bobot < biaya[tujuan]:
                biaya[tujuan] = biaya[simpul_sekarang] + bobot

    return biaya

if __name__ == "__main__":
    graf = {
        'A': {'B': 9, 'D': 10, 'F': 3},
        'B': {'A': 10, 'C': 5, 'D': 6, 'E': 5, 'F': 11},
        'C': {'B': 5, 'E': 8},
        'D': {'A': 10, 'B': 6, 'E': 6, 'F':6},
        'E': {'B': 5, 'C': 8, 'D': 6, 'F':9},
        'F': {'A': 3, 'B': 11, 'D': 6, 'E':9}
    }
    mulai_simpul = 'D'
    minimum_cost = dijkstra(graf, mulai_simpul)
    print("\n","Biaya minimum dari simpul {}: ke C adalah :".format(mulai_simpul), minimum_cost['C'], "\n")