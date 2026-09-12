# -*- coding: utf-8 -*-
"""Isi naskah untuk poster dan infografis. Diambil dari REVISI_24_JUNI.docx."""

JUDUL = ('Perancangan UI/UX Aplikasi Lost and Found “Balikin” '
         'Berbasis Sistem Reputasi Komunitas dengan Pendekatan Design Thinking')
SUBJUDUL = 'Studi Kasus di Sukabumi'
PENULIS = 'Uldan Pamungkas'
NIM = '20210060127'
PRODI = 'Program Studi Desain Komunikasi Visual'
FAKULTAS = 'Fakultas Teknik, Komputer dan Desain · Universitas Nusa Putra Sukabumi'
BIMBING = ['Pembimbing I · Firman Mutaqin, S.Ds., M.Ds',
           'Pembimbing II · Rifky Nugraha, S.Pd., M.Ds']

LATAR = ('Kehilangan dompet, ponsel, kunci, atau dokumen adalah kejadian sehari-hari yang '
         'menimbulkan kerugian materiil sekaligus tekanan psikologis. Di Sukabumi, pelaporan '
         'masih bergantung pada inisiatif pribadi: pesan di grup percakapan dan unggahan media '
         'sosial yang bersifat sementara, serta penitipan di pos keamanan yang sering tidak '
         'diketahui pemiliknya. Belum ada data statistik resmi untuk kehilangan barang non-pidana, '
         'sehingga pemahaman masalah dibangun dari data primer di lapangan.')

RUMUSAN = [
 'Bagaimana merancang antarmuka yang mudah digunakan untuk pelaporan barang hilang dan temuan?',
 'Bagaimana merancang sistem reputasi komunitas yang dipahami dan dipersepsi positif oleh pengguna?',
 'Bagaimana menerapkan Design Thinking dalam perancangan dan pengujian usability prototipe?']

TUJUAN = [
 'Merancang antarmuka yang usable untuk memudahkan pelaporan barang hilang dan temuan.',
 'Merancang sistem reputasi yang jelas dan dipahami sebagai bentuk pengakuan, bukan imbalan uang.',
 'Menerapkan Design Thinking untuk merancang dan menguji usability prototipe aplikasi Balikin.']

METODE = ('Penelitian perancangan dengan metode campuran berdominasi kualitatif. Data kualitatif '
          'dari observasi lapangan non-partisipatif dan wawancara mendalam; data kuantitatif '
          'deskriptif dari kuesioner preferensi dan Single Ease Question (SEQ) sebagai pendukung '
          'keputusan desain.')
LOKASI = 'Kampus · halte · taman kota · masjid besar · pusat perbelanjaan di Kota Sukabumi'

TAHAP = [
 ('Empathize', 'Observasi lapangan, wawancara mendalam, kuesioner.',
  'Data kebutuhan, kebiasaan, dan motivasi pengguna di konteks sosial Sukabumi.'),
 ('Define', 'Merumuskan masalah inti: bukan sekadar ketiadaan platform, tetapi rendahnya dorongan sosial untuk bertindak.',
  'Pernyataan masalah dan tujuan perancangan.'),
 ('Ideate', 'Brainstorming fitur, sistem reputasi, elemen visual, dan strategi komunikasi.',
  'Kumpulan ide fitur, sketsa wireframe awal, konsep lencana, dan gaya UI.'),
 ('Prototype', 'Wireframe hingga antarmuka high fidelity di Figma.',
  'Prototipe aplikasi Balikin siap diuji.'),
 ('Test', 'Uji coba prototipe kepada responden pengguna potensial.',
  'Umpan balik pengguna dan revisi desain berdasarkan data uji.')]

TEMUAN = [
 ('Penemu ragu bertindak', 'Takut dituduh mencuri, atau tidak tahu cara mengembalikan dengan aman.'),
 ('Kanal sekarang tidak bertahan', 'Unggahan media sosial bersifat sementara dan sulit diakses kembali.'),
 ('Pengakuan lebih dihargai', 'Sebagian pengguna lebih menghargai rekam jejak dan pengakuan daripada imbalan uang.'),
 ('Celah penelitian', 'Belum ada yang memadukan pendekatan DKV (UI/UX) dengan sistem reputasi komunitas.')]

TEORI = [('Self-Determination Theory', 'Ryan & Deci, 2000 — kebutuhan kompetensi dan keterhubungan'),
         ('Bystander effect', 'Latané & Darley, 1970 — latar konteks sosial masalah')]

KESIMPULAN_PENDING = ('[Ringkasan hasil pengujian usability diisi setelah data terkumpul.] '
                      'Penelitian dibatasi pada perancangan dan pengujian prototipe; perubahan '
                      'perilaku aktual pengguna berada di luar lingkup penelitian.')

BATASAN = ['Luaran berupa prototipe antarmuka yang dapat diklik (Figma), bukan aplikasi rilis.',
           'Pengujian dibatasi pada usability (SEQ) dan persepsi pengguna.',
           'Responden purposif dengan jumlah terbatas, tidak digeneralisasi.',
           'Sukabumi sebagai lokasi studi kasus, bukan populasi yang diwakili.']

# ---- infografis 1: perjalanan ----
PERJALANAN = [
 ('HILANG',       'Dompet tertinggal di angkot, sore hari.',                       'pin',    'terra'),
 ('DILAPORKAN',   'Foto, kategori, lokasi, kirim. Empat langkah, dua menit.',      'camera', 'teal'),
 ('TAMPIL',       'Muncul di beranda warga dalam radius lima kilometer.',          'grid',   'teal'),
 ('DICOCOKKAN',   'Sistem menemukan laporan mirip. Kemiripan tertinggi 92%.',      'scan',   'teal'),
 ('DIVERIFIKASI', 'Tiga pertanyaan dari ciri rahasia yang dikunci pemiliknya.',    'bag',    'teal'),
 ('DISERAHKAN',   'Titik aman ber-CCTV. Kode empat huruf dicocokkan di lokasi.',   'wallet', 'teal'),
 ('PULANG',       'Barang kembali. Penemunya mendapat 150 poin reputasi.',         'check',  'gold')]

# ---- infografis 2: sistem reputasi ----
TINGKAT = [('Warga Baru', '0 – 150', 'Mulai berkontribusi di komunitas.', '#E6DDCD', '#C4B9A9'),
           ('Tetangga Baik', '150 – 400', 'Mulai dipercaya oleh komunitas.', '#8FD4C4', '#5FB8A4'),
           ('Penolong', '400 – 900', 'Aktif membantu pengembalian barang.', '#1B7A6E', '#15655B'),
           ('Penjaga Kota', '900 – 2.000', 'Dipercaya dalam proses pengembalian.', '#BC5A3C', '#9A4630'),
           ('Legenda Balikin', '2.000 ke atas', 'Jadi teladan komunitas.', '#C8952E', '#A87722')]

LENCANA = ['Balik Pertama', '10 Barang', 'Balas Cepat', 'Mata Elang', 'Dokumen',
           'Jaga Malam', 'Nol Sengketa', 'Penggerak', 'Legenda']

POIN_NAIK = [('Barang kembali ke pemiliknya', '+150'), ('Laporan tepat dan terverifikasi', '+50'),
             ('KTP terverifikasi', '+40'), ('Foto wajah terverifikasi', '+30')]
POIN_TURUN = [('Laporan palsu', '−50'), ('Klaim berulang', '−30'),
              ('Batal janji temu tanpa kabar', '−20')]
