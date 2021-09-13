import xlrd
print("------------------12月份衣服销售数据-----------------")
wb = xlrd.open_workbook(filename=r"E:\python测试开发\day01\任务\12月份衣服销售数据.xlsx",encoding_override=True)
st=wb.sheet_by_name("12月份衣服销售数据")
rows = st.nrows
cols = st.ncols
print(rows,cols)
for row in range(rows):

        value = st.row_values(row)
        print(value)

# for row in range(rows):
#    value = st.row_values(row)
#    print(value)
print("总金额为:{:.2f}￥".format(253.6*10+86.3*60+96.8*43+135.9*63+65.8*63+49.3*120+86.3*72+253.6*140+86.3*90+135.9*24+65.8*45
                             +96.8*25+86.3*60+65.8*129+253.6*10+96.8*25+86.3*60+135.9*63+96.8*60+65.8*58+86.3*140+65.8*48
                             +96.8*43+135.9*57+253.6*10+65.8*63+96.8*78),
      "平均日销量为:",round(10+60+43+63+63+120+72+69+35+140+90+24+45+25+60+129+10+43+63+60+63+60+58+140+48+43+57+10+63+78, 2)/100,"￥")

print("羽绒服占销售比为:",round(((10+69+140+10+10)/500),3)*100,"%")
