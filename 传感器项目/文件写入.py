list1 = [['张三','男','未婚',20],['李四','男','已婚',28],['小红','女','未婚',18],['小芳','女','已婚',25]]
output = open('data.txt','w',encoding='gbk')    #######'w'为每次刷新文件数据，'a'每次接着文件最后写入
output.write('name,gender,status,age\n')
for row in list1:
	rowtxt = '{},{},{},{}'.format(row[0],row[1],row[2],row[3])
	output.write(rowtxt)
	output.write('\n')
output.close()