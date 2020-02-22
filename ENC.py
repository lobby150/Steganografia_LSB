from PIL import Image


def string2bits(s):
    return  str(  ''.join(format(ord(x), 'b') for x in s))


end = input("Podaj tekst: ")
end= string2bits(end)
print(len(end))
j = 0
print(end)

with Image.open("foto.png") as img:

    for x in range(0,256):
        for y in range(0,256):
            pixel = list(img.getpixel((x,y)))
            for n in range(0,3):
                if(j<len(end)):
                    if pixel[n]%2 ==1 and int(end[j])==1:
                        pixel[n]=pixel[n]
                    elif pixel[n]%2==1 and int(end[j])==0:
                        pixel[n]= pixel[n]-1
                    elif pixel[n]%2==0 and int(end[j])==0:
                        pixel[n]=pixel[n]
                    elif pixel[n]%2==0 and int(end[j])==1:
                        pixel[n] = pixel[n]+1
                    j+=1
            img.putpixel((x,y),tuple(pixel))
            pixel2 = list(img.getpixel((x,y)))
    img.save("secret.png","PNG")

img = Image.open("foto.png")
img2 = Image.open("secret.png")


deszyfr = []
with Image.open("secret.png") as img:
    for x in range(0,256):
        for y in range(0,256):
            pixel = list(img.getpixel((x,y)))
            for n in range(0,3):
                deszyfr.append(pixel[n]&1)
deszyfrowanie = "".join([str(x)for x in deszyfr])
print("Zdeszyfrowane:" + deszyfrowanie[:len(end)])











