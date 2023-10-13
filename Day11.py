import random
from PIL import Image
import tkinter as tk

# 감정 이미지 파일 경로
happy_image = "happy.png"
angry_image = "angry.png"
sad_image = "sad.png"
surprised_image = "surprised.png"

# 감정 레이블과 해당 이미지 파일 매핑
emotions = {
    "행복": happy_image,
    "화남": angry_image,
    "슬픔": sad_image,
    "놀람": surprised_image,
}

# 랜덤으로 감정 선택
selected_emotion = random.choice(list(emotions.keys()))

# GUI 창 만들기
root = tk.Tk()
root.title("감정 인식 게임")

# 이미지를 로드하고 표시
image = Image.open(emotions[selected_emotion])
photo = tk.PhotoImage(file=emotions[selected_emotion])
label = tk.Label(root, image=photo)
label.photo = photo
label.pack()

# 사용자가 감정을 맞추는 입력 필드
user_guess = tk.StringVar()
user_guess_entry = tk.Entry(root, textvariable=user_guess)
user_guess_entry.pack()

# 사용자의 답을 확인하고 힌트 제공
def check_guess():
    guess = user_guess.get()
    if guess == selected_emotion:
        result_label.config(text="정답입니다!")
    else:
        result_label.config(text="틀렸어요. 다시 시도하세요.")

check_button = tk.Button(root, text="확인", command=check_guess)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
