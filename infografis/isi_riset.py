# -*- coding: utf-8 -*-
"""Isi lima bagian infografis penelitian. Seluruhnya dikutip dari
REVISI_24_JUNI.docx — jangan mengetik ulang dari ingatan.

Rujukan baris di naskah dicatat supaya gampang dicek ulang:
  Latar Belakang        BAB I, 1.1
  Tujuan Penelitian     BAB I, 1.4
  Metode                BAB III, 3.1 – 3.5.1
  Temuan                BAB III (data observasi & wawancara) + BAB II (kesimpulan deskriptif)
  Kesimpulan            BAB IV (Hasil Pengujian, Efektivitas Media)
"""

JUDUL_ATAS = 'Perancangan UI/UX Aplikasi Lost and Found'
JUDUL_NAMA = 'BALIKIN'
JUDUL_BAWAH = ('Berbasis Sistem Reputasi Komunitas dengan Pendekatan Design Thinking')
JUDUL_KASUS = 'Studi Kasus di Sukabumi'
PENULIS = 'Uldan Pamungkas'
NIM = '20210060127'
PRODI = 'Program Studi Desain Komunikasi Visual'
FAKULTAS = 'Fakultas Teknik, Komputer dan Desain · Universitas Nusa Putra Sukabumi'
BIMBING = ['Pembimbing I · Firman Mutaqin, S.Ds., M.Ds',
           'Pembimbing II · Rifky Nugraha, S.Pd., M.Ds']

LATAR = [
 'Kehilangan dompet, ponsel, kunci, atau dokumen penting adalah kejadian sehari-hari. '
 'Bukan hanya kerugian materiil — juga tekanan psikologis dan turunnya rasa aman di '
 'ruang publik.',
 'Di Sukabumi pelaporan masih bergantung pada inisiatif pribadi: pesan di grup percakapan '
 'dan unggahan media sosial yang bersifat sementara, serta penitipan di pos keamanan yang '
 'sering tidak diketahui pemiliknya.',
 'Belum ada data statistik resmi untuk kehilangan barang non-pidana (BPS, 2023), jadi '
 'pemahaman dibangun dari data primer. Sistem yang ada pun berhenti pada pencatatan — belum '
 'ada yang memadukan DKV dengan reputasi komunitas non-tunai lalu mengujinya.',
]

TEMUAN = [
 ('Penemu ragu bertindak', 'warga',
  'Takut dituduh mencuri, atau tidak tahu cara mengembalikan dengan aman — bystander effect.'),
 ('Kanal yang ada tidak bertahan', 'obrolan',
  'Unggahan media sosial bersifat sementara, tanpa format baku, dan sulit diakses kembali.'),
 ('Tidak ada sistem terintegrasi', 'peta',
  'Tidak ditemukan satu pun sistem pelaporan digital yang dipakai secara umum di Sukabumi.'),
 ('Pengakuan lebih dihargai', 'bintang',
  'Sebagian pengguna lebih menghargai rekam jejak kejujuran daripada imbalan uang.'),
]
CELAH = ('Celah penelitian: belum ada yang memadukan pendekatan DKV (UI/UX) dengan sistem '
         'reputasi komunitas non-tunai sekaligus mengujinya dari sisi usability.')

TUJUAN = [
 'Merancang antarmuka (UI/UX) aplikasi Balikin yang usable untuk memudahkan pelaporan '
 'barang hilang dan temuan.',
 'Merancang sistem reputasi komunitas yang jelas dan dipahami sebagai bentuk pengakuan, '
 'bukan imbalan uang.',
 'Menerapkan pendekatan Design Thinking untuk merancang dan menguji usability prototipe '
 'aplikasi Balikin.',
]

PENDEKATAN = ['Kualitatif', 'Kuantitatif deskriptif']
PENGUMPULAN = [
 ('Observasi lapangan', 'peta', '1–5 Mei 2025 · non-partisipatif',
  'Kampus, halte, taman kota, masjid besar, pusat perbelanjaan.'),
 ('Wawancara mendalam', 'obrolan', 'semi-terstruktur · purposif',
  'Mahasiswa, petugas keamanan, warga yang pernah kehilangan barang.'),
 ('Kuesioner daring', 'dokumen', '2–9 Juni 2025 · 60 responden',
  'Google Form, 15 butir, pilihan ganda dan skala Likert 1–5.'),
]
ANALISIS = ['SWOT', 'User Journey Mapping', 'Kuesioner deskriptif', '5W + 1H']
TAHAP = [
 ('Empathize', 'Observasi, wawancara, kuesioner'),
 ('Define', 'Dorongan sosial yang rendah'),
 ('Ideate', 'Fitur, reputasi, elemen visual'),
 ('Prototype', 'Wireframe → high fidelity'),
 ('Test', 'Uji coba ke pengguna'),
]
PENGUJIAN = 'Single Ease Question (SEQ)'

SEQ_NILAI, SEQ_MAKS = '6,1', '7'
SEQ_KET = 'Antarmuka dinilai sangat mudah digunakan.'
ANGKA = [('82%', 'terdorong melapor karena adanya apresiasi'),
         ('74%', 'menyukai visualisasi lencana'),
         ('88%', 'memahami alur laporan dalam waktu kurang dari satu menit')]
KESIMPULAN = [
 'Desain bekerja karena menurunkan beban kognitif, memberi apresiasi visual yang bermakna, '
 'dan mengubah persepsi “lapor itu ribet” menjadi “lapor itu mudah dan dihargai”.',
 'Masukan pengguna yang masuk tahap iterasi: fitur hubungi pemilik, penegasan status barang '
 'lewat warna, dan tombol aksi yang lebih besar.',
]
BATAS = ('Penelitian dibatasi pada perancangan dan pengujian prototipe; perubahan perilaku '
         'aktual pengguna di luar lingkup.')
TEORI = ['Self-Determination Theory (Ryan & Deci, 2000)',
         'Bystander effect (Latané &amp; Darley, 1970)']
