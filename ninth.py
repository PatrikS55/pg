def dec_to_bin(cislo):
    n = int(cislo)
    
    if n == 0:
        return "0"
        
    binary_string = ""
    while n > 0:
        zbytek = n % 2
        binary_string = str(zbytek) + binary_string
        n = n // 2
        
    return binary_string

def test_bin_to_dec():

    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"