# 读文件
txt=open("./data/foo.txt")
txt_read=txt.read() #全部读进来
print("content=\n",txt_read)
txt.close()

txt=open("./data/foo.txt")
lines=txt.readlines() #一行一行读
print("content=\n",lines)
for line in lines:
    print("line=\n",line)
txt.close()

# 写文件
tex=open("./data/foo.txt",'w') #覆盖写 (慎重)
tex.write("今天天气不错\n")
tex.write("今天天气不错\n")
txt.close()

tex=open("./data/foo.txt",'a') #追加写
tex.write("123\n")
tex.write("345\n")
txt.close()

with open("./data/foo.txt",'w') as f:  # with 方法可以自动关闭
    f.write("今天天气不错，是吧\n")