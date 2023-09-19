#函数input()接受一个参数 即要向用户显示的提示的提示或说明
message=input("Tell me something,and I will repeat it back to you:")
print(message)

prompt="If you tell us who you are,we can personalize the messages you see."
prompt+="\nWhat is your first name?"
name=input(prompt)
print(f"\nHello,{name}!")

# 函数int()让Python将输入视为数值
# 函数int()将数的字符串表示转换为数值表示
height=input("How tall are you,in inches?")
height=int(height)
if height>=48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
