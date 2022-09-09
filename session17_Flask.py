# when to exeucte a py file uska naam= __main__

print(__name__)

def main():
    main("this is main function")


if __name__=="__main__":
    main()