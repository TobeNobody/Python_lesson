result = {}
with open("file_task06.txt", "r", encoding="utf-8") as f:
    for i in f:
        subject, *time = i.split()
        result[subject] = sum(map(int, time))
    print(result)

# с модулем re так и не разобрался пока  =.(( и понял только как сделать если отсутствуют (л), (пр) и (лаб)...
# Но итак затянул, буду сдавать так