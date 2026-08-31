soal = [
    {
        'pertanyaan': 'ibukota indonesia adalah',
        'a': 'jakarta',
        'b': 'surabaya',
        'c': 'garut',
        'jawaban': 'a',
    },
    {
        'pertanyaan': 'nama presiden republik indonesia adalah?',
        'a': 'feri irwandi',
        'b': 'tan malaka',
        'c': 'prabowo galer',
        'jawaban': 'c'
    },
    {
        'pertanyaan': 'siapa GOAT sepakbola dunia?',
        'a': 'Antony',
        'b': 'Mudrikkk',
        'c': 'prabowo galer',
        'jawaban': 'c'
    }
]

score = 0
jawaban = ["a", "b", "c"]
for item in soal:
    print(item['pertanyaan'])
    print(f"a) {item['a']}")
    print(f"b) {item['b']}")
    print(f"c) {item['c']}")
    jawab = input('masukan jawaban anda: ').lower()
    if jawab not in jawaban:
        print("jawabannya cuman ada di ABC idiot")
    elif jawab == item["jawaban"]:
        print('jawaban anda benar')
        print('+1')
        score += 1
    else:
        print('salah tolol')
        print(f"jawabannya {item['jawaban']}")
print(f"anda mendapatkan score {score}/{len(soal)}")