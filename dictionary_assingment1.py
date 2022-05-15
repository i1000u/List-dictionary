cheonwoo = {'name': '전천우', 'age': 20, 'birthday': 20030417,
            'sex': 'male', 'phone_number': '010-9339-6369'}
juha = {'name': '김주하', 'age': 20, 'birthday': 20031031,
        'sex': 'female', 'phone_number': '010-8518-5507'}
hyunwoo = {'name': '이현우', 'age': 24, 'birthday': 19990414,
           'sex': 'male', 'phone_number': '010-8408-9589'}

name = [1, 2, 3]
age = [1, 2, 3]
birthday = [1, 2, 3]
sex = [1, 2, 3]
phone_number = [1, 2, 3]
###############################################################################3333
name[0] = cheonwoo['name']
name[1] = juha['name']
name[2] = hyunwoo['name']

age[0] = cheonwoo['age']
age[1] = juha['age']
age[2] = hyunwoo['age']

birthday[0] = cheonwoo['birthday']
birthday[1] = juha['birthday']
birthday[2] = hyunwoo['birthday']

sex[0] = cheonwoo['sex']
sex[1] = juha['sex']
sex[2] = hyunwoo['sex']

phone_number[0] = cheonwoo['phone_number']
phone_number[1] = juha['phone_number']
phone_number[2] = hyunwoo['phone_number']





print("이름 리스트는 %s" %name ) 
print("나이 리스트는 %s" %age )
print("생일 리스트는 %s" %birthday)
print("성별 리스트는 %s" %birthday)
print("전화번호 리스트는 %s" %phone_number)