# Yılan Oyunu (Python + JSON)

Kısa: Basit bir Pygame tabanlı Yılan oyunu. Oyun ayarları `config.json` içinde, en yüksek skor `scores.json` içinde tutulur.

Kurulum:

```bash
python -m pip install -r requirements.txt
```

Çalıştırma:

```bash
python "Yılan Oyunu.py"
```

Kullanım:
- Ok tuşları veya WASD ile oynanır.
- `R` tuşu ile oyun bittiğinde yeniden başlatılabilir.
- `ESC` ile çıkış.

Ayarlar:
- `config.json` içinde `cell_size`, `cols`, `rows`, `speed` gibi ayarlar mevcut. Değiştirip yeniden çalıştırabilirsiniz.

Notlar:
- Windows kullanıyorsanız Pygame kurulumu için yukarıdaki `pip` komutunu kullanın.
- `scores.json` otomatik olarak güncellenir.
