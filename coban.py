import math

# A. Tính giai thừa
def tinh_giai_thua(n):
    return math.factorial(n)

# B. Tính giá trị trung bình
def tinh_trung_binh(danh_sach):
    return sum(danh_sach) / len(danh_sach)

# C. Tính lợi nhuận sau 12 tháng (Lãi kép)
def tinh_loi_nhuan(von, lai_suat):
    # Công thức: Tiền gốc * (1 + lãi suất)^thời gian
    ket_qua = von * (1 + lai_suat)**12
    return ket_qua

# Chạy thử
print(f"Giai thua cua 5 la: {tinh_giai_thua(5)}")
print(f"Trung binh day so [10, 20, 30] la: {tinh_trung_binh([10, 20, 30])}")
print(f"Loi nhuan sau 12 thang (goc 100tr, lai 1%/thang): {tinh_loi_nhuan(100, 0.01):.2f}")