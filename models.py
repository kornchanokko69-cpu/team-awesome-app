"""models.py — ★ our one class lives here.

Package: one row of data.json (a game top-up package) turned into an object,
with methods that apply today's promotion and describe the package in words.

A page can turn a row from data.json into an object like this:

    import models
    pkg = models.Package(row["game"], row["package"], row["price"], row["has_promo"])
    pkg.discounted_price()
"""


class Package:
    def __init__(self, game, package, price, has_promo):
        self.game = game
        self.package = package
        self.price = price
        self.has_promo = has_promo

    def discounted_price(self):
        """ราคาหลังหักโปรโมชั่นวันนี้ (ลด 15% ถ้าแพ็กเกจนี้มีโปรอยู่ ไม่งั้นราคาเท่าเดิม)."""
        if self.has_promo == "yes":
            return round(self.price * 0.85)
        return self.price

    def describe(self):
        """ประโยคสรุปแพ็กเกจนี้ ใช้โชว์ในหน้าคำนวณส่วนลด."""
        if self.has_promo == "yes":
            return (self.game + " · " + self.package + " วันนี้มีโปร ลดเหลือ "
                    + str(self.discounted_price()) + " บาท (ปกติ " + str(self.price) + " บาท)")
        return self.game + " · " + self.package + " ราคาปกติ " + str(self.price) + " บาท (ไม่มีโปรวันนี้)"
