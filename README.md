# mini-project1-fina-salsabila-p
# Penjelasan Program
Program ini merupakan Sistem Manajemen Line-Up Program ini digunakan untuk mengelola data penampilan band dalam sebuah konser.
Data yang disimpan meliputi:

Nama Band

Judul Lagu

Jam Tampil

Program menggunakan list sebagai tempat penyimpanan data sementara. List yang digunakan adalah lineup = [], yang berfungsi untuk menyimpan seluruh data line-up band.
Setiap data band disimpan dalam bentuk tuple yang berisi nama band, lagu yang dibawakan, dan jam tampil. Data tersebut kemudian dimasukkan ke dalam list menggunakan fungsi append().
Program juga menggunakan perulangan while sehingga menu akan terus ditampilkan sampai pengguna memilih menu keluar. Ketika pengguna memilih menu keluar, program menggunakan perintah `break` untuk menghentikan perulangan.
Sistem ini menerapkan operasi CRUD (Create, Read, Update, Delete), yaitu:

1. Tambah Line-Up (Create)

Digunakan untuk menambahkan data band baru ke dalam daftar line-up konser. Program akan meminta pengguna memasukkan nama band, lagu, dan jam tampil. Data yang telah dimasukkan kemudian disimpan ke dalam list.

2. Lihat Semua Line-Up (Read)

Digunakan untuk menampilkan seluruh data band yang telah dimasukkan. Program menggunakan perulangan `for` untuk menampilkan setiap data line-up yang tersimpan.

3. Ubah Line-Up (Update)
 
Digunakan untuk mengubah data line-up yang sudah ada. Pengguna diminta memilih nomor line-up yang ingin diubah, kemudian memasukkan data baru untuk menggantikan data sebelumnya.

4.  Hapus Line-Up (Delete)

Digunakan untuk menghapus data line-up dari daftar. Pengguna memilih nomor line-up yang ingin dihapus, kemudian program menggunakan fungsi pop() untuk menghapus data tersebut dari list.
Program ini juga menggunakan conditional statement (if, elif, dan else) untuk menentukan pilihan menu dan melakukan validasi. Jika pengguna memasukkan pilihan menu yang tidak tersedia, program akan menampilkan pesan bahwa pilihan tidak valid dan meminta pengguna untuk memasukkan pilihan kembali.

Program juga memiliki beberapa validasi input, seperti memastikan data nama band, lagu, dan jam tampil tidak kosong. Jika terdapat data yang kosong, program akan menampilkan pesan bahwa data tidak boleh kosong.
Pada proses ubah dan hapus data, program melakukan validasi nomor line-up menggunakan isdigit() untuk memastikan bahwa input yang dimasukkan berupa angka. Program juga mengecek apakah nomor yang dimasukkan tersedia dalam daftar line-up. Jika nomor tidak tersedia atau input bukan berupa angka, pengguna akan diminta untuk memasukkan input kembali.

Program juga menggunakan len() untuk mengecek apakah data line-up masih kosong. Jika belum ada data yang tersimpan, program akan menampilkan pesan bahwa data line-up masih kosong.

Dengan adanya program ini, pengguna dapat mengelola data line-up konser secara sederhana melalui menu yang berjalan secara berulang. Program ini telah menerapkan CRUD (Create, Read, Update, Delete), penggunaan list dan tuple, perulangan, conditional statement, serta validasi input agar program dapat berjalan dengan baik dan tidak mengalami error ketika pengguna memasukkan input yang salah.
# flowchart
<img width="5908" height="5200" alt="image" src="https://github.com/user-attachments/assets/e5029873-f8f8-40f6-92b0-86ff0e850dc2" />

# terminal

1. Tambah Line-Up (Create)

<img width="545" height="412" alt="image" src="https://github.com/user-attachments/assets/e1b009f3-0c80-4ae4-8f75-05b5a92403ef" />

2. Lihat Semua Line-Up (Read)

<img width="576" height="573" alt="image" src="https://github.com/user-attachments/assets/22650191-3255-4193-bb53-872d29b25a39" />

3. Ubah Line-Up (Update)

<img width="575" height="542" alt="image" src="https://github.com/user-attachments/assets/07e9b308-ead6-4a62-b76b-e984b042db0d" />

4.  Hapus Line-Up (Delete)

<img width="542" height="485" alt="image" src="https://github.com/user-attachments/assets/4c89b87a-f9ed-4a89-a998-eac96e30e56c" />

5.keluar

<img width="415" height="296" alt="image" src="https://github.com/user-attachments/assets/6dbf81a6-88ba-4b0a-a9d5-10ccae325412" />
