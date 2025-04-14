class SmartPhone:
    def __init__(self):
        self.ram = None
        self.rom = None
        self.display = None
        self.refresh_rate = None

    def __str__(self):
        return (
            f"SmartPhone(ram={self.ram}, rom={self.rom}, "
            f"display={self.display}, refresh_rate={self.refresh_rate})"
        )


class SmartPhoneBuilder:
    def __init__(self):
        self.smartPhone = SmartPhone()

    def set_ram(self, ram):
        self.smartPhone.ram = ram
        return self

    def set_rom(self, rom):
        self.smartPhone.rom = rom
        return self

    def set_display(self, display):
        self.smartPhone.display = display
        return self

    def set_refresh_rate(self, refresh_rate):
        self.smartPhone.refresh_rate = refresh_rate
        return self

    def build(self):
        return self.smartPhone


if __name__ == "__main__":
    smartPhone = SmartPhoneBuilder()
    test_phone = (
        smartPhone.set_ram("8GB")
        .set_rom("128GB")
        .set_display("6.2 inches")
        .set_refresh_rate("120Hz")
        .build()
    )

    print(test_phone)
