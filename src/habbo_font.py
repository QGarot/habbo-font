from src.letters_data import get_letter_size, get_letter_position
from PIL import Image


class HabboFont:
    def __init__(self, text: str):
        self.text = text
        self.width = 0
        self.height = 41
        self.image = None

    def set_image_size(self) -> None:
        for letter in self.text:
            # thickness: 10px
            if self.width > 10:
                self.width = self.width + get_letter_size(letter) - 10
            else:
                self.width = self.width + get_letter_size(letter)

    def set_image(self, img: Image) -> None:
        self.image = img

    def get_text(self) -> str:
        return self.text

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_image_letter(self, letter: str) -> Image:
        with Image.open("src/habbofont.png") as front:
            # top left corner
            x1 = get_letter_position(letter)
            y1 = 0
            # bottom right corner
            x2 = x1 + get_letter_size(letter)
            y2 = self.height

            return front.crop((x1, y1, x2, y2)).convert("RGBA")

    def generate_image(self, image_format: str = "png") -> None:
        # Foresee image size
        self.set_image_size()
        self.set_image(Image.new(mode="RGBA", size=(self.get_width(), self.get_height())))
        current_pos = 0
        for letter in self.get_text():
            # cut the letter
            image_letter = self.get_image_letter(letter)
            # paste it
            self.image.paste(image_letter, (current_pos, 0), image_letter)
            current_pos = current_pos + image_letter.size[0] - 10
        self.image.save("test/" + self.get_text() + "." + image_format)
