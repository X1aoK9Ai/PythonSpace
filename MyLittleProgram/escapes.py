#!usr/etc/python3
#coding=UTF-8
start=1
while start==1:
    a = str(input(r"Input the escapes to view:"))
    a = str(a)
    if a == "\\":
        print("\\表示在代码中换行，在输出中不换且不添加任何字符。")
        print("代码：print\(\"This is the first line. \nThis is the second line.\"\)")
        print("输出：\nThis is the first line. \
              This is the second line.")
    elif a == "\\\\":
        print("\\\\表示输入\\。")
        print("代码：print\(\"\\\"\)")
        print("输出；\n\\")
    elif a == "\\a":
        print("表示响铃。")
    elif a == "\\b":
        print("退格\(Backspace\)，指删除\\b前一个字符")
        print("代码:print\(\"Backspace\\b\"\)")
        print("输出：\nBackspac")
    elif a == "\e":

else:
    print("结束了。")