import pandas as pd

df = pd.read_json ("../raw_posts.json")

#xuất 5 dòng đầu và 3 dòng cuối
print (df.head())
print (df.tail(3))
# In ra tổng số dòng, số cột và kiểu dữ liệu (dtypes) của từng cột trong DataFrame đó. Dữ liệu có bị khuyết (null) ô nào không?
print (df.dtypes)# kiểm tra kiểu dữ liệu
print (df.shape) #số dòng số cột
print (df.fillna(0))#kiểm tra null
renamee = df.rename (columns ={'userId':'USER_ID'}),df.rename(columns={'id':'POST_ID'})
print (renamee)
drops = df.drop (columns=['body'],inplace=True)
print (df)


#Bài tập 3: Chuẩn hóa text và Tính độ dài
 # Yêu cầu: Tạo một cột mới tên là title_length chứa độ dài (số ký tự) của trường title

df['title_length'] = df['title'].str.len()
df['title_upper'] = df['title'].str.upper()
print(df)
# tạo 1 cột chứa ký tự đầu tiên
df['first_word'] =  df['title'].str.split()
print (df['first_word'])

#bài tập 4: Lọc dữ liệu phức tạp (Filtering)

#Lọc ra các bài viết thỏa mãn đồng thời 2 điều kiện: Có userId là số chẵn (2, 4, 6, 8...) VÀ trường title có chứa từ "qui"

df_condit= df.loc[
    (df['userId']%2 ==0)
    & (df['title'] =="qui")
]
print (df_condit)
# Bài tập 5: Gom nhóm (Group By)
#  Yêu cầu: Đếm xem mỗi userId đã đăng bao nhiêu bài viết.
df['group'] = df.groupby ('userId')['title'].transform('count')
print(df)
# #  Yêu cầu nâng cao: Tìm bài viết có title dài nhất của từng userId. Kết quả trả về phải là một bảng gồm các cột: userId,id, title, và title_length
# # Tính độ dài title
df['title_length'] = df['title'].str.len()

# Lấy index của title dài nhất trong mỗi user
idx = df.groupby('userId')['title_length'].idxmax()
#
# # Lấy các dòng tương ứng
result = df.loc[idx, ['userId', 'id', 'title', 'title_length']]
#
# print(result)

# Bài tập 6: Tạo báo cáo tổng hợp (Pivot Table)
#  Yêu cầu: Giả sử bạn muốn phân loại các bài viết. Bài viết nào có title_length < 30 ký tự thì phân loại là "Short", ngược lại là "Long". Hãy tạo cột title_category để lưu phân loại này.
#  Yêu cầu nâng cao: Dùng hàm pd.crosstab hoặc .groupby() để thống kê xem mỗi userId có bao nhiêu bài "Short" và bao nhiêu bài "Long".


# )
df['Phanloai']=df['title_length'].apply (lambda x : 'Short' if x<30 else 'Long')
print(df)

cros = pd.crosstab(df['userId'], df['Phanloai'])
print(cros)

# df.to_excel("posts_processed.xlsx", index=False)
# df.to_csv("posts_processed.csv", index=False)
df.to_parquet("posts_processed.parquet", index=False)