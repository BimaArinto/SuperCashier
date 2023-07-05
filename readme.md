# SuperCashier
Python Project from Pacmann - Bima Arinto Nugroho - AI/ML Engineering

SuperCashier merupakan sistem kasir di supermarket dimana pelanggan bisa mengakses dan langsung membeli suatu barang dengan cara memasukkan nama barang jumlah barang, dan harga barang dimanapun pelanggan berada.

## 1. Requirements / Objectives
   - a. Membuat sistem input ID transaksi.
   - b. Membuat proses sistem untuk menambahkan barang yang ingin dibeli beserta jumlah dan harga barang.
   - c. Membuat proses sistem untuk mengubah atau update barang yang sudah dimasukkan ke dalam sistem sebelumnya.
   - d. Membuat proses sistem untuk menghapus salah satu barang yang sudah dimasukkan ke dalam sistem.
   - e. Membuat proses sistem untuk menghapus seluruh barang dan transaksi yang sudah dibuat di dalam sistem.
   - f. Membuat proses sistem untuk menampilkan dan menghitung total belanja dengan diskon (Jika sesuai persyaratan)

## 2.  Flowchart

![SuperCashier_Diagram](https://github.com/BimaArinto/SuperCashier/assets/98025217/bd77c2e9-2367-4d5d-a713-aebb5d69403f)

## 3. Penjelasan Code
Pelanggan akan dihadapkan dengan 8 menu yang memiliki fungsi tersendiri berupa:
- Masukkan ID Transaksi: Pelanggan dapat memasukkan pilihan angka 1 ke sistem dan mengisi ID transaksi.

![1  ID_Transaksi](https://github.com/BimaArinto/SuperCashier/assets/98025217/22596285-5479-4b3c-8823-788b2a8069b1)

- Tambah barang: Pelanggan dapat menambahkan dengan memasukkan pilihan angka 2 ke sistem dan memasukkan detail barang yang dibeli.

![2  Add_Item](https://github.com/BimaArinto/SuperCashier/assets/98025217/932babe7-f311-40c9-b6d8-4d53d82ff475)

- Ubah/edit barang: Pelanggan dapat melakukan perubahan dengan barang yang dibeli jika terdapat kesalahan dengan memilih pilihan 3.

![3  Update_Item](https://github.com/BimaArinto/SuperCashier/assets/98025217/946b6cd6-f407-485b-a9c8-1cc7c256bde3)

- Hapus barang: Pelanggakn dapat menghapus salah satu barang dengan memilih pilihan 4.

![4  Hapus_item](https://github.com/BimaArinto/SuperCashier/assets/98025217/083481ba-e654-4a5b-926d-d82a1f286ca7)

- Hapus semua Transaksi: Pelanggan dapat menghapus semua transaksi dan daftar barang dengan memilih pilihan 5.

![5  Delete_all](https://github.com/BimaArinto/SuperCashier/assets/98025217/3fccc5ef-0dde-47c3-9a06-b4cab04c41f5)

- Tampilkan transaksi: Pelanggan dapat melihat berapa jumlah barang yang sudah dimasukkan dan total harga dengan memilih pilihan 6.

![6  Show_item](https://github.com/BimaArinto/SuperCashier/assets/98025217/edc26526-27ca-487b-80bf-22e5e9f1d96b)

- Jumlahkan total pengeluaran: Pelanggan dapat melihat total yang harus dibayar dengan atau tanpa diskon dengan memilih pilihan 7.

![7  Total_expenditure](https://github.com/BimaArinto/SuperCashier/assets/98025217/587804cc-1e1b-41be-acc5-1afe77012bd7)

- def main()
Digunakan untuk mendefinisikan fungsi bernama main(). Dalam hal ini, main() berfungsi sebagai titik masuk atau titik awal eksekusi untuk sistem SuperCashier.

![main](https://github.com/BimaArinto/SuperCashier/assets/98025217/5e84256e-87b5-4665-a9a5-0447fa23c246)

### Berikut beberapa potongan gambar bagaimana menggunakan SuperCashier
#### Cara menggunakan SuperCashier

![Cara_menggunakan_aplikasi](https://github.com/BimaArinto/SuperCashier/assets/98025217/8d2500fb-1d75-4f00-8c9b-1cde4ebe2dfc)

## 4. Hasil Test Case

#### Test case 1
menambahkan item.

![Test_case_1](https://github.com/BimaArinto/SuperCashier/assets/98025217/0271822b-0170-410c-bc3b-341ab820efbb)

#### Test case 2
menghapus pesanan dengan memasukkan urutan/index barang. (dimulai dari 0)

![Test_case_2(1)](https://github.com/BimaArinto/SuperCashier/assets/98025217/d4e57085-3698-40e1-b394-470de979b4b7)

![Test_case_2(2)](https://github.com/BimaArinto/SuperCashier/assets/98025217/10c34472-8721-47a1-9968-cc902abcbcd7)

#### Test case 3
Menghapus semua pesanan yang telah dipesan

![Test_case_3](https://github.com/BimaArinto/SuperCashier/assets/98025217/6d4cd3d3-9e38-4f76-9634-4fe86a96ef69)

#### Test case 4
Menambahkan barang kembali dan menghitung total belanja.

![Test_case_4](https://github.com/BimaArinto/SuperCashier/assets/98025217/db9e32bf-a13d-4969-b260-d6c5bb07d6ba)

## 5. Future Work
- a. Menambahkan sistem kemanan dengan memberikan User Authentication, sehingga pelanggan dapat dengan tenang berbelanja tanpa harus khawatir jika perangkat pelanggan digunakan kerabat, anak, maupun keluarga dan membuat transaksi tidak disengaja maupun disengaja.
- b. Menambahkan Transaction History atau riwayat belanja sehingga pelanggan dapat melihat dan mengoreksi kembali belanjaan yang sudah dibeli.
