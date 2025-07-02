def hitungStandarDeviasi(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    return variance ** 0.5

data = [1, 2, 3, 4, 5]
standar_deviasi = hitungStandarDeviasi(data)
print("Standar Deviasi:", standar_deviasi)