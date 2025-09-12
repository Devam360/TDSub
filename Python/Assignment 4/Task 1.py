try:
    with open('../Written during class/sample.txt', 'r') as f:
        read_file= f.read()
        print(read_file)
        f.close()
except FileNotFoundError:
    print("Error: File not found")