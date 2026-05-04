from PIL import Image
import os

SRC = r'd:\Projetos\Vault\logos-archive\fotos'
DST = r'd:\Projetos\Vault\logos-archive\site\banners'
BANNER_W, BANNER_H = 1400, 350
TOLERANCE = 30

def color_dist(c1, c2):
    return sum((a - b) ** 2 for a, b in zip(c1[:3], c2[:3])) ** 0.5

os.makedirs(DST, exist_ok=True)

for fname in os.listdir(SRC):
    if not fname.endswith('.png'):
        continue
    img = Image.open(os.path.join(SRC, fname)).convert('RGBA')
    w, h = img.size
    # Detecta cor de fundo pelos 4 cantos
    corners = [img.getpixel((0, 0)), img.getpixel((w-1, 0)),
               img.getpixel((0, h-1)), img.getpixel((w-1, h-1))]
    bg = tuple(sum(c[i] for c in corners) // 4 for i in range(3))
    # Remove fundo
    data = list(img.getdata())
    new_data = [
        (0, 0, 0, 0) if color_dist(px, bg) < TOLERANCE else px
        for px in data
    ]
    img.putdata(new_data)
    # Redimensiona mantendo proporção, centraliza em canvas transparente
    img.thumbnail((BANNER_W, BANNER_H), Image.LANCZOS)
    canvas = Image.new('RGBA', (BANNER_W, BANNER_H), (0, 0, 0, 0))
    x = (BANNER_W - img.width) // 2
    y = (BANNER_H - img.height) // 2
    canvas.paste(img, (x, y), img)
    canvas.save(os.path.join(DST, fname), 'PNG')
    print(f'OK: {fname}  bg={bg}  img={img.size}')
