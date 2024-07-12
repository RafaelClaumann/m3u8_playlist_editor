import services as svc

def main():
    input_playlist = open("sample_playlist.m3u8", "r")
    channels = input_playlist.read().split('\n')
    input_playlist.close()

    while True:
        print("Escolha uma opção:")
        print("1. Remove low quality channels")
        print("2. Remove unwanted groups")
        print("3. Rename group")
        print("4. List groups")
        print("5. Sair")
        
        escolha = input("Digite o número da opção desejada: ")
        
        if escolha == '1':
            svc.remove_low_quality_channels(channels=channels)

        elif escolha == '2':
            input_str = input("Digite os elementos do array separados por vírgula: ")
            unwanted_groups = input_str.strip().split(',')
            svc.remove_unwanted_groups(channels=channels, groups=unwanted_groups)
            
        elif escolha == '3':
            old_group_input = input("Nome do grupo a ser substituido: ")
            new_group_input = input("Nome do novo grupo: ")
            svc.rename_group(channels=channels, old_group=old_group_input, new_group=new_group_input)

        elif escolha == '4':
            print(svc.list_all_groups(channels=channels))

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")
    

    output_playlist = open("output_playlist.m3u8", "w")
    output_playlist.write("\n".join(channels))
    output_playlist.close()


if __name__ == "__main__":
    main()
