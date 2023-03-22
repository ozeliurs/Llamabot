from llama_cpp import LLAMA

llama = LLAMA()


def main():
    print(llama.exec('Hi how are you?'))


if __name__ == '__main__':
    main()
