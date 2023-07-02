from src.habbo_font import HabboFont

launched = True
while launched:
    text = str(input(">> Enter a text: "))
    try:
        HabboFont(text).generate_image()
        print("<< Your image has been saved successfully! Please check 'test' folder.")
    except:
        print("<< Oops... An error has occured.")
    launched = str(input(">> Generate another image? (Y/N) ")) in ["Y", "y", "yes", "YES", "Yes"]
