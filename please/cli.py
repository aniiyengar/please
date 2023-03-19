
import sys
from please import please

def main():
    if len(sys.argv) < 2:
        print("Usage: please <prompt>")
        sys.exit(1)

    user_input = ' '.join(sys.argv[1:])

    please(user_input)

if __name__ == '__main__':
    main()
