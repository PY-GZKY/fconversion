import xlwings as xw

app = xw.App(visible=False, add_book=False)
app.display_alerts = True
app.screen_updating = True
wb = app.books.open('../../src/test_files/318线路列表.xlsx')
sheet1 = wb.sheets['318线路列表']
info = sheet1.used_range.shape
# nrow = sheet1.api.UsedRange.Rows.count
# ncol = sheet1.api.UsedRange.Columns.count

print(sheet1.range('A1').options(dict, transpose=True).expand("table").value)
# 遍历读取单元格
# column_name = ['A','B',"C"]
# data_list = [] #将数据存到list中去
# for i in range(3): # 遍历行
#   row_list = []
#   for j in range(3): #遍历列
#     str1 = column_name[j]+str(i+1)
#     a = sht.range(str1).value
#     row_list.append(a)
#     print(a)
#     pass
#   data_list.append(row_list)
#   pass
# print(data_list)

# 读取行列：读取A1:C7（直接填入单元格范围就行了）,得到一个二维列表
# print(sht.range('a1:').value)
# print(sheet1.range('A1:8').value)

# 读取行：得一维列表
# print(sht.range('a1:c1').value)

# 读取列：得一维列表
# print(sht.range('a1:a7').value)

wb.save()
wb.close()
app.quit()