with open("abc.txt","r") as file:
    data=file.read()
    print(data)
    
processed_data=data.upper()
with open("abc.txt","w") as file:
    file.write(processed_data)
print("file processed completed")


