class Vector:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # นี่คือ dunder add
  def __add__(self, vector):
    # การบวกเวกเตอร์คือการสร้างเวกเตอร์ตัวใหม่
    # โดยเวกเตอร์ผลลัพธ์จะมีจุดเริ่มต้นที่ (0, 0)
    # แต่มีจุดปลาย ค่า x อยู่ที่ผลบวกของเวกเตอร์ทั้งสอง
    # ค่า y ก็เช่นกัน
    return Vector(self.x + vector.x, self.y + vector.y)
    
vector1 = Vector(3, 4)
vector2 = Vector(5, 6)

# เมื่อเราต้องการให้เวกเตอร์ + กันได้
# เราจึงต้องกำหนด __add__ ภายใต้คลาส Vector ของเรา
vector3 = vector1 + vector2

print(vector3.x, vector3.y) # 8 10
