# 🎮 Game Collection PBO - Pygame Project

## 📌 Deskripsi Project

Project ini merupakan implementasi **Pemrograman Berbasis Objek (PBO)** menggunakan Python dengan library **Pygame**.

Aplikasi ini adalah sebuah **Game Collection (Game Hub)** yang berisi beberapa game 2D klasik dalam satu aplikasi, yaitu:

- 🐍 Snake
- 🐦 Flappy Bird
- 🦖 Dino Run

Setiap game dibuat secara **modular (terpisah)**, namun dikontrol oleh satu sistem utama (**Game Manager**).

---

## 🎯 Tujuan Project

- Mengimplementasikan konsep **OOP/PBO secara nyata**
- Membuat sistem **multi-game dalam satu aplikasi**
- Membangun arsitektur program yang **rapi, scalable, dan reusable**
- Melatih pembuatan game dengan **event-driven system (Pygame)**

---

## 🧠 Konsep PBO yang Digunakan

### ✅ Class & Object
Semua elemen game berbasis object:
- Player
- Obstacle
- UI
- Scene

---

### ✅ Inheritance
```python
GameObject → Snake / Bird / Dino
BaseGame   → SnakeGame / FlappyGame / DinoGame
```

---

## 🏗️ Arsitektur Sistem
Project menggunakan konsep:
🎮 Game Hub System (Multi-Scene + Multi-Game)

Komponen Utama:
 - Game Manager (Mengatur perpindahan scene)
 - Scene System (Home, Game Select, Game Scene)
 - BaseGame (Template semua game)
 - Game Scene (Logic tiap game (SnakeScene, FlappyScene, DinoScene))

---

## 🔁 Alur Program (Global)
 ```text
 START
  ↓
HOME MENU
  ↓
GAME SELECT
  ↓
PILIH GAME
  ↓
GAME SCENE (HOME → PLAYING)
  ↓
PAUSE / GAME OVER
  ↓
KEMBALI / RESTART
```

---

## 🔄 Alur Internal Game (State System)
Setiap game menggunakan state machine:
```text
HOME → LEVEL (optional) → PLAYING → PAUSE → GAME_OVER
```

---

## 📂 Struktur Project
```text
project_pbo_game/
│
├── main.py
├── game_manager.py
│
├── core/
│   ├── base_game.py        # Template game
│   ├── game_object.py      # Base object
│   └── asset_manager.py   
│
├── scenes/
│   ├── home.py
│   └── game_select.py      # Pilih game
│
├── games/
│   ├── snake/
│   ├── flappy_bird/
│   └── dino_run/
│
└── assets/
```

---

## ⚙️ Cara Kerja Sistem

### 1. main.py

 - Inisialisasi pygame
 - Menjalankan game loop

### 2. Game Manager

 - Mengatur scene aktif
 - Pindah antar game
 - Handle music global

### 3. BaseGame

Mengatur:
 - Layout game (window / fullscreen)
 - Scaling (smooth / pixel)
 - Header UI
 - Info panel
 - Scroll system

### 4. Scene (Game Logic)

Contoh:
 - SnakeScene
 - FlappyScene
 - DinoScene

Berisi:
 - State game
 - Input handling
 - Update logic
 - Rendering

---

## 🎮 Fitur Utama

### Multi Game System
 - Bisa pindah game tanpa restart aplikasi

### Scene-Based Architecture
 - Home
 - Game Select
 - Game Scene

### State Machine
 - HOME
 - PLAYING
 - PAUSE
 - GAME OVER

### Responsive Layout
 - Window mode & Fullscreen
 - Auto scaling 4:3 ratio

### Smooth / Pixel Scaling
```python
smoothscale (grafis halus)
scale (pixel gameplay)
```

### Audio System
 - Background Music
 - Sound Effect
 - Mute toggle (M)

### UI System
 - Header (judul + tombol)
 - Info panel
 - Button interaktif


---

## 🎮 Kontrol Global
 - ESC   : Pause / Back
 - M     : Mute
 - F     : Fullscreen
 - Mouse : Navigasi UI


---

## 🐍 Snake Controls
 - WASD / Arrow : Gerak
 - ESC          : Pause
 - R            : Restart
 - H            : Home

---

## 🐦 Flappy Bird Controls
 - Space/Click  : Lompat
 - ESC          : Pause
 - R            : Restart

---

## 🦖 Dino Run Controls
 - SPACE / UP   : Lompat
 - DOWN         : Duck
 - ESC          : Pause
 - R            : Restart

---

## 🧩 Mekanisme Game

### Snake
 - Makan food → tambah panjang
 - Speed meningkat tiap skor tertentu
 - Game over jika tabrak tubuh

### Flappy Bird
 - Hindari pipa
 - Skor bertambah saat melewati pipa
 - Gap mengecil seiring skor

### Dino Run
 - Hindari obstacle
 - Speed meningkat seiring waktu
 - Score berdasarkan waktu hidup


---

## Assets
- <a href="">Snake</a>
- <a href="">Flappy Bird</a>
- <a href="">Dino Run</a>

---

 ## Developer

  - Fauzan Adhim Muntazhar (003)
  - TIA25