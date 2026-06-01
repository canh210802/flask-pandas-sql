#1 tạo các route
from zlib import DEFLATED

from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return '''
#     <h1>Trang chủ</h1>
#     <p>Xin chào</p> <br>
#     <a href ='/about'>Page</a><br>
#     <a href="/contact">Contact Page</a>
#     '''
# @app.route('/about')
# def About_Page():
#     return '<h1>About Page</h1>'
#
# @app.route('/contact')
# def Contact_Page():
#     return '<H1>Contact page: 0971335664</h1>'
#
# if __name__ == "__main__":
#     app.run(debug=True)


#2 tạo các biến route



# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return '''
#     <h1>Trang chủ </h1>
#     <a href = 'Xin chao/ cảnh'>HELLO CẢNH </a><br>
#     <a href = 'xin chào/thang'> HELLO THANG </a>
#     '''
# @app.route('/hello/<name>')
# def hello(name):
#     return f'''
#     <h1>Hello {name}</h1>
#     <a href -' /'>quay lại </a>
# '''
# if __name__ == '__main__':
#     app.run(debug=True)


    # kiểm tra số chẵn lẻ

# app = Flask(__name__)
#
# @app.route ('/')
# def home ():
#     return '''
#     <h1> Kiểm tra chẵn lẻ </h1> <br>
#
#     <a href = '/check/8'>kiểm tra số 8 </a><br>
#     <a href = '/check/5' > kiểm tra số 5 </a> <br>
#     '''
# @app.route('/check/<int:number>')
# def check (number):
#     if number%2== 0:
#         return f'{number}  số chẵn'
#     else:
#         return f'{number}  là số lẻ'
#
# if __name__ == '__main__':
#     app.run(debug=True)

#Xử lý dữ liệu may tinh

# app = Flask(__name__)
#
# @ app.route ('/')
# def home():
#     return '''
#
#     <h1> kiểm tra cộng trừ nhân chia</h1> <br>
#
#     <a href = '/tong/5/10'> tổng là 15 </a><br>
#     <a href = '/tich/5/10'> tích là 50 </a><br>
#     <a href = '/hieu/5/10'> hieu la -5 </a><br>
#     <a href ='/thuong/5/10'> thuong la 0.5 </a><br>
#     '''
#
# @app.route('/tong/<int:a>/<int:b>')
# def tong(a,b):
#     result = a+b
#     return f'''
#     <h1> kết quả </h1><br>
#
#     <p> tổng là {a}+{b} = {result} </p><br>
#     <a href ='/'>Quay lại </a><br>
#     '''
#
#
# @app.route ('/tich/<float:a>/<float:b>')
# def tich(a,b):
#     phep_nhan = a*b
#     return f'''
#     <h1> phép nhân </h1><br>
#
#     <p> tích là {a}*{b} = {phep_nhan} </p><br>
#     <a href ='/'>Quay lại </a><br>
#     '''
# @app.route ('/hieu/<int:a>/<int:b>')
# def hieu(a,b):
#     phep_tru = a-b
#     return f'''
#     <h1> phép nhân </h1><br>
#
#     <p> hieu là {a}-{b} = {phep_tru} </p><br>
#     <a href ='/'>Quay lại </a><br>
#     '''
# @app.route ('/thuong/<int:a>/<int:b>')
# def thuong(a,b):
#     phep_chia = a%b
#     return f'''
#     <h1> phép nhân </h1><br>
#
#     <p> thương là {a}%{b} = {phep_chia} </p><br>
#     <a href ='/'>Quay lại </a><br>
#     '''
#
# if __name__ == "__main__":
#     app.run(debug=True)


#tính bmi

# app = Flask(__name__)
#
# @app.route('/')
# def home ():
#     return '''
#     <h1> Tính BMI giữa chiều cao cân nặng</h1><br>
#     <a href ='/tinhBMI'>BMI của bạn là: </a>
#     '''
# @app.route('/tinhBMI/<int:weight>/<float:height>')
# def tinhBMI (weight, height):
#     BMII= weight/(height**2)
#     if BMII< 18.5:
#         status= 'Gầy'
#     elif BMII< 25:
#         status = 'Bình thường'
#     elif BMII< 30:
#         status = 'thừa cân'
#     else:
#         status ='Béo PHÌ'
#     return f'''
#     <h1>Kết quả BMI </h1><br>
#
#     <p>BMI = {round(BMII, 2)}</p>
#
#     <p>Phân loại: {status}</p>
#
#     <a href='/'>Quay lại</a>
#     '''
#
# if __name__ == "__main__":
#     app.run(debug=True)


# app = Flask(__name__)


# @app.route('/')
# def home():
#     return '''
#     <h1>welcome</h1><br><br>
#     <a href ='/chanle'>tính chẵn lẻ:</a>
#
#     '''
# @app.route('/chanle/<int:number>')
# def chanle(number):
#     if number%2==0:
#         status ='Số chan'
#     else:
#         status = ' số lẻ'
#     return f'''
#     <p> số {number} là {status}</p>
#     '''
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask

# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return '''
#     <h1>Kiểm tra chẵn lẻ</h1>
#
#     <a href='/check/8'>Kiểm tra số 8</a><br><br>
#
#     <a href='/check/5'>Kiểm tra số 5</a>
#     '''
#
# @app.route('/check/<int:number>')
# def check(number):
#
#     if number % 2 == 0:
#         return f'{number} là số chẵn'
#
#     else:
#         return f'{number} là số lẻ'
#
# if __name__ == "__main__":
#     app.run(debug=True)

q