import fileinput


# evm_word = "".join([line for line in fileinput.input()])
evm_word = "fdfffcfffcfff389000000000000000000000000000000000000000000000000"
result = ""

assert len(evm_word) == 64, "invalid size for evm word"

for i in range(0, len(evm_word), 16):
    x = [evm_word[j:j+2] for j in range(i,i+17,2)]
    result += "".join(reversed(x))
    # result += "".join(list(reversed([evm_word[i:i+2] for i in range(0, 17, 2)])))

print(result)
