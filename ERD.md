Entity Relationship Diagram (ERD) merupakan diagram yang
digunakan untuk menggambarkan struktur basis data sistem secara visual,
mencakup entitas-entitas yang terlibat beserta hubungan dan atribut
masing-masing. Diagram ini menjadi acuan utama dalam proses
perancangan dan pembangunan skema basis data agar setiap relasi antar
tabel terdefinisi dengan jelas. Dengan memahami ERD, pengembang
dapat memastikan bahwa struktur penyimpanan data sudah sesuai dengan
kebutuhan fungsional sistem yang telah dirancang.
Sistem ini memiliki sebelas entitas utama yang saling berelasi
satu sama lain. Entitas Pengguna merupakan entitas pusat yang berelasi
dengan hampir seluruh entitas lain dalam sistem, memiliki atribut peran
untuk membedakan tiga jenis pengguna dalam sistem, serta atribut
percobaan_login dan terkunci untuk mendukung mekanisme keamanan
akun. Entitas Unit menyimpan data unit kerja dengan atribut jenis_unit
yang membedakan empat jenis unit, yaitu KNA, Penumpang, Barang, dan
Keuangan, di mana satu Pengguna berelasi dengan satu Unit melalui
hubungan memiliki. Entitas Token Reset berelasi dengan Pengguna
melalui hubungan memiliki dan menyimpan atribut sudah_dipakai serta
88
kedaluwarsa_pada untuk memastikan token hanya dapat digunakan satu
kali dalam batas waktu yang ditentukan. ERD sistem monitoring dan
pelaporan kinerja unit PT KAI Divre I Sumatera Utara ini dapat dilihat
pada Gambar 3.x berikut.
Berdasarkan ERD pada Gambar 3.x, entitas Laporan merupakan
inti dari sistem pelaporan yang berelasi dengan Pengguna melalui
hubungan membuat, dengan Unit melalui hubungan memiliki, serta
memiliki atribut status_internal dan status untuk merepresentasikan dua
tingkat validasi yang berlaku dalam sistem. Laporan berelasi dengan
empat entitas detail sesuai jenis unitnya, yaitu Laporan KNA, Laporan
89
Penumpang, Laporan Barang, dan Laporan Keuangan,
masing-masing melalui hubungan relasi detail KNA, detail penumpang,
detail barang, dan detail keuangan. Entitas Laporan Barang secara
khusus berelasi dengan entitas Komoditi Barang melalui hubungan
digunakan pada, di mana satu komoditi dapat digunakan pada banyak
laporan barang sehingga mendukung pengelolaan komoditi yang bersifat
dinamis. Entitas Target berelasi dengan Pengguna melalui hubungan
menetapkan dan menyimpan data target kinerja per tahun dan per
kategori sebagai acuan perbandingan terhadap data realisasi pada laporan.
Entitas Permintaan Bantuan berelasi dengan Pengguna melalui
dua hubungan berbeda, yaitu mengajukan untuk pengguna yang
mengajukan tiket dan menangani untuk pengguna yang menanganinya,
serta memiliki atribut jenis yang membedakan tiga jenis tiket yaitu
TOKEN, ISSUE, dan REVISION. Entitas ini juga berelasi dengan
Laporan melalui hubungan terkait dengan kardinalitas 0..1 yang
menunjukkan bahwa tidak semua permintaan bantuan selalu berkaitan
dengan laporan tertentu. Entitas Log Audit berelasi dengan Pengguna
melalui hubungan mencatat dan menyimpan seluruh rekam jejak aktivitas
penting dalam sistem secara otomatis, mencakup atribut aksi dan detail
untuk keperluan penelusuran riwayat. Keseluruhan sebelas entitas ini
membentuk struktur basis data yang saling terhubung dan mendukung
seluruh alur fungsional sistem secara menyeluruh.