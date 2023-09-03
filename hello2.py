

# 분기 -> 이런 상황에선 이렇게 두둥탁 


temp = int(input("기온은 어때요? "))

if 30 <= temp:
    print("너무 더워요.")
elif 10 <= temp and temp < 30 :
    print("괜찮네요")
elif 0 <= temp < 10 : # 0 <= temp and temp < 10 랑 가틈 
    print("외투를 챙기세요")
else:
    print("나가지 마쇼.")
