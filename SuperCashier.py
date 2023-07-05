from tabulate import tabulate

transaction_list = []

def enter_transaction_id():
    """
    Memberikan instruksi kepada pengguna untuk memasukkan ID transaksi.
    
    Returns:
    - transaction_id (str): ID transaksi yang sudah dibuat.
    """
    transaction_id = input("Masukkan ID transaksi: ")
    return transaction_id

def add_item():
    """
    Menambahkan barang ke daftar trnasaksi.
    Meminta pengguna untuk memasukkan nama barang, jumlah, dan harga.
    """
    item = input("Masukkan nama barang: ")
    quantity = int(input("Jumlah barang: "))
    price = float(input("Jumlah harga: "))
    transaction_list.append((item, quantity, price))
    print("barang berhasil ditambahkan.")

def update_item():
    """
    Memperbarui detail item dalam daftar transaksi.
    Menampilkan daftar transaksi saat ini dan meminta pengguna untuk memasukkan indeks item yang akan diperbaharui.
    """
    display_transaction()
    index = int(input("masukkan urutan barang yang ingin diubah(dimulai dari 0): "))
    item = input("Masukkan nama yang benar: ")
    quantity = int(input("Masukkan jumlah yang benar: "))
    price = float(input("masukkan harga yang benar: "))
    transaction_list[index] = (item, quantity, price)
    print("barang berhasil diubah.")

def delete_item():
    """
    Menghapus item dari daftar transaksi.
    Menampilkan daftar transaksi saat ini dan meminta pengguna memasukkan indeks item yang akan dihapus.
    """
    display_transaction()
    index = int(input("Masukkan angka dari item yang ingin dihapus(dimulai dari 0): "))
    
    if index < 0 or index >= len(transaction_list):
        print("Urutan salah, silahkan coba lagi")
    else:
        del transaction_list[index]
    print("Barang berhasil dihapus.")

def delete_all_transactions():
    """
    Menghapus semua transaksi dari daftar transaksi.
    Meminta pengguna untuk konfirmasi sebelum menghapus semua transaksi.
    """
    confirmation = input("Apakah anda yakin ingin menghapus semua transaksi? (y/n): ")
    if confirmation.lower() == 'y':
        transaction_list.clear()
        print("semua transaksi berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

def display_transaction():
    """
    Menampilkan daftar transaksi saat ini dengan rincian item.
    """
    headers = ["Nama Barang", "Jumlah", "Harga", "Total harga"]
    formatted_transactions = []

    if not transaction_list:
        print("Anda tidak memiliki barang.")
    else:
        print("Item yang akan dibeli adalah:")
        for item, quantity, price in transaction_list:
            total_price = quantity * price
            formatted_transactions.append([item, quantity, price, total_price])

        print(tabulate(formatted_transactions, headers=headers))


def calculate_total_expenditure():
    """
    Menghitung total pengeluaran dan diskin yang berlaku.
    Menampilkan total pengeluaran, persentase diskon, dan jumlah diskon.
    """
    total_price = sum(quantity * price for _, quantity, price in transaction_list)

    discount = 0
    if total_price > 500000:
        discount = 0.10
    elif total_price > 300000:
        discount = 0.08
    elif total_price > 200000:
        discount = 0.05

    discount_amount = total_price * discount
    total_price -= discount_amount

    print("Item yang akan dibeli adalah:")
    display_transaction()

    print("Total Pengeluaran: {:.2f}".format(total_price))
    print("Diskon: {:.2f}%".format(discount * 100))
    print("Jumlah diskon: {:.2f}".format(discount_amount))

def main():
    """
    Fungsi utama untuk menjalankan sistem self-service cashier.
    """
    running = True
    while running:
        print("\nSelf-Service Cashier System")
        print("1. Masukkan ID transaksi")
        print("2. Tambah barang")
        print("3. Ubah/edit barang")
        print("4. Hapus barang")
        print("5. Hapus semua transaksi")
        print("6. Tampilkan transaksi")
        print("7. Jumlahkan total pengeluaran")
        print("8. Exit")

        choice = input("Masukkan Pilihan Anda (1-8): ")

        if choice == '1':
            transaction_id = enter_transaction_id()
            print("ID transaksi:", transaction_id)
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            delete_all_transactions()
        elif choice == '6':
            display_transaction()
        elif choice == '7':
            calculate_total_expenditure()
        elif choice == '8':
            print("Exiting the program...")
            running = False
        else:
            print("Pilihan salah. Silahkan coba lagi.")

if __name__ == "__main__":
    main()