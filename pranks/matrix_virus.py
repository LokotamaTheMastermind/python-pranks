def main():
    import random_string
    try:
        while 1:
            text = random_string.generate(min_length=50, max_length=500)
            print(text)
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
