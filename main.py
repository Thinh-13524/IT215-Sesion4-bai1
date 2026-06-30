# Phân tích lỗi
# GET /products/1 trả về 404 Not Found vì route hiện tại là: @app.get("/products/product_id")
# FastAPI hiểu đây là đường dẫn cố định /products/product_id, không phải biến
# Dòng khai báo sai: @app.get("/products/product_id")
# /products/product_id không phải Path Parameter vì product_id không nằm trong dấu {}
# Endpoint đúng: @app.get("/products/{product_id}")

from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Laptop Dell", "price": 15000000},
    {"id": 2, "name": "Chuột Logitech", "price": 350000},
    {"id": 3, "name": "Bàn phím cơ", "price": 1200000}
]
@app.get("/products/{product_id}")
def get_product_detail(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"message": "Không tìm thấy sản phẩm"}