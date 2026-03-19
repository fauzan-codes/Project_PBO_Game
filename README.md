# Project_PBO_Game

# 🎮 Game Collection PBO - Pygame Project

## 📌 Deskripsi Project

Project ini merupakan implementasi **Pemrograman Berbasis Objek (PBO)** menggunakan Python dengan library **Pygame**.

Aplikasi yang dibuat adalah sebuah **Game Collection (Game Hub)** yang berisi beberapa game 2D klasik dalam satu program. Setiap game dibuat secara modular (terpisah), namun semuanya dapat diakses melalui satu menu utama.

Contoh game yang akan dibuat:
- Snake
- Flappy Bird
- Game3
- Game4
- Game5

Project ini tidak hanya berfokus pada gameplay, tetapi juga pada penerapan konsep **OOP/PBO secara benar dan terstruktur**.

---

## 🎯 Tujuan Project

Tujuan utama dari project ini adalah:

1. Mengimplementasikan konsep **Pemrograman Berbasis Objek (PBO)**:
   - Class
   - Object
   - Inheritance
2. Membuat game sederhana menggunakan Pygame
3. Melatih kemampuan membuat program modular dan scalable
4. Mengembangkan kreativitas dalam desain game
5. Membuat struktur kode yang rapi, jelas, dan mudah dipahami

---

## 🧠 Konsep PBO yang Digunakan

### 1. Class & Object

Semua elemen dalam game dibuat dalam bentuk object.

Contoh:
- Player
- Enemy
- Obstacle
- Item

```python
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```


### 2. Inheritance (WAJIB)

Inheritance digunakan untuk membuat class turunan dari class utama.

Contoh:

```python
class GameObject:
    def update(self):
        pass

    def draw(self, screen):
        pass

class Bird(GameObject):
    def update(self):
        # implementasi khusus
```

Manfaat:
- Mengurangi duplikasi kode
- Struktur lebih rapi
- Mudah dikembangkan


### 3. Encapsulation

Digunakan untuk menyembunyikan data dalam class.

Contoh:
```python
self._speed = 5
```


### 4. Polymorphism (Bonus)

Method yang sama digunakan oleh object berbeda. Namun tiap object memiliki perilaku berbeda.

Contoh:
```python
object.update()
```


---

## 🏗️ Arsitektur Sistem

Project ini menggunakan konsep: 🎮 Game Hub / Multi-Game System

Dimana:
- Setiap game berdiri sendiri (independent)
- Semua game diatur oleh satu sistem utama (Game Manager)
- User dapat memilih game dari menu


---

## 🔁 Alur Program

```teks
START PROGRAM
     ↓
MAIN MENU
     ↓
PILIH GAME
     ↓
GAME BERJALAN
     ↓
PAUSE / GAME OVER
     ↓
KEMBALI KE MENU
```


---

## 📂 Struktur Folder Project

```teks
project_pbo_game/
│
├── main.py                  # Entry point program
├── game_manager.py          # Pengatur perpindahan game
│
├── core/                    # Base class (inti PBO)
│   ├── game_object.py       # Parent semua object
│   ├── base_game.py         # Parent semua game
│
├── scenes/                  # UI / scene
│   ├── menu.py              # Menu utama
│   ├── pause.py             # Pause menu
│
├── games/                   # Semua game
│
│   ├── snake/
│   │   ├── snake_game.py
│   │   ├── snake.py
│   │   ├── food.py
│
│   ├── flappy/
│   │   ├── flappy_game.py
│   │   ├── bird.py
│   │   ├── pipe.py
│
│   ├── pong/
│   │   ├── pong_game.py
│
│   ├── shooter/
│   │   ├── shooter_game.py
│
│   ├── breakout/
│   │   ├── breakout_game.py
│
└── assets/                  # Gambar, sound, font
```

 
---

## ⚙️ Penjelasan Struktur

### 1. main.py

File utama untuk menjalankan program.

Tugas:
- Inisialisasi pygame
- Game loop utama
- Memanggil Game Manager


### 2. game_manager.py

Mengatur game yang sedang aktif.

Fungsi:
- Load game
- Switch game
- Update game
- Render game


### 3. core/

Berisi class dasar (PBO utama)

game_object.py
Parent untuk semua object dalam game:
- Player
- Enemy
- Obstacle

base_game.py
Parent untuk semua game:
- SnakeGame
- FlappyGame
- PongGame


### 4. scenes/

Berisi UI:
- Menu utama
- Pause menu
- Game over screen


### 5. games/

Setiap game:
- Dipisah folder
- Berdiri sendiri
- Punya class sendiri


---

## 🎮 Standar Implementasi Game

Setiap game minimal memiliki:
- Player (karakter utama)
- Obstacle / musuh
- Sistem score
- Collision detection
- Update & render loop


---

## 🔗 Integrasi Antar Game

PENTING:
- Game tidak saling terhubung langsung
- Setiap game memiliki:
    - Class sendiri
    - Logic sendiri
- Integrasi hanya melalui:
    - Game Manager
    - Menu system


---

## 🧩 Struktur Class (PBO)

### GameObject

```python
class GameObject:
    def update(self):
        pass

    def draw(self, screen):
        pass
```

### BaseGame

```python
class BaseGame:
    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        pass
```

### Contoh Turunan

```python
class SnakeGame(BaseGame):
    pass

class Snake(GameObject):
    pass
```


---

## 🧪 Fitur Global (Semua Game)

Setiap game harus memiliki:
- Pause
- Restart
- Exit ke menu
- Game over screen


---

## ⚠️ Hal Penting yang Harus Diperhatikan

### 1. Fokus pada kualitas, bukan jumlah

- Lebih baik 2–3 game bagus
- Daripada 5 game tapi tidak selesai


### 2. Minimal 1 game dijelaskan detail

Untuk video penjelasan:
- Pilih 1 game utama
- Jelaskan class, inheritance, dan logic


### 3. Pastikan tidak error

Game HARUS:
- Bisa dijalankan
- Tidak crash


### 4. Gunakan inheritance

Minimal:
- GameObject → Player
- BaseGame → Game turunan


### 5. Code harus rapi

- Pisah file
- Gunakan nama jelas
- Hindari kode berantakan


---

## 🏆 Tips Mendapat Nilai Tinggi

- Gunakan struktur PBO yang jelas
- Terapkan inheritance dengan benar
- Tambahkan fitur:
    - Score
    - Sound
    - Animasi
- Buat UI sederhana tapi jelas
- Pastikan game playable


---

## 💡 Rencana Pengembangan

Project ini dapat dikembangkan menjadi:
- Tambah game baru
- Sistem save score
- Multiplayer (lanjut)
- UI lebih interaktif


---

## 📌 Catatan Developer

- Setiap game dibuat modular
- Mengutamakan clean code
- Mudah dikembangkan (scalable)


---

## 🏁 Penutup

Project ini dibuat sebagai implementasi nyata dari konsep PBO dalam bentuk game.

Dengan project ini diharapkan mahasiswa dapat memahami:
- Cara kerja OOP
- Struktur program besar
- Pengelolaan banyak class dalam satu sistem



---

# 🚀 Next Step (Saran dari aku)

Kalau kamu serius mau bikin ini:

👉 Step terbaik:
1. Setup project (folder + main + manager)
2. Buat base class (GameObject & BaseGame)
3. Buat menu
4. Baru implement game satu-satu

Kalau mau, aku bisa langsung:
👉 bikinin **starter template code (tinggal jalan)**  
👉 atau mulai dari **main + game manager dulu**

Tinggal bilang aja 👍

