def prevod_C_na_F(stupne):
    return stupne * 1,8 + 32

def test_prevod_c_na_f():
    assert prevod_C_na_F(100) == 212
    assert prevod_C_na_F(0) == 32


if __name__ == "__main__":

    stupne = 57
    x1 = prevod_C_na_F(vstup)
    print(x1)