import app.services.services as services
import app.helpers as helpers


def show_menu(svc: services.Services):
    while True:
        print("Choose an option:")
        print("1. Remove series groups")
        print("3. Exit")

        escolha = input("Enter the number of the desired option: ")

        if escolha == '1':
            series_groups = svc.get_series_groups()
            helpers.print_groups_with_indexes(groups=series_groups)

            print("Choose one or more groups to be removed, use the number displayed at left of the group title.")
            input_str = input("Type numbers separated by comma: ")
            ids = list(map(int, input_str.strip().split(',')))

            groups_to_remove = [series_groups[id] for id in ids]
            if helpers.user_confirmation():
                svc.remove_groups(groups_to_remove=groups_to_remove)

        if escolha == '3':
            print("Returning... \n")
            break
