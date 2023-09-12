#通过使用for循环来遍历整个列表
#for语句末尾的冒号告诉Python，下一行是循环的第一行
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)

#在for循环中执行更多的操作时，需要将操作都缩紧在for循环之后
#在for循环后执行更多的操作时，需要将操作与for循环并列书写
magicians=['alice','david','carolina']
for magician in magicians:
    print(f"{magician.title()},that was a great trick!")
    print(f"I can't wait to see your next trick! {magician.title()}!")
    print("\n")
print("Thank you,everyone. That was a great show!")