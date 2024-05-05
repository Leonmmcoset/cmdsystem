def start():
    import pygame
    import os
    import time

    def play_music(file_path):
        # 初始化pygame
        pygame.init()

        try:
            # 设置音频设备
            pygame.mixer.init()

            # 加载音乐文件
            pygame.mixer.music.load(file_path)

            # 播放音乐
            pygame.mixer.music.play()

            while True:
                command = input("Enter command (play/pause/resume/exit): ").lower()

                if command == 'play':
                    pygame.mixer.music.unpause()  # 继续播放音乐
                elif command == 'pause':
                    pygame.mixer.music.pause()  # 暂停音乐
                elif command == 'resume':
                    pygame.mixer.music.unpause()  # 恢复播放音乐
                elif command == 'exit':
                    break  # 退出播放器
                else:
                    print("Invalid command.")
        except pygame.error as e:
            print("Error playing music:", e)
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
            pygame.quit()

    def main():
        # 获取音乐文件路径
        file_path = input("Enter the path to the music file you want to play: ")

        # 确保文件存在
        if not os.path.exists(file_path):
            print("Error: File not found.")
            return

        # 播放音乐
        play_music(file_path)
    main()
