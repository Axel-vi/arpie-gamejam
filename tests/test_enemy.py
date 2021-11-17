
def test_asteroide():
    v, n, epsilon = 20, 10000, 0.000000001
    vitesses = []
    positions = []
    for i in range(n):
        x, y, vx, vy = apparition(v)
        aste = [x, y]
        temps = 0
        while aste[0] > 1:
            aste[0] += vx
            aste[1] += vy
            temps += 1
        vitesses.append(sqrt((x-aste[0])**2+(y-aste[1])**2)/temps)
        bool = aste[1] >= 0 and aste[1] <= height
        positions.append(bool)
        if not bool:
            print(aste[0], aste[1])
    vit_diff = [abs(v-vit) for vit in vitesses]
    vit_diff_max = max(vit_diff)
    bool_out = True
    for bool in positions:
        bool_out = bool_out and bool
    print("Max de différence entre vitesse entrée et vitesse pratique :" +
          str(vit_diff_max) + " pixels/frame")
    return bool_out and (vit_diff_max <= epsilon)


def test_asteroid():
    asteroid = Asteroide()
    asteroid2 = asteroid.move_rect()
    assert asteroid2.rect.left == asteroid.rect.left + asteroid.speed_x
    assert asteroid2.rect.top == asteroid.rect.top + asteroid.speed_y
