import zlib, struct, sys, os

def png(size, path):
    bg = (255, 143, 0)
    rows = []
    cx = cy = size / 2
    r = size * 0.30
    t = size * 0.07
    # checkmark segments
    p1 = (size * .30, size * .52); p2 = (size * .44, size * .66); p3 = (size * .72, size * .36)
    def dist(px, py, a, b):
        ax, ay = a; bx, by = b
        dx, dy = bx - ax, by - ay
        k = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
        return ((px - ax - k * dx) ** 2 + (py - ay - k * dy) ** 2) ** .5
    for y in range(size):
        row = bytearray([0])
        for x in range(size):
            d = min(dist(x, y, p1, p2), dist(x, y, p2, p3))
            row += bytes((255, 255, 255) if d < t else bg)
        rows.append(bytes(row))
    raw = b''.join(rows)
    def chunk(t, d):
        c = struct.pack('>I', len(d)) + t + d
        return c + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    data = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', size, size, 8, 2, 0, 0, 0)) \
        + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b'')
    open(path, 'wb').write(data)

out = sys.argv[1]
png(180, os.path.join(out, 'icon-180.png'))
png(512, os.path.join(out, 'icon-512.png'))
