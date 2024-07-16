from app.services import services
from app.view import channel_groups_menu, series_group_menu, movies_group_menu


def main():
    svc = services.Services("/home/rafaelcb/Documentos/Projetos/m3u8_playlist_editor/files/sample_playlist.m3u8")

    while True:
        print("Choose an option to work with:")
        print("1. Channels")
        print("2. Movies/Vod")
        print("3. Series")
        print("4. Exit")

        escolha = input("Enter the number of the desired option: ")
        print()

        if escolha == '1':
            channel_groups_menu.show_menu(svc)

        if escolha == '2':
            movies_group_menu.show_menu(svc)

        if escolha == '3':
            series_group_menu.show_menu(svc)

        if escolha == '4':
            print("Exiting...")
            break

        channels = svc.get_channels_list()
        f = open("/home/rafaelcb/Documentos/Projetos/m3u8_playlist_editor/files/output_playlist.m3u8", 'w', encoding='utf-8')
        f.write("\n".join(channels))
        f.close()


if __name__ == "__main__":
    main()
