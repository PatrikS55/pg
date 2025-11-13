def fibac(maximum):
    result = [1, 1]
    while True:
        next_value = result[-1] + result[-2]
        if next_value > maximum:
            break
        result.append(next_value)
    return result

if __name__ == "__main__":
    import sys
    maximum = int(sys.argv[1])
    print(fibac(maximum))
