#If the computer is dead,then has this.
from system import color
from system import config
def dead(id,reason):
    deadid = str(id)
    if config.main('image'):
        from PIL import Image

        # 打开图片文件
        image = Image.open("_internal/image/error.png")

        # 进一步缩小图片尺寸
        new_width, new_height = image.size
        new_width //= 4
        new_height //= 4
        image = image.resize((new_width, new_height))

        # 转换图像为灰度模式
        image = image.convert("L")

        # 获取图像的像素值
        pixels = list(image.getdata())

        # 字符映射
        char_map = " .:-=+*#"  # 7个字符

        # 将像素值转换为字符表示，并打印到控制台
        for i in range(new_height):
            for j in range(new_width):
                pixel_value = pixels[i * new_width + j]
                # 将像素值映射到字符
                char_index = int(pixel_value / 36)  # 将0-255的灰度值映射到0-6之间
                if char_index >= len(char_map):
                    char_index = len(char_map) - 1
                char = char_map[char_index]
                print(color.red+char, end=""+color.end)
            print()  # 换行
    print(color.red+'-------------------------------------------'+color.end)
    print(color.red+'Oh no!The system is dead because of some errors!'+color.end)
    print(color.red+'If you need help,contact to leonmmcoset@outlook.com!')
    print(color.red+'You should give information down below:')
    print(color.red+'ID:#'+color.end+color.yellow,deadid+color.end)
    print(color.red+'Error Info:'+color.end+color.yellow,reason,color.end)
    print(color.red+'-------------------------------------------'+color.end)
    #Root command system
    print(color.blue+'[Info]Input "stop" to exit the system.'+color.end)
    print(color.cyan+'ROOT COMMAND'+color.end)
    while True:
        a = input(color.blue+'ROOT >'+color.end)
        if a == 'stop':
            stop()
        else:
            print(color.red+'ERR:ROOT COMMAND FAILED!'+color.end)