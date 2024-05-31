def month_year_converter(angka_desimal):
    total_bulan = int(angka_desimal * 12)

    tahun = total_bulan // 12
    bulan = total_bulan % 12

    return f"{tahun} Tahun {bulan} Bulan"

