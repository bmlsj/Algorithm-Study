
T = int(input())

# 표 1
decode = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z',
          '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
          ]

for i in range(T):
    sentence = input()

    """ 라이브러리 사용시
    from base64 import b64decode
    sentence_bytes = base64.b64decode(sentence)
    sentence = sentence_bytes.decode('ascii')

    print(f"#{i} {sentence}")
    """

    word_len = len(sentence)
    res = ''

    for s in range(word_len):
        num = decode.index(sentence[s])

        # 2 진수로 변환 -> 8bit를 6bit로 나타내기 위해 앞에 00제거
        # int로 나타내면 숫자의 합이 나오므로, 0001010 이런식으로 나타내 주기 위해 str 사용
        bin_num = str(bin(num)[2:])

        # bin_num의 길이가 6보다 작으면 앞에 0붙여주기
        # 1 -> 000001
        while len(bin_num) < 6:
            bin_num = '0' + bin_num

        res += bin_num

    # 원래 문장(디코딩된 문장)
    r = ''
    # 글자 길이 * 6에서 8bit씩 자름
    for w in range(word_len * 6 // 8):
        # 8bit 씩 자르고 10진수로 변환
        e = int(res[w * 8:w * 8 + 8], 2)

        # 아스키 코드의 값을 r에 추가
        r += chr(e)

    print(f"#{i+1} {r}")


# https://swbeginner.tistory.com/entry/SWEA-%EC%BD%94%EB%94%A9-Base64-Decoder-PYTHON-1928
